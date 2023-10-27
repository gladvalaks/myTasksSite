<template>
  <h2 v-if="userCoins / userCoinsRequired < 0.5">
    Сегодня вы мало выполнили задач, постарайтесь еще, и у вас все получится
  </h2>
  <h2 v-else-if="userCoins / userCoinsRequired == 1">
    Поздравляем, ваш день был очень продуктивен
  </h2>
  <h2 v-else-if="userCoins / userCoinsRequired > 1">
    Поздравляем, вы сделали больше чем требовалось, вы большой молодец
  </h2>
  <h2 v-else>
    Вы уже правили свой день с пользой, осталось чуть-чуть поднажать до закрытия ежедневной цели
  </h2>
</template>
<script>
export default{
  props:{
    userCoins:{
      type: Number,
      required: true
    },
    userCoinsRequired:{
      type: Number,
      required: true
    }
  }
}
</script>

<style></style>