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
.task {
  border: 2px solid teal;
  padding: 1%;
  margin-top: 10px;
}

.task-important{
  border: 2px solid teal;
  padding: 1%;
  margin-top: 10px;
  background-color: rgb(255, 0, 0);
}
</style>