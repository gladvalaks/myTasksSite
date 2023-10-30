<script>
import TaskTemplate from '../task/TaskTemplate.vue';


export default {
  components: {
    TaskTemplate,
  },
  props: {
    completedTasks: {
      type: Array,
      required: true
    },
  },

}
</script>

<template>
  <div>
    <h2>
      Сегодня вы выполнили такие задания
    </h2>
    <div class="completed-task-list">
      <div 
        v-for="task in completedTasks" 
        :key="task.id" 
        class="task"
      >
        <TaskTemplate :task="task" />
      </div>
    </div>
  </div>
</template>


<style>
.task-content {
  display: inline-block;
  width: 95%;
  word-wrap: break-word;
}

.task {
  border: 2px solid teal;
  padding: 10px;
  margin-top: 10px;
}


.completed-task-list {
  border: 1px teal solid;
  overflow-y: scroll;
  height: 47vh;
}
</style>