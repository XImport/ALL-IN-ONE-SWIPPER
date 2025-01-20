<template>
  <v-card elevation="0" class="rounded-lg transition-transform">
    <v-card-text class="pa-4">
      <!-- Product Header -->
      <div class="d-flex align-center mb-1 bg-grey-lighten-4">
        <div class="flex-grow-1">
          <div
            class="text-subtitle-2 font-weight-bold text-truncate text-decoration-underline pa-2 text-center"
          >
            {{ product.productname }}
          </div>
        </div>
      </div>

      <!-- Product Details -->
      <v-row class="">
        <v-col cols="12">
          <div class="d-flex align-center pa-2 rounded bg-grey-lighten-4">
            <v-icon size="20" color="primary" class="mr-2"> mdi-cash </v-icon>
            <div style="margin-left: 30%">
              <div class="text-caption text-grey-darken-1">Prix</div>
              <div class="text-subtitle-2 font-weight-bold">
                {{ product.price }}
              </div>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: ["product"],
};
</script>

<style></style>
