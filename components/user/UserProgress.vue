<script>
import UserDayStatus from './UserDayStatus.vue';
import UserSortParametrs from './UserSortParametrs.vue';

export default {

  components: {
    UserDayStatus,
    UserSortParametrs
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
  emits:["change-sort-method"],

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
    <UserSortParametrs @change-sort-method="(sortMethod)=>$emit('change-sort-method',sortMethod)" />
  </div>
</template>


<style>
.user-progress {
  padding: 5%;
  border: 2px solid blueviolet;
  word-wrap: break-word;
}

</style>