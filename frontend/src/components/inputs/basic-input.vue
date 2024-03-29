<docs>

</docs>

<template>
  <div class="container-input">
    <div class="box-input" :class="{'check': showCheck,'wrong':error}">
      <input
        :type="type"
        :name="inputName"
        :placeholder="placeholder"
        :id="id"
        :required="required"
        :minlength="minlength"
        :maxlength="maxlength"
        :value="value"
        :readonly="readonly"
        :disabled="disabled"
        @input="input"
        @keyup="onKeyUp"
        @keyup.enter="$emit('keyupEnter')"
        >
      <component
        v-bind:is="iconComponent"
        size="16"
        class="icon--grey"
        v-if="!showCheck"
      ></component>
      <icon-check-circle size="16" class="blue-check" v-else></icon-check-circle>
    </div>
    <p class="help-text" v-if="helpText"> 
      {{ helpText }}
    </p>
    <p class="input-alert">
      <slot name="error"></slot>
    </p>
  </div>
</template>

<script lang="ts">
import { VueConstructor } from 'vue';

import { Component, Prop, Vue, Model, Emit, Watch } from 'vue-property-decorator';

import IconCar from '@/components/icons/icon-car.vue'
import IconIdCard from '@/components/icons/icon-id-card.vue'
import IconCheckCircle from '@/components/icons/icon-check-circle.vue'
import IconEnvelope from '@/components/icons/icon-envelope.vue'
import IconLock from '@/components/icons/icon-lock.vue'
import IconPhone from '@/components/icons/icon-phone.vue'
import IconUser from '@/components/icons/icon-user.vue'

type Icon = 'car' | 'envelope' | 'id-card'| 'lock' | 'phone' | 'user';

@Component({
  components: {
    IconCheckCircle,
  }
})
export default class BasicInput extends Vue {

  @Prop()
  placeholder?: string;

  @Prop()
  id?: string;

  @Prop({ default: false })
  disabled?: boolean;

  @Prop({ default: false })
  required?: boolean;

  @Prop({ default: false })
  readonly?: boolean;

  @Prop()
  inputName!: string;

  @Prop({ default: '' })
  helpText?: string;

  @Prop({ default: 'text' })
  type?: string;

  @Prop()
  icon?: Icon;
  
  @Prop()
  minlength?: number;

  @Prop()
  maxlength?: number;

  @Prop({ default: false })
  error?: boolean

  @Prop({ default: true })
  validate?: boolean

  @Prop()
  value!: string

  @Watch('invalid')
  validChange(): void {
    this.$emit('valid', !this.invalid)
  }

  input(event: { target: HTMLInputElement; }): void {
    this.$emit('input', event.target.value);
  }

  @Emit('keyup')
  onKeyUp(event: Event): any {
    return event;
  }

  get iconComponent(): VueConstructor<Vue> | undefined {
    switch (this.icon) {
      case 'id-card':
        return IconIdCard;
      case 'car':
        return IconCar;
      case 'envelope':
        return IconEnvelope;
      case 'phone':
        return IconPhone;
      case 'user':
        return IconUser;
      case 'lock':
        return IconLock;
      default:
        return undefined;
    }
  }

  get emailValid(): boolean {
    return this.type !== 'email' || !this.required || (!!this.value && /.*@*.\.{1}.\w/.test(this.value))
  }

  get invalid(): boolean {
    return !this.emailValid || (!this.minlength && this.value === '') || (this.minlength && (!this.value || this.value.length < this.minlength)) || !this.validate
  }

  get showCheck(): boolean {
    return !this.invalid && !this.disabled
  }

  created(): void {
    this.validChange();
  }
}
</script>

<style lang="scss" scoped>
.icon--grey {
  color: $grey;
}

.blue-check {
  color: $blue;
}

.container-input {
  .input-alert {
    font-size: $fs-md;
    margin-top: 0.25rem;
    text-align: left;
    line-height: 1.33;
    span {
      font-size: $fs-md;
      margin-top: 0.25rem;
      text-align: left;
      line-height: 1.33;
    }
  }
}
.box-input {
  align-items: center;
  background-color: $white;
  border: 1px solid $grey;
  border-radius: 2px;
  display: flex;
  margin-left: auto;
  margin-right: auto;
  justify-content: space-between;
  position: relative;
  padding: 0.625rem 0.75rem;
  &.wrong {
    animation: wrong-log 0.3s;
    border: 1px solid $orange;
  }
  &.check {
    border: 1px solid $blue;
    box-shadow: 0 0 3px 0 rgba(66, 99, 235, 0.5);
  }
  input {
    color: $blue-dark;
    font-size: $fs-lg;
    letter-spacing: 0.2px;
    width: calc(100% - 1.5rem);
  
    &::placeholder {
      color: $grey;
    }
    &:focus {
      outline: none;
    }

    &:disabled {
      color: $grey-darker;
    }
  }
}

.help-text {
  color: $blue-dark;
  font-size: $fs-sm;	
  line-height: 17px;
  margin-top: 0.375rem;
	opacity: 0.5;	
  text-align: left;
}

@keyframes wrong-log {
  0% {
    left: 0px;
  }
  20% {
    left: 15px;
  }
  40% {
    left: -15px;
  }
  60% {
    left: 15px;
  }
  80% {
    left: -15px;
  }
  100% {
    left: 0px;
  }
}
</style>