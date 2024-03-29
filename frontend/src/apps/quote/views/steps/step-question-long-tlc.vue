<template>
  <quote-process-layout>
    <quote-summary></quote-summary>
    <quote-process-radio-form :answers="answers" name="years" v-model="value" @next="onNext">
      How long have you had your TLC license?
    </quote-process-radio-form>
  </quote-process-layout>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator';

import { Getter, Action, namespace } from 'vuex-class';
import { Route } from 'vue-router';

import { QuestionsStep } from '@/@types/quote';

import { RadioElement } from '@/apps/quote/components/@types/forms'
import QuoteProcessRadioForm from '@/apps/quote/components/forms/quote-process-radio-form.vue'
import QuoteProcessLayout from '@/components/layout/quote-process-layout.vue'
import QuoteSummary from '@/apps/quote/components/containers/quote-summary.vue'


import { OrderedQuoteRouteName, QuoteProcessRouter } from '@/router/quote'

// Question Step 

const quote = namespace('Quote')

@Component({
  components: {
    QuoteProcessLayout, QuoteProcessRadioForm, QuoteSummary
  }
})
export default class StepQuestionLongTlc extends Vue {
  @quote.Getter
  questionAnswers!: QuestionsStep;

  @quote.Getter
  stepCompletedByName!: (route: OrderedQuoteRouteName) => boolean

  @quote.Action
  updateStepStatus!: (payload: { step: string, value: boolean }) => void;

  @quote.Action
  updateQuestionAnswers!: (payload: QuestionsStep) => void;

  value = ''
  
  answers = [
    {
      label: '+3 years',
      value: '3+'
    },
    {
      label: '1 - 3 years',
      value: '1-3'
    },
    {
      label: '<1 year',
      value: '<1'
    }
  ]

  onNext(): void {
    this.updateQuestionAnswers({ tlc_license_years: this.value })
    this.updateStepStatus({ step: this.$route.name!, value: true });
    this.$router.push(QuoteProcessRouter.nextRoute(this.$route.name!))
  }

  created(): void {
    this.value = this.questionAnswers.tlc_license_years || ''
  }

  resetState(): void {
    this.value = '';
    this.updateQuestionAnswers({ tlc_license_years: undefined });
    this.updateStepStatus({ step: this.$route.name!, value: false });
  }

  beforeRouteEnter (to: Route, from: Route, next: any): void {
    next((vm: StepQuestionLongTlc) => {
      if (!from.name || QuoteProcessRouter.isBefore(from.name, vm.$route.name!)) {
        vm.resetState();
      }

      if (!vm.stepCompletedByName(QuoteProcessRouter.previousRouteName(vm.$route.name!))) {
        vm.resetState();
        vm.$router.replace(QuoteProcessRouter.previousRoute(vm.$route.name!));
      }
    })
  }
}
</script>

<style lang='scss' scoped>

</style>
