<template>
    <div class="svg-icon-center">
        <svg aria-hidden="true" data-prefix="fas" data-icon="chevron-down" class="svg-inline--fa fa-chevron-down fa-w-14" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" :width="size" :height="size"><path fill="currentColor" d="M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z"/></svg>
    </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';

@Component
export default class IconChevronDown extends Vue {
  @Prop()
  size?: string | number;
}
</script>

<style lang="scss" scoped>
  .svg-icon-center {
    display: flex;
  }
</style>
