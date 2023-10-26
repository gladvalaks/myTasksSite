<template>
  <div class="tasks-list">
    <div v-for="task in tasks" :key="task.id" class="task">
      <NotCompletedTask :task="task" />
      <div class="task-buttons">
        <div class="task-complete-button">
          <img @click="$emit('task-complete', task.id)" src="@/assets/images/Checkmark.png" width="30" height="30">
        </div>
        <div class="task-cancel-button">
          <img @click="$emit('task-delete', task.id)" src="@/assets/images/Cancel.png" width="30" height="30">
        </div>
        <div class="task-star-button">
          <img @click="$emit('task-delete', task.id)" src="@/assets/images/star.jpg" width="30" height="30">
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

  emits: ['task-complete','task-delete'],
  computed: {

  },
  methods: {

  },

}
</script>



<style>
.task {
  border: 2px solid teal;
  padding: 1%;
  margin-top: 10px;
}
.task-buttons{
  display: inline-block;
  margin-left: 60%;

}
.task-complete-button, .task-cancel-button, .task-star-button{
  margin-left: 5%;
}
.tasks-list{
  overflow-y: auto;
  height: 500px;
}
</style>