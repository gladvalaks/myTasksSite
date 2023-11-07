<template>
  <div class="main-page">
    <div class="daily-tasks">
      <DailyTaskList 
        :tasks="notCompletedDailyTasks"
        @task-complete="completeTask"
        @task-delete="deleteTask"
        @task-change-important-status="changeImportantStatusTask" 
      />
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
        @change-sort-method="changeSortMethod"
      />
    </div>
  </div>
</template>

<script>
import TasksList from '@/components/task/TasksList.vue';
import TaskForm from '@/components/task/TaskForm.vue';
import UserProgress from "@/components/user/UserProgress.vue";
import CompletedTasksList from '@/components/task/CompletedTasksList.vue';
import DailyTaskList from '../components/task/DailyTaskList.vue';


export default {
  components: {
    TasksList,
    TaskForm,
    UserProgress,
    CompletedTasksList,
    DailyTaskList
},

  data() {
    return {
      userCoins: 0,
      userCoinsRequired: 10,
      sortMethod: "byDate",
      tasks: [
        {
          id: 1,
          title: "Сходить в тренажерный зал",
          description: "Жим лежа 5 по 70, подтягивания 5 по 10.",
          coins: 1,
          isDaily: false,
          wasCompleted: false,
          important: false,
          date: Date.now(),
        },
        {
          id: 2,
          title: "Прочитать 3 главы Чистого кода",
          description: "Составить краткий план прочитанных глав",
          coins: 10,
          isDaily: false,
          wasCompleted: false,
          important: true,
          date: Date.now()+1,
        },
      ]
    }
  },
  computed: {
    notCompletedTasks() {
      return this.sortedTasks().filter((task) => !task.wasCompleted && !task.isDaily);
    },
    notCompletedDailyTasks() {
      return this.sortedTasks().filter((task) => !task.wasCompleted && task.isDaily);
    },
    completedTasks() {
      return this.sortedTasks().filter((task) => task.wasCompleted);
    },

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
    },
    changeSortMethod(sortMethod){
      this.sortMethod = sortMethod;
    },
    sortedTasks(){
      if(this.sortMethod=="byDate"){
        return this.sortedByDateTasks();
      }
      else if(this.sortMethod=="byCoins"){
        return this.sortedByCoinsTasks()
      }
      else{
        return this.sortedByImportantTasks();
      }
    },
    sortedByImportantTasks() {
      return this.tasks.sort((a, b) => b.important - a.important);
    },
    sortedByDateTasks() {
      return this.tasks.sort((a, b) => b.date - a.date);
    },
    sortedByCoinsTasks() {
      return this.tasks.sort((a, b) => b.coins - a.coins);
    },
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