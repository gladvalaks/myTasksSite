<template>
  <div class="not-completed-task-list">
    <div 
      v-for="task in tasks" 
      :key="task.id" 
      :class="[task.important ? 'task-important':'task']"
    >
    <NotCompletedTask 
        :task="task"
        @task-delete = "(id)=>$emit('task-delete',id)" 
        @task-complete ="(id)=>$emit('task-complete',id)"
        
      />
    </div>
  </div>
</template>

<script>
import NotCompletedTask from './NotCompletedTask.vue';
import TaskButtons from './TaskButtons.vue';
export default {
  components: {
    NotCompletedTask,
    TaskButtons
  },
  props: {
    tasks: {
      type: Array,
      required: true
    }
  },

  emits: ['task-complete','task-delete','task-change-important-status'],
  computed: {

  },
  methods: {

  },

}
</script>



<style>
.task-buttons{
  display: inline-block;
  margin-left: 0%;

}
.task-complete-button, .task-cancel-button, .task-star-button{
  display: inline-block;
  margin-left: 5%;
}
.not-completed-task-list{
  border: 1px teal solid;
  overflow-y: scroll;
  height: 50vh;
}
</style>