<template>
  <div class="login">
    <div class="login-form">
      <div class="page-name">
        <h1>Авторизация</h1>
      </div>
      <h3 v-show="this.errorAuthentification" class="error-authentification">
        Неверный email или пароль
      </h3>
      <ValidationForm @submit="auth">
        <Field v-model="email" name="email" class="login-form-input" type="email" placeholder="Введите ваш email" />
        <Field v-model="password" name="password" class="login-form-input" type="password"
          placeholder="Введите ваш пароль" />
        <button class="button-auth">Войти</button>
      </ValidationForm>
      <div class="register-container">
        <router-link to="/register" class="register-link">
          Зарегистрироваться
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import { Field, Form as ValidationForm, ErrorMessage } from 'vee-validate'

export default {
  components: {
    ValidationForm,
    Field,
    ErrorMessage,
  },
  created() {

  },
  data() {
    return {
      email: "",
      password: "",
      errorAuthentification: false
    }
  },
  methods: {
    auth() {
      const requestBody = { "email": this.email, "password": this.password }
      axios.post("http://tasks.localhost.com/api/login", requestBody)
        .then(() => this.$router.push("/tasks"))
        .catch(() => this.errorAuthentification = true)
    }
  }
}
</script>
  
<style>
.login {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
}

.login-form {

  grid-column-start: 2;
  grid-column-end: 3;
  grid-row-start: 2;
  grid-row-end: 3;
  height: 33vh;
  border: 2px solid teal;
}

.login-form-input {
  margin: 2%;
  margin-top: 2%;
  width: 91%;

  border: 1px solid teal;
  padding: 2% 2%;
}

.button-auth {
  max-width: 25%;
  min-width: 25%;
  padding: 10px 15px;
  background: none;
  color: teal;
  border: 1px solid teal;
  margin: 1%;
}
.register-link{
  color: teal;
}
.register-container{
  max-width: 50%;
  min-width: 50%;
  margin-left: 25%;
  word-wrap: break-word;
  text-align: center;
}
.page-name{
  text-align: center;
}
.error-authentification {
  color: red

}
</style>