<script>
import Task from '../task/Task.vue';
export default{
  components:{
    Task,
  },
    props:{
        userCoins:{
            type: Number,
            required:true
        },
        completedTasks:{
          type:Array,
          required:true
        },
        userCoinsRequired:{
          type:Number,
          required:true
        }
    },
  
}
</script>

<template>
  <div
    class="user-progress"
  >
    <h1>Ваш Прогресс</h1>
    <h1 
      class="user-coins"
    > 
      <p>{{ userCoins }} / {{ userCoinsRequired }}</p>
    </h1>
    <h2 
      v-if="userCoins/userCoinsRequired<0.5"
    >
      Сегодня вы мало выполнили задач, постарайтесь еще, и у вас все получится
    </h2>
    <h2 
      v-else-if="userCoins/userCoinsRequired==1"
    >
      Поздравляем, ваш день был очень продуктивен
    </h2>
    <h2 
      v-else-if="userCoins/userCoinsRequired>1"
    >
      Поздравляем, вы сделали больше чем требовалось, вы большой молодец
    </h2>
    <h2 
      v-else
    >
       Вы уже правили свой день с пользой, осталось чуть-чуть поднажать до закрытия ежедневной цели
    </h2>
    <h2 v-show="completedTasks.length"> Сегодня вы выполнили такие задания </h2>
    <div class="task" v-for="task in completedTasks" :key="task.id">
      <Task :task="task" />
    </div>
  </div>
</template>


<style>
.task-content{
  display: inline-block;
  width: 95%;
  word-wrap: break-word;
}
.user-progress{
  padding: 5%;
  border: 2px solid blueviolet;
  word-wrap: break-word;
}
.task{
  border: 2px solid teal;
  padding: 10px;
  margin-top: 10px;
}
.completed-task-content{
  display: inline-block;
  width: 100%;
  word-wrap: break-word;
}
</style>