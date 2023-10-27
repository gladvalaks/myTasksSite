<script>
import UserDayStatus from './UserDayStatus.vue';

export default {
  components: {
    UserDayStatus,
  },
  props: {
    userCoins: {
      type: Number,
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
    <UserDayStatus
      :user-coins="userCoins"
      :user-coins-required="userCoinsRequired"
    />
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