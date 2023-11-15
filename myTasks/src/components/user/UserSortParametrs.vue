<template>
  <div class="sort-method-container">
    <div>
      <input id="sort-by-date" type="radio" name="sort-method" checked @change="$emit('change-sort-method', 'byDate')">
      <label for="sort-by-date">Сортировать задачи по дате их создания</label>
    </div>

    <div>
      <input id="sort-by-coins" type="radio" name="sort-method" @change="$emit('change-sort-method', 'byCoins')">
      <label for="sort-by-coins">Сортировать задачи по количеству монет</label>
    </div>

    <div>
      <input id="sort-by-important" type="radio" name="sort-method" @change="$emit('change-sort-method', 'byImportant')">
      <label for="sort-by-important">Сортировать задачи по важности</label>
    </div>
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