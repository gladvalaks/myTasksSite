<template>
  <div class="task-text">
    <h2> {{ task.title }}</h2>
    <p v-show="task.description">
      {{ task.description }}
    </p>   
  </div>
</template>

<script>
export default{
  props:{
    task:{
      type: Object,
      required: true
    }
  }
}
</script>

<style>
.task-text{
  display: inline-block;
  max-width: 100%;
  word-wrap: break-word;
}

</style>