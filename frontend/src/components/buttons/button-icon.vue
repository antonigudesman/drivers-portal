<template>
  <button class="basic-button" @click="$emit('click',$event)" :disabled="disabled" :title=title>
    <slot></slot>
  </button>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';

@Component
export default class ButtonIcon extends Vue {
  @Prop()
  text!: string;

  @Prop({ default: '' })
  title!: string;

  @Prop({ default: false })
  disabled?: boolean
}
</script>

<style lang="scss" scoped>
  .basic-button{
    align-items: center;
    cursor: pointer;
    justify-content: center;
    display: inline-flex;

    &:disabled{
      color: $grey-medium !important;
      cursor: not-allowed
    }
    &:focus{
      outline: none;
    }
  }
</style>