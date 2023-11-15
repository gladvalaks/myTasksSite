<template>
  <div class="task-content">
    <h2> {{ task.title }}</h2>
    <p v-show="task.description">
      {{ task.description }}
    </p>   
  </div>
  <h1 v-show="!task.wasCompleted" class="task-coins">
    {{ task.coins }}
  </h1> 
</template>

<script>
export default{
  props:{
    task:{
      type: Object,
      required: true
    }
  }
}
</script>

<style>
.task-coins{
  font-size: 50px;
  text-align: center;
  display: inline-block;
  width: 60px;
  height: 60px;
  margin-left: 5%;
  color:white;
  border: 2px solid lightblue;
  background-color: green;
}
.task{
  border: 2px solid teal;
  padding: 10px;
  margin-top: 10px;
}
.task-content{
  display: inline-block;
  width: 60%;
  word-wrap: break-word;
}

</style>