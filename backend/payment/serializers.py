from rest_framework import serializers

from quotes.models import QuoteProcess
from payment.utils import (
    create_stripe_charge,
    get_or_create_stripe_customer,
    exchange_plaid_token,
)

from payment.models import Payment


class BaseStripeDepositChargeCreateSerializer:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = self.context.get("request")
        self.user = getattr(self.request, "user", None)

    def get_customer_source(self):
        raise NotImplementedError

    def get_payment_type(self):
        return self.payment_type

    def gen_customer_description(self):
        return "Customer {email} for Quote process {process} user {user}".format(
            **{
                "email": self.validated_data["email"],
                "process": self.validated_data["quote_process"].id.hex,
                "user": self.user.id.hex,
            }
        )

    def gen_charge_description(self):
        return "Stableins deposit charge to {email}. Quote process {process}.".format(
            **{
                "email": self.validated_data["email"],
                "process": self.validated_data["quote_process"].id.hex,
            }
        )

    def create_customer(self):
        customer_data = {
            "description": self.gen_customer_description(),
            "email": self.validated_data["email"],
            "user": self.user,
            "metadata": {"user": self.user.id.hex},
            "source": self.get_customer_source(),
        }
        return get_or_create_stripe_customer(**customer_data)

    def gen_charge_data(self, *, customer, token_source):
        data = {
            "payment_type": self.get_payment_type(),
            "description": self.gen_charge_description(),
            "amount": self.validated_data["amount"],
            "email": self.validated_data["email"],
            "user": self.user,
            "metadata": {
                "user": self.user.id.hex,
                "quote_process": self.validated_data["quote_process"].id.hex,
            },
            "product": self.validated_data["quote_process"].id.hex,
        }
        if customer:
            data.update({"customer": customer})
        if token_source:
            data.update({"source": token_source})
        return data

    def create_charge(self, *, customer, token_source=None):
        charge_data = self.gen_charge_data(customer=customer, token_source=token_source)
        return create_stripe_charge(**charge_data)


class StripeDepositChargeCreateSerializer(
    BaseStripeDepositChargeCreateSerializer, serializers.Serializer
):
    payment_type = "card"
    amount = serializers.FloatField()
    source = serializers.CharField()
    card_id = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField(required=False)

    def get_customer_source(self):
        return self.validated_data["source"]

    def create(self, validated_data):
        customer = self.create_customer()
        charge = self.create_charge(customer=customer)
        return charge


class PlaidDepositChargeCreateSerializer(
    BaseStripeDepositChargeCreateSerializer, serializers.Serializer
):
    payment_type = "bank_account"
    _bank_token = None
    quote_process = serializers.PrimaryKeyRelatedField(
        queryset=QuoteProcess.objects.all()
    )
    amount = serializers.FloatField()
    email = serializers.EmailField(required=False)
    public_token = serializers.CharField()
    account_id = serializers.CharField()

    def get_customer_source(self):
        return self._bank_token

    def create(self, validated_data):
        quote_process_instance = validated_data.pop("quote_process")
        exchange_data = {
            "public_token": validated_data["public_token"],
            "account_id": validated_data["account_id"],
        }
        self._bank_token = exchange_plaid_token(**exchange_data)
        customer = self.create_customer()
        charge = self.create_charge(customer=customer)
        return charge