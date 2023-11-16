<template>
  <div class="task-complete-button">
          <img             
            src="@/assets/images/Checkmark.png" 
            width="30" 
            height="30"
            @click="$emit('task-complete', id)" 
          >
        </div>
        <div class="task-cancel-button">
          <img             
            src="@/assets/images/Cancel.png" 
            width="30" 
            height="30"
            @click="$emit('task-delete', id)" 
          >
        </div>
        <div class="task-star-button">
          <img             
            src="@/assets/images/redact.png" 
            width="30" 
            height="30"
            @click="$emit('task-change-important-status', id)" 
          >
        </div>
</template>
<script>
export default {
  props: {
    id: {
      type: Number,
      required: true
    }
  },

  emits: ['task-complete','task-delete','task-change-important-status'],
  computed: {

  },
  methods: {

  },

}
</script>
<style>

</style>