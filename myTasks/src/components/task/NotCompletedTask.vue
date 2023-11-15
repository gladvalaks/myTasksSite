<template>
  <div class="task-content">
    <TaskTemplate :task="task" />
  </div>
  <h1 class="task-coins">
    {{ task.coins }}
  </h1>
</template>
  
<script>
import TaskTemplate from './TaskTemplate.vue';
export default {
  components: {
    TaskTemplate
},
  props: {
    task: {
      type: Object,
      required: true
    }
  }
}
</script>
  
<style>
.task-coins {
  font-size: 50px;
  text-align: center;
  display: inline-block;
  width: 60px;
  height: 60px;
  margin-left: 5%;
  color: white;
  border: 2px solid lightblue;
  background-color: green;
}

.task-content {
  display: inline-block;
  max-width: 80%;
  word-wrap: break-word;
}
</style>