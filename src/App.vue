<template>
  <v-app>
    <router-view></router-view>
    <v-main class="bg-grey-lighten-4">
      <div>
        <!-- Content Goes Here  -->
        <NavigationDrawer />
      </div>
    </v-main>
  </v-app>
</template>

<script>
import NavigationDrawer from "./components/GlobalComponents/NavigationDrawer.vue";
export default {
  name: "App",
  components: { NavigationDrawer },
  data() {
    return {
      // your data here
    };
  },
};
</script>
