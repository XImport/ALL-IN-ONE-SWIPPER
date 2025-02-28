<template>
    <div>
        <AppHeaderBar :DATA="DATA" :FetchQuery="FetchQuery"
            :StaticInfo="{ icon: 'mdi-poll', title: 'Évaluation Client' }" />
    </div>
    <div style="position: fixed; top: 300px; left: 0%; z-index: 5 !important" v-show="!isDrawerOpen">
        <v-btn icon="mdi-arrow-collapse-right" elevation="3" @click="ChangeDrawerState()" size="x-large"></v-btn>
    </div>
    <div style="position: fixed; top: 300px; left: 15%; z-index: 5 !important" v-show="isDrawerOpen">
        <v-btn icon="mdi-arrow-collapse-left" elevation="3" @click="ChangeDrawerState()" size="x-large"></v-btn>
    </div>

    <div :class="{
        'content-with-drawer': isDrawerOpen,
        'content-full-width': !isDrawerOpen,
    }" style="margin-top: 4% !important;">
        <v-container style="max-width: 37%;margin-left: 30.5%">
            <v-select v-if="!isDrawerOpen" v-model="favorites" style="height: 2% !important;" :items="states"
                variant="outlined" hint="Analysez le client que vous voulez."
                label="Choisissez le nom du client ou des clients." multiple persistent-hint></v-select>
        </v-container>
        <v-container style="max-width: 32.5%;margin-left: 24.4%;margin-top: -2%;">
            <v-select v-if="isDrawerOpen" v-model="favorites" style=" height: 80% !important;
    justify-content: center !important;
    align-items: center !important;
    align-content: center !important;" :items="states" hint="Analysez le client que vous voulez."
                label="Choisissez le nom du client ou des clients. " multiple variant="outlined"
                persistent-hint></v-select>
        </v-container>





    </div>
</template>

<script>
import AppHeaderBar from '../components/GlobalComponents/AppHeaderBar.vue';
export default {
    components: { AppHeaderBar },
    data() {
        return {
            DATA: {
                DébutDate: "",
                FinDate: "",
            },
            favorites: [],
            states: [


            ],
        }
    },
    methods: {
        FetchQuery() {
            console.log("hello world")
        },
        ChangeDrawerState() {
            this.$store.commit("ChangeDrawerState");
        },
    },
    computed: {
        isDrawerOpen() {
            return this.$store.getters.GetDrawerState; // Assuming you store drawer state in Vuex
        },
    }
}
</script>

<style scoped>
.content-with-drawer {
    margin-left: 15% !important;
    width: calc(100% - 280px) !important;
    transition: margin-left 0.3s ease, width 0.3s ease;
}

.content-full-width {
    margin-left: 0;
    margin: auto;
    width: 95%;
    transition: margin-left 0.3s ease, width 0.3s ease;
}

.v-field__input,
.v-select .v-field.v-field {
    cursor: pointer !important;
    height: 80% !important;
    justify-content: center !important;
    align-items: center !important;
    align-content: center !important;
}
</style>