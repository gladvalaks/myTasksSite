<template>
  <div class="main-page">
    <div class="daily-tasks">
      <p>Заглушка</p>
    </div>

    <div class="create-task">
      <TaskForm @create-task="addTask" />
    </div>

    <div class="tasks-list">
      <TasksList
        :tasks="notCompletedTasks"
        @task-complete="completeTask"
        @task-delete="deleteTask"
        @task-change-important-status="changeImportantStatusTask"
      />
    </div>

    <div class="completed-tasks-list">
      <CompletedTasksList :completed-tasks="completedTasks" />
    </div>

    <div class="user">
      <UserProgress
        :user-coins="userCoins"
        :user-coins-required="userCoinsRequired"
      />
    </div>
  </div>
</template>

<script>
import TasksList from '@/components/task/TasksList.vue';
import TaskForm from '@/components/task/TaskForm.vue';
import UserProgress from "@/components/user/UserProgress.vue";
import CompletedTasksList from '@/components/task/CompletedTasksList.vue';

export default {
  components: {
    TasksList,
    TaskForm,
    UserProgress,
    CompletedTasksList
  },

  data() {
    return {
      userCoins: 0,
      userCoinsRequired: 10,
      tasks: [
        {
          id: 1,
          title: "Сходить в тренажерный зал",
          description: "Жим лежа 5 по 70, подтягивания 5 по 10.",
          coins: 1,
          isDaily: false,
          wasCompleted: false,
          important: false
        },
        {
          id: 2,
          title: "Прочитать 3 главы Чистого кода",
          description: "Составить краткий план прочитанных глав",
          coins: 10,
          isDaily: false,
          wasCompleted: false,
          important: true
        },
      ]
    }
  },
  computed: {
    notCompletedTasks() {
      return this.tasks.filter((task) => !task.wasCompleted);
    },
    completedTasks() {
      return this.tasks.filter((task) => task.wasCompleted);
    },
    sortedByImportantTasks() {
      const importantTasks = this.tasks.slice(0, this.tasks.length);
      return importantTasks.sort((a, b) => b.important - a.important);
    }

  },
  methods: {
    addTask(task) {
      this.tasks.push(task);
    },

    completeTask(id) {
      const task = this.findTask(id);
      task.wasCompleted = true;
      this.userCoins += task.coins;
    },

    changeImportantStatusTask(id) {
      const task = this.findTask(id);
      task.important = !task.important;
    },

    deleteTask(id) {
      const taskPos = this.tasks.indexOf(this.tasks.find(task => task.id == id));
      this.tasks.splice(taskPos, 1);
    },

    findTask(id) {
      return this.tasks.find(task => task.id == id);
    }
  }
}
</script>

<style>
*{
  margin:0px;
  padding:0px;
}
.main-page{
  height: 98vh;
  display:grid;
  grid-template-rows: repeat(2,1fr);
  grid-template-columns: repeat(8,1fr);
  grid-template-areas:
    "daily-tasks daily-tasks daily-tasks daily-tasks create-task create-task user user"
    "task-list task-list task-list task-list completed-tasks-list completed-tasks-list completed-tasks-list    completed-tasks-list"
    
}
.daily-tasks{
  grid-area: daily-tasks;
  height:100%;
  padding: 1%;
  
}
.create-task{
  grid-area: create-task;
  max-height: 50vh;
  padding: 1%;
}
.user{
  grid-area: user;
  height:100%;
  padding: 1%;
}
.tasks-list{
  grid-area: task-list;
  height:100%;
  padding: 1%;
}
.completed-tasks-list{
  grid-area:  completed-tasks-list;
  height:100%;
  padding: 1%;
}
</style>