<template>
  <v-app>
    <router-view></router-view>
    <v-main class="bg-grey-lighten-4">
      <div>
        <!-- Content Goes Here  -->
        <NavigationDrawer v-if="Drawer" />
        <div>
        <DialogBox />
      </div>
      </div>
    </v-main>
  </v-app>
</template>

<script>
import NavigationDrawer from "./components/GlobalComponents/NavigationDrawer.vue";
import DialogBox from "./components/MiniComponents/DialogBox.vue";
export default {
  name: "App",
  components: { NavigationDrawer,DialogBox },
  data() {
    return {
      // your data here
    };
  },
  computed: {
    Drawer() {
      return this.$store.getters.GetDrawerState;
    },
  },
};
</script>
