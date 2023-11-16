<template>
  <div class="sort-method-container">
    <select @change="($event) =>$emit('change-sort-method',$event.target.value)">
      <option id="sort-by-date" name="sort-method"
       value="byCoins">Сортировать задачи по дате их создания</option>
      <option id="sort-by-coins"  name="sort-method" value="byCoins">
      Сортировать задачи по количеству монет</option>
      <option id="sort-by-important"  name="sort-method" value="byImportant"
        >Сортировать задачи по важности</option>
  </select>
  </div>
</template>

<script>
export default {
  emits: ["change-sort-method"],

}
</script>

<style>

.sort-method-container div {
  display: block;
  font-size: 1vw;
}
</style>