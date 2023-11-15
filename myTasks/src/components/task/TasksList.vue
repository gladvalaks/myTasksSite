<template>
  <div class="not-completed-task-list">
    <div 
      v-for="task in tasks" 
      :key="task.id" 
      :class="[task.important ? 'task-important':'task']"
    >
      <NotCompletedTask :task="task" />
      <div class="task-buttons">
        <div class="task-complete-button">
          <img             
            src="@/assets/images/Checkmark.png" 
            width="30" 
            height="30"
            @click="$emit('task-complete', task.id)" 
          >
        </div>
        <div class="task-cancel-button">
          <img             
            src="@/assets/images/Cancel.png" 
            width="30" 
            height="30"
            @click="$emit('task-delete', task.id)" 
          >
        </div>
        <div class="task-star-button">
          <img             
            src="@/assets/images/star.jpg" 
            width="30" 
            height="30"
            @click="$emit('task-change-important-status', task.id)" 
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NotCompletedTask from './NotCompletedTask.vue';
export default {
  components: {
    NotCompletedTask
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