<template>
    <div class="notification is-dark">
        <button class="delete"></button>
        <p class="has-text-centered">{{ name }}</p>
    </div>
</template>
<script>
export default {
    props: {
        name: {
            type: String,
            required: true
        }
    }
}
</script>