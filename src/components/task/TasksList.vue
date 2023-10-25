<template>
  <div class="tasks-list">
    <div  
      v-for="task in tasks"
      :key="task.id"  
      class="task" 
    >
      <Task :task="task" />
      <div class="task-complete-button">
        <img @click="$emit('task-complete',task.id)" src="@/assets/images/Checkmark.png" width="60" height="60">
      </div>
    </div>
  </div>
</template>

<script>
import Task from './Task.vue';
    export default{
        components:{
          Task
        },
        props:{
            tasks:{
                type:Array,
                required: true
            }
        },
      
        emits:['task-complete'],
        computed:{
          
        },
        methods:{

        },
        
    }
</script>



<style>

.task-complete-button{
  display: inline-block;
  margin-left: 5%;
  vertical-align:bottom;
}
</style>