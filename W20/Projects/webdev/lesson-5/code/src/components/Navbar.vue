<template>
    <nav class="navbar is-transparent">
        <div class="navbar-brand">
            <div class="navbar-burger burger"
                :class="{'is-active':activeNavbar}"
                @click="toggleStatus">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
        <div class="navbar-menu"
            :class="{'is-active':activeNavbar}"
            @click="toggleStatus">
            <div class="navbar-start has-dropdown">
                <router-link v-for="(option, index) in options" :key="index" class="navbar-item is-unselectable"
                   :to="urls[index]"
                    @click="toggleActiveItem(index)">{{ option }}</router-link>
            </div>
        </div>
    </nav>
</template>
<script>
export default {
    data: function() {
        return {
            options: ['Home', 'Dashboard', 'Add an Item'],
            urls: ['/', '/dashboard', 'add-item'],
            activeNavbar: false,
            itemIndex: 0
        }
    },
    methods: {
        toggleStatus: function() {
            this.activeNavbar = !this.activeNavbar
        },
        toggleActiveItem: function(index) {
            this.itemIndex = index
        }
    }
}
</script>