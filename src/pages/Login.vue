<template>
    <div class="login">
      <div class="login-form">
        <div>
        <h1>Авторизация</h1>
        <ValidationForm 
        @submit="auth"
        >
        <Field 
          v-model="email"
          name="email" 
          class="login-form-input" 
          type="email"
          placeholder="Введите ваш email" 
        />
        <Field 
          v-model="password"
          name="password" 
          class="login-form-input" 
          type="password"
          placeholder="Введите ваш пароль" 
        />
        <button class="button-auth">Войти</button>
        </ValidationForm>
        </div>
      </div>
    </div>
</template>
<script>
import { Field, Form as ValidationForm, ErrorMessage } from 'vee-validate'
export default{
    components: {
    ValidationForm,
    Field,
    ErrorMessage
  },
    data(){
        return{
            login:"",
            password:""
        }
    },
    methods:{
        auth(){
            const requestBody = {"email":this.email, "password":this.password}
            fetch("https://mytasks-8rct.onrender.com//auth",{
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify(requestBody)})
                .then(response => response.json())
                .then(response => console.log(JSON.stringify(response)))
        }
    }
}
</script>
  
<style>
.login{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
}
.login-form{
    grid-column-start: 2;
    grid-column-end: 3;
    grid-row-start: 2;
    grid-row-end: 3;
    height: 33vh;
    border: 2px solid teal;
}
.login-form-input {
  margin: 2.5%;
  margin-top: 10%;
  width: 90%;

  border: 1px solid teal;
  padding: 2% 2%;
}
.button-auth {
  width: 20%;
  align-self: flex-end;
  padding: 10px 15px;
  background: none;
  color: teal;
  border: 1px solid teal;
  margin: 1%;
  margin-left: 75%;
}

</style>