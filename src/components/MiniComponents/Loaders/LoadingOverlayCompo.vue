<!-- SpinnerOverlay.vue -->

<template>
  <v-overlay color="rgb(5, 19, 97, 0.19)">
    <v-container fill-height fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" md="6" class="text-center">
          <v-progress-circular
            indeterminate
            color="primary"
            size="90"
            :width="8"
          ></v-progress-circular>
          <v-divider class="my-4"></v-divider>
          <div class="caption font-weight-bold text-center">Chargement</div>
        </v-col>
      </v-row>
    </v-container>
  </v-overlay>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style scoped>
.caption {
  color: rgb(red, rgb(173, 173, 173), blue);
  font-size: 19px;
}

/* Add any additional styles as needed */
</style>
