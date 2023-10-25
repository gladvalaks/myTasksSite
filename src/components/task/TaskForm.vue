<template>
  <div class="task-form">
    <form @submit.prevent>
      <input v-model="title" class="task-input-text" type="text">
      <input v-model="description" class="task-input-text-description" type="text">
      <input v-model="coins" class="task-input-text" type="number" min="1" max="10">
      <button class="button-create" @click="create">
        Создать задачу
      </button>
    </form>
  </div>
</template>

<script>
import {v4 as uuid4} from 'uuid'

export default {
  emits: ["create-task"],

  data() {
    return {
      title: "",
      description: "",
      coins: 0,
    }
  },

  methods: {
    isValid() {
      return (
        this.title.length < 4 || this.coins > 10 || this.coins < 1
      );
    },

    create() {
      if (this.isValid()) {
        return;
      }

      const task = {
        id: uuid4(),
        title: this.title,
        description: this.description,
        coins: this.coins,
        isTaskComplete: false
      };

      this.$emit('create-task', task);
    }
  }
}

</script>

<style>
.task-form {
  display: flex;
  flex-direction: column;
  width: 100%;
  border: 1px solid teal;
}

.task-input-text,
.task-input-text-description {
  margin: 1%;
  width: 95%;
  border: 1px solid teal;
  padding: 1% 1%;
}

.button-create {
  margin-bottom: 10px;
  width: 98%;
  align-self: flex-end;
  padding: 10px 15px;
  background: none;
  color: teal;
  border: 1px solid teal;
  margin: 1%;
}
</style>