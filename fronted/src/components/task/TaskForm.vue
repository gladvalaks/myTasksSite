<template>
  <div class="task-redact-form">
    <ValidationForm 
      :validation-schema="schema"
      @submit="form" 
       >
      <div>
        <Field 
          v-model="this.task_body.title"
          name="title" 
          class="task-input-text" 
          type="text"
          placeholder="Введите название вашей задачи" 
        />
        <ErrorMessage 
          name="title" 
          class="input-error" 
        />
        <Field 
          v-model="task_body.description"
          as="textarea" 
          name="description" 
          class="task-input-text-description" 
          type="text"
          placeholder="Введите описание вашей задачи, если оно требуется"   
        />
        <div class="container-coins">
          <h4>Введите количество монеток за выполнение задания</h4>
          
          <Field 
            v-model="task_body.coins"
            name="coins"
            class="task-input-coins" 
            type="number" 
            min="1" 
            max="10" 
          />

          <ErrorMessage 
            name="coins" 
            class="input-error" 
          />
        </div>
        <div class="is-daily">
          <h4>Это будет ежедневное ваше задание (Задания такого типа будут появляться каждый день)?</h4>
          <input 
            v-model="task_body.isDaily" 
            type="checkbox" 
          >
        </div>
      </div>
      <button class="button-create" v-if="!task" >
        Создать задачу
      </button>
      <button class ="button-redact" v-else >
        Редактировать задачу
      </button>
    </ValidationForm>
  </div>
</template>

<script>
import { Field, Form as ValidationForm, ErrorMessage } from 'vee-validate'
import * as yup from 'yup';


export default {
  components: {
    ValidationForm,
    Field,
    ErrorMessage
  },
  props:{
    task: {
      type: Object,
      required: false
    }
  },
  emits: ["create-task","redact-task"],

  data() {
    return {
      task_body: {
        id: this.task ? this.task.id: 0,
        title: this.task ? this.task.title: "",
        description: this.task ? this.task.description:"",
        coins: this.task ? this.task.coins: 0,
        is_daily: this.task ? this.task.is_daily: false,
        task_priority_id: this.task ? this.task.task_priority_id:1,
      },
      
      schema:
        yup.object({
          title: yup.string()
            .min(4, "Название должно быть длиннее 4 символов"),
          coins: yup.number()
            .min(1, "Количество монеток должно быть больше 1")
        })
    };
    
  },
  computed: {
  },
  methods: {
    form(){
      if(this.task){
        this.redact();
      }
      else{
        this.create();
      }
    },
    redact() {
      const task = {
        id: this.id,
        title: this.title,
        description: this.description,
        coins: this.coins,
        is_daily: this.isDaily,
        task_priority_id: this.task_priority_id
      };

      this.$emit('redact-task', this.task_body);
    },
    create() {
      this.$emit('create-task', this.task_body);
    }
  },

}

</script>

<style>
.task-form {
  display: flex;
  flex-direction: column;
  width: 100%;
  border: 2px solid teal;
}

.task-input-text,
.task-input-text-description {
  margin: 1%;
  width: 95%;
  max-width: 95%;
  min-width: 95%;
  max-height: 13vh;
  border: 1px solid teal;
  padding: 1% 1%;
}
.task-input-text-description{
  min-height: 4vh;
}
.container-coins > * {
  display: inline-block;
  margin: 1%;
}

.is-daily > * {
  display: inline-block;
  margin: 1%;
}


.task-input-coins {
  max-width: 10%;
  min-width: 10%;
  padding: 0.5% 0.5%;
  border: 1px solid teal;
}

.button-create {
  width: 50%;
  font-size: 1.2vw;
  background: none;
  color: teal;
  border: 1px solid teal;
  margin: 1%;
  margin-left: 25%;
}

.input-error {
  color: red;
  margin: 1%;
}
</style>