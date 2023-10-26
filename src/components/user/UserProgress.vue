<script>
import TaskTemplate from '../task/TaskTemplate.vue';
import UserDayStatus from './UserDayStatus.vue';

export default {
  components: {
    TaskTemplate,
    UserDayStatus,
  },
  props: {
    userCoins: {
      type: Number,
      required: true
    },
    completedTasks: {
      type: Array,
      required: true
    },
    userCoinsRequired: {
      type: Number,
      required: true
    }
  },

}
</script>

<template>
  <div class="user-progress">
    <h1>Ваш Прогресс</h1>
    <h1 class="user-coins">
      <p>{{ userCoins }} / {{ userCoinsRequired }}</p>
    </h1>
    <UserDayStatus :userCoins="userCoins" :userCoinsRequired="userCoinsRequired" />
    <h2 v-show="completedTasks.length"> Сегодня вы выполнили такие задания </h2>
    <div class="tasks-list">
      <div class="task" v-for="task in completedTasks" :key="task.id">
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

.user-progress {
  padding: 5%;
  border: 2px solid blueviolet;
  word-wrap: break-word;
}

.task {
  border: 2px solid teal;
  padding: 10px;
  margin-top: 10px;
}

.completed-task-content {
  display: inline-block;
  width: 100%;
  word-wrap: break-word;
}
</style>