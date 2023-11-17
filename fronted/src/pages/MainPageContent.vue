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
        @redact-task="redactTask"
      />
    </div>

    <div class="completed-tasks-list">
      <CompletedTasksList 
      :completed-tasks="completedTasks"
      @task-uncomplete = "uncompleteTask" />
    </div>

    <div class="user">
      <UserProgress
        :user-coins="userCoins"
        :user-coins-required="userCoinsRequired"
        :user-name = "userName"
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
import axios from "axios"


export default {
  components: {
    TasksList,
    TaskForm,
    UserProgress,
    CompletedTasksList,
    DailyTaskList
},
   created(){

    this.updateTaskList()
    this.getUserName()

  }
            ,
  data() {
    return {
      userName : "",
      userCoinsRequired: 10,
      sortMethod: "byDate",
      tasks: []
    }
  },
  computed: {
    userCoins()
    { 
      return this.completedTasks.reduce((acc,task)=> {return acc+task.coins},0);
    },
    notCompletedTasks() { 
      return this.sortedTasks().filter((task) => !task.finished_at && !task.is_daily);
    },
    notCompletedDailyTasks() {
      return this.sortedTasks().filter((task) => !task.finished_at && task.is_daily);
    },
    completedTasks() {
      return this.sortedTasks().filter((task) => +new Date().setHours(0,0,0,0)== +new Date(task.finished_at).setHours(0,0,0,0));
    },

  },
  methods: {
    async addTask(task) {
      console.log("add");
      await axios.post("http://tasks.localhost.com/api/tasks",task)
      this.updateTaskList();
    },
    async redactTask(task) {
      console.log(task);
      await axios.put(`http://tasks.localhost.com/api/tasks/${task.id}`,task)
      this.updateTaskList();
    },
    async completeTask(id) {
      await axios.post(`http://tasks.localhost.com/api/tasks/${id}/complete`).then((response)=> console.log(response));
      this.updateTaskList();
    },
    async uncompleteTask(id) {
      await axios.post(`http://tasks.localhost.com/api/tasks/${id}/uncomplete`).then((response)=> console.log(response));
      this.updateTaskList();
    },
    async deleteTask(id) {
      await axios.delete(`http://tasks.localhost.com/api/tasks/${id}`).then((response)=> console.log(response));
      this.updateTaskList();
    },
    async updateTaskList(){
      this.tasks = await axios.get("http://tasks.localhost.com/api/tasks").then((response) => {
        return response.data
      })
      .catch(()=>this.$router.push("/login"))
    },
    async getUserName(){
      this.userName = await axios.get("http://tasks.localhost.com/api/user").then((response) => {
        return response.data
      })
      .catch(()=>this.$router.push("/login"))
    },

    changeImportantStatusTask(id) {
      const task = this.findTask(id);
      task.important = !task.important;
    },

    
    findTask(id) {
      return this.tasks.find(task => task.id == id);
    },
    changeSortMethod(sortMethod){
      this.sortMethod = sortMethod;
    },
    sortedTasks(){
      if(this.sortMethod=="byDate"){
        console.log(this.sortedByDateTasks())
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
      return this.tasks.sort((a, b) => a.created_at- b.created_at);
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