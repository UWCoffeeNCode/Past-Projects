<template>
    <div class="content-section">
        <section>
            <div class="hero is-dark is-medium">
                <div class="hero-body">
                    <div class="container" >
                        <h1 class="title has-text-centered is-unselectable">
                        Welcome!
                        </h1>
                        <h1 class="subtitle has-text-centered is-unselectable">
                        Your Dashboard
                        </h1>
                    </div>
                </div>
            </div>
            <div class="tabs is-centered">
                <ul v-if="types">
                    <li v-for="(type, index) in types"
                        :key="index"
                        :class="{ 'is-active' : selectedType === index }"
                        @click="pickType(index)">
                        <a>{{ type }}</a>
                    </li>
                </ul>
            </div>
            <div class="tabs is-small is-toggle is-centered has-text-centered">
                <ul v-if="filters">
                    <li v-for="(filter, index) in filters"
                        :key="index"
                        :class="{ 'is-active' : selectedFilter === index }"
                        @click="pickFilter(index)">
                        <a>{{ filter }}</a>
                    </li>
                </ul>
            </div>
        </section>
        <section class="section" v-if="items.length > 0">
            <Item
                v-for="(item, index) in items"
                :name="item.name"
                :key="index" />
        </section>
        <section class="section" v-else>
            <div class="notification is-white">
                <p class="has-text-centered is-unselectable">
                No Items to Show
                </p>
            </div>
        </section>
        <DeleteModal
            :active="activeDeleteModal"
            :item="selectedItem"/>
        <ItemModal
            :active="activeItemModal"
            :item="selectedItem"/>
    </div>
</template>
<script>
import ItemModal from './ItemModal'
import DeleteModal from './DeleteModal'
import { types, filters } from './../rulesets/ItemRuleset'
import Item from './Item'

export default {
    data: function () {
        return {
            items: [{
                name: 'spider-man',
                type: 'Movies',
                completed: true
            }, {
                name: 'stranger things',
                type: 'TV Shows',
                completed: false
            }],
            types: types,
            filters: filters,
            selectedType: 0,
            selectedFilter: 0
            
        }
    },
    methods: {
        pickType (index) {
            this.selectedType = index
        },
        pickFilter (index) {
            this.selectedFilter = index
        }
    },
    components: {
        DeleteModal,
        ItemModal,
        Item
    }
}
</script>