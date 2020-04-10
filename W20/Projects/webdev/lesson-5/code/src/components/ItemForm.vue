<template>
    <div class="container">
        <div class="tile is-ancestor">
            <div class="tile is-parent">
                <article class="tile is-child">
                    <div class="columns">
                        <form class="column" :class="{'is-one-quarter is-offset-5': !isModal}">
                            <h5 class="title has-text-centered is-unselectable">{{ title }}</h5>
                            <div class="field">
                                <div class="control">
                                    <input
                                        class="input"
                                        type="text"
                                        placeholder="Name"
                                        autoComplete="false"
                                        v-model="name.value"
                                        @blur="checkValidness('name')"
                                    />
                                </div>
                                <span v-if="!name.pristine">
                                    <p v-if="!name.value" class="help is-danger">
                                    name is required</p>
                                </span>
                            </div>
                            <div class="field">
                                <div class="select">
                                    <select
                                        v-model="type.value"
                                        @change="checkValidness('type')">
                                        <option value="" disabled selected>
                                        Select your option</option>
                                        <option 
                                        v-for="(type, index) in types" 
                                        :key="index">{{ type }}</option>
                                    </select>
                                </div>
                                <span v-if="!type.pristine">
                                    <p v-if="!type.value" class="help is-danger">
                                    type is required</p>
                                </span>
                            </div>
                            <div class="field has-text-centered" v-if="!isNew">
                                <label class="checkbox">
                                    <input type="checkbox" v-model="completed"/> 
                                    Completed
                                </label>
                            </div>
                            <br/>
                            <div class="field">
                                <div class="control buttons is-centered">
                                    <button type="submit" class="button is-success">
                                    Submit</button>
                                    <button type="submit" class="button is-dark">
                                    Cancel</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </article>
            </div>
        </div>
    </div>
</template>
<script>
import { ItemRuleSet, types } from './../rulesets/ItemRuleset'
export default {
    data: function () {
        return {
            name: {
                value: '',
                pristine: true,
                valid: true
            },
            type: {
                value: '',
                pristine: true,
                valid: true
            },
            completed: false,
            types: types
        }
    },
    props: {
        item: Object,
        title: String,
        isNew: Boolean,
        isModal: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        checkValidness(field) {
            const value = this[field].value
            const ruleset = ItemRuleSet({ [field]: value })

            this[field] = {
                valid: ruleset[field].valid,
                pristine: false,
                value: value
            }
        }
    }
}
</script>
<style lang="css">
    .select select:not([multiple]) {
        width: 100%
    }
    .select:not(.is-multiple) {
        width: 100%
    }
</style>