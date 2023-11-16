<template>
  <div v-if="!onRedact" class="task-not-on-redact" >
    <div class="task-content">
      <TaskTemplate :task="task" />
    </div>
    <h1 class="task-coins">
      {{ task.coins }}
    </h1>
    <div class="task-buttons">
      <TaskButtons :id="task.id" @task-delete="(id) => $emit('task-delete', id)"
        @task-complete="(id) => $emit('task-complete', id)"
        @task-redact ="()=> onRedact = true" />
    </div>
  </div>
  <div v-else class ="on-redact" >
    <div class="task-content">
      <TaskRedactForm :task="task"
      @redact-task ="(task)=>$emit('redact-task',task)"/>
    </div>
  </div>
</template>
  
<script>
import TaskTemplate from './TaskTemplate.vue';
import TaskButtons from './TaskButtons.vue';
import TaskRedactForm from './TaskRedactForm.vue'
export default {
  components: {
    TaskTemplate, TaskButtons,
    TaskRedactForm
},
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  emits: [
    "task-delete", "task-complete"
  ],
  data() {
    return{
      onRedact: false
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