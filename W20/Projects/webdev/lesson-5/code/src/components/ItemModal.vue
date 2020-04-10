<template>
    <section class="section" v-if="item != null && active">
        <div class="modal is-active">
            <div class="modal-background"></div>
            <div class="modal-content">
                <article class="message">
                    <div class="message-header">
                        <p>Edit Item</p>
                        <button class="delete" aria-label="delete"></button>
                    </div>
                    <div class="message-body has-text-centered">
                        <ItemForm
                            :item="item"
                            :isModal="true"
                        />
                    </div>
                </article>
            </div>
        </div>
    </section>
</template>
<script>
import ItemForm from './ItemForm'
export default {
    props: {
        item: Object,
        active: {
            type: Boolean,
            required: true
        }
    },
    components: {
        ItemForm
    }
}
</script>