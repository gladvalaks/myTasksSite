<template>
  <div>
    <div class="tasks">
      <TaskForm @create-task="addTask" />
      <TasksList 
        :tasks="notCompletedTasks" 
        @task-complete="taskComplete"  
      />
    </div>

    <div class="user">
      <UserProgress 
      :userCoins="userCoins" 
      :completedTasks ="completedTasks"
      :userCoinsRequired = "userCoinsRequired"
      />
    </div>
  </div>
</template>

<script>
import TasksList from '@/components/task/TasksList.vue';
import TaskForm from '@/components/task/TaskForm.vue';
import UserProgress from "@/components/user/UserProgress.vue";

export default {
  components: {
    TasksList,
    TaskForm,
    UserProgress
  },

  data() {
    return {
      userCoins: 0,
      userCoinsRequired:10,
      tasks: [
        {
          id: 1,
          title: "Сходить в тренажерный зал",
          description: "Жим лежа 5 по 70, подтягивания 5 по 10.",
          coins: 1,
          wasCompleted: false
        },
        {
          id: 2,
          title: "Прочитать 3 главы Чистого кода",
          description: "Составить краткий план прочитанных глав",
          coins: 10,
          wasCompleted: false
        },
      ]
    }
  },
  computed:{
    notCompletedTasks(){
            return this.tasks.filter((task)=>!task.wasCompleted);
          },
    completedTasks(){
      return this.tasks.filter((task)=>task.wasCompleted)
    }
  },
  methods: {
    addTask(task) {
      this.tasks.push(task);
    },
    taskComplete(id){
      const task = this.tasks.find(task=> task.id == id);
      task.wasCompleted = true;
      this.userCoins += task.coins;
    }
  }
}
</script>

<style>
* {
  padding: 0px;
  margin: 0px;
}

body {
  padding: 25px;
}

.tasks {
  display: inline-block;
  padding: 10px;
  width: 50%;
}

.user {
  display: inline-block;
  vertical-align: top;
  padding: 10px;
  margin-left: 5%;
  width: 40%;
}</style>