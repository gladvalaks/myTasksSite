<template>
  <div class="task-content">
    <TaskTemplate :task="task" />
  </div>
  <h1 class="task-coins">
    {{ task.coins }}
  </h1>
  <div class="task-buttons">
        <TaskButtons :id="task.id"
        @task-delete = "(id)=>$emit('task-delete',id)" 
        @task-complete = "(id)=>$emit('task-complete',id)"/>       
  </div>
</template>
  
<script>
import TaskTemplate from './TaskTemplate.vue';
import TaskButtons from './TaskButtons.vue';
export default {
  components: {
    TaskTemplate, TaskButtons
},
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  emits:[
    "task-delete","task-complete"
  ]
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