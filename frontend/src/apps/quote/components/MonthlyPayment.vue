<template>
  <div class="montly-estimated" v-if="this.internalDate === ''">
    <h3>Monthly payment</h3>

    <div class="month-record">
      <span>October XX</span>
      <span class="estimated-price-no-data">$--</span>
    </div>
    <div class="month-record">
      <span>November XX</span>
      <span class="estimated-price-no-data">$--</span>
    </div>

    <span class="estimated-date">The additional charge on each monthly payment is an installment fee charged by Hereford
    </span>
  </div>
  <div class="montly-estimated" v-else-if="this.internalDeposit === 100">
    <h3>Monthly payment</h3>

    <div class="month-record">
      <span>{{ date2 }}</span>
      <span class="estimated-price">$0 + $0</span>
    </div>
    <div class="month-record">
      <span>November {{ date1 }}</span>
      <span class="estimated-price">$0 + $0</span>
    </div>

    <span class="estimated-date">The additional charge on each monthly payment is an installment fee charged by Hereford
    </span>
  </div>
  <div class="montly-estimated" v-else>
    <h3>Monthly payment</h3>

    <div class="month-record">
      <span>{{ date2 }}</span>
      <span class="estimated-price">{{ fmp | beautyCurrency }}+{{ herefordFee | beautyCurrency }}</span>
    </div>
    <div class="month-record">
      <span>November {{ date1 }}</span>
      <span class="estimated-price">{{ omp | beautyCurrency }}+{{ herefordFee | beautyCurrency }}</span>
    </div>

    <span class="estimated-date">The additional charge on each monthly payment is an installment fee charged by Hereford
    </span>
  </div>
</template>

<script>
  import { currency, beautyCurrency } from '@/utils/text'
  import { format, addDays, differenceInDays } from 'date-fns';

  export default {
    props: {
      qrsf: Number,
      deposit: Number,
      internalDeposit: Number,
      internalDate: [Date, String]
    },
    computed: {
      date1() {
        return this.internalDeposit > 15 ? 21 : 15;
      },
      utc_date() {
        const date = new Date(this.internalDate); 
        const date_utc = new Date(date.getTime() + date.getTimezoneOffset() * 60000);

        return date_utc;
      },
      date2() {
        const days = this.internalDeposit > 15 ? 20 : 15;
        return format(addDays(this.utc_date, days), 'MMMM d')
      },
      herefordFee() {
        return this.internalDeposit === 15 ? 30 : this.internalDeposit === 20 ? 25 : 20;
      },
      nodp() {
        return differenceInDays(this.utc_date, new Date(2020, 2, 2));
      },
      prp() {
        return this.qrsf * (363 - this.nodp) / 363;
      },
      omp() {
        return this.qrsf * (100 - this.internalDeposit) / 900;
      },
      fmp() {
        return this.prp - this.deposit - this.omp;
      }
    },
    filters: {
      beautyCurrency
    }
  }
</script>

<style lang='scss' scoped>
  h3 {
    margin-bottom: 0.7rem;
  }
  .month-record {
    color: $blue;
    margin-top: 0.3rem;
    span {
      display: inline-block;
      width: 50%;

      &:first-child {
        text-align: center;
        font-size: 1rem;
      }

      &:last-child {
        text-align: left;
        font-weight: 600;
      }
    }
  }
  .montly-estimated {
    background-color: $white;
    border-radius: 2px;
    text-align: center;
    display: flex;
    flex-direction: column;
    flex: 1;
    min-width: 240px;

    span {
      font-size: $fs-lg;
    }
    .estimated-price-no-data {
      text-align: center !important;
    }
    .estimated-date {
      background-color: $grey-light;
      font-size: $fs-sm;
      margin: 10px auto 0;
      opacity: 0.5;
      padding: 0.5rem;
    }
  }
</style>