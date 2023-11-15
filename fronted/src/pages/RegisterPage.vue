<template>
    <div class="register">
      <div class="register-form">
        <div>
        <h1>Регистрация</h1>
        <ValidationForm 
        :validation-schema="schema"
        @submit="register"
        >
        <Field 
          v-model="email"
          name="email" 
          class="register-form-input" 
          type="email"
          placeholder="Введите ваш email" 
        />
        <ErrorMessage 
          name="email" 
          class="input-error"
        />
        <Field 
          v-model="username"
          name="username" 
          class="register-form-input" 
          type="username"
          placeholder="Как к вам обращаться?" 
        />
        <ErrorMessage 
          name="username" 
          class="input-error"
        />
        <Field 
          v-model="password"
          name="password" 
          class="register-form-input" 
          type="password"
          placeholder="Введите ваш пароль" 
        />
        <ErrorMessage 
          name="password" 
          class="input-error"
        />
        <Field 
          v-model="passwordConfirm"
          name="passwordConfirm" 
          class="register-form-input" 
          type="password"
          placeholder="Подтвердите ваш пароль" 
        />
        <ErrorMessage 
          name="passwordConfirm" 
          class="input-error"
        />
        <button class="button-auth">Зарегистрироваться</button>
        </ValidationForm>
        </div>
      </div>
    </div>
</template>

<script>
import * as yup from 'yup';
import axios from 'axios';
import { Field, Form as ValidationForm, ErrorMessage } from 'vee-validate'
export default{
  components: {
    ValidationForm,
    Field,
    ErrorMessage
  },
  created(){

  },
  data(){
        return{
            email:"",
            password:"",
            passwordConfirm:"",
            username:"",
            schema:
              yup.object({
                email: yup.string().email("Некорректный email")
                .required("Обязательное поле").max(50,"аааааааааааа слишком много символов"),

                username: yup.string().required("Обязательное поле").max(20,"аааааааааааа слишком много символов"),

                password: yup.string().required("Обязательное поле")
                .min(6,"Пароль должен быть длиннее6 символов").max(50,"аааааааааааа слишком много символов"),

                passwordConfirm: yup.string().required("Обязательное поле").oneOf([yup.ref("password")],"Пароли не совпадают")

        })
        }
    },
  methods:{
        register(){
            const requestBody = {"email":this.email, "username":this.username, "password":this.password}
            axios.post("http://tasks.localhost.com/api/register",requestBody)
            .then(()=>this.$router.push("/login"))
            
        }
    }
}
</script>
  
<style>
.register{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
}
.register-form{
    grid-column-start: 2;
    grid-column-end: 3;
    grid-row-start: 2;
    grid-row-end: 3;
    height: 33vh;
    border: 2px solid teal;
}
.register-form-input {
  margin-left: 2.5%;
  margin-top: 1%;
  width: 90%;

  border: 1px solid teal;
  padding: 2%;
}
.button-auth {
  max-width: 40%;
  min-width: 40%;
  align-self: flex-end;
  padding: 10px 15px;
  background: none;
  color: teal;
  border: 1px solid teal;
  margin: 2%;
  margin-left: 30%;
}
.input-error {
  color: red;
  margin-left: 2.5%;
  margin-top: 1%;
}

</style>