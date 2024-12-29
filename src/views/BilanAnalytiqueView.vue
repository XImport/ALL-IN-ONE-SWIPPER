<template>
  <div>
    <AppHeaderBar />

    <!-- Cards container -->
    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="(Frow, index) in FirstRowCard"
          :key="index"
          cols="12"
          sm="3"
          md="2"
          class="pa-2"
        >
          <InfoCard
            :Title="Frow.Title"
            :TextNumber="Frow.TextNumber"
            :Icon="Frow.Icon"
            :IconColor="Frow.IconColor"
          />
        </v-col>
      </v-row>
    </v-container>

    <v-container fluid style="max-width: 60%; margin-left: 25% !important">
      <v-row dense>
        <v-col
          v-for="(Srow, index) in SecondRowCard"
          :key="index"
          cols="12"
          sm="3"
          class="pa-2 mx-auto"
        >
          <InfoCard
            :Title="Srow.Title"
            :TextNumber="Srow.TextNumber"
            :Icon="Srow.Icon"
            :IconColor="Srow.IconColor"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import AppHeaderBar from "../components/GlobalComponents/AppHeaderBar.vue";
import InfoCard from "../components/MiniComponents/InfoCard.vue";

export default {
  name: "BilanAnalytique",
  components: { AppHeaderBar, InfoCard },
  data() {
    return {
      FirstRowCard: [
        {
          Title: "CA Brut",
          TextNumber: 2765879.32,
          IconColor: "deep-purple-darken-4",
          Icon: "mdi-finance", // Changed to a more relevant finance icon
        },
        {
          Title: "CA Net",
          TextNumber: 2547981.32,
          IconColor: "indigo-darken-4",
          Icon: "mdi-chart-bar", // Changed to a relevant net cash flow icon
        },
        {
          Title: "PMV Global",
          IconColor: "lime-darken-4",
          TextNumber: 36.35,
          Icon: "mdi-circle-multiple", // Used a globe icon for global scope
        },
        {
          Title: "PMV Hors Stérile",
          IconColor: "orange-darken-4",
          TextNumber: 43.25,
          Icon: "mdi-circle-multiple", // Icon to reflect something outside sterile conditions
        },
        {
          Title: "Marge Transport",
          IconColor: "yellow-accent-4",
          TextNumber: 25698,
          Icon: "mdi-truck", // Icon related to transport
        },
        {
          Title: "Quantité en T",
          IconColor: "blue-grey-darken-4",
          TextNumber: 64589.32,
          Icon: "mdi-weight", // Icon for quantity or weight
        },
      ],
      SecondRowCard: [
        {
          Title: "Mix Produit",
          IconColor: "green-accent-4",
          TextNumber: "76.32%",
          Percentange: true,
          Icon: "mdi-pound", // Changed to a more relevant finance icon
        },
        {
          Title: "N.Voyages R.Livré",
          IconColor: "green-darken-4",
          TextNumber: "45 Voyages",
          Icon: "mdi-train-car", // Changed to a relevant net cash flow icon
        },
        {
          Title: "Caisse Espèces",
          IconColor: "light-blue-darken-4",
          TextNumber: 458356.32,
          Icon: "mdi-cash", // Used a globe icon for global scope
        },
        {
          Title: "Recouv Effecteé",
          IconColor: "cyan-darken-4",
          TextNumber: 1798254.36,
          Icon: "mdi-signal", // Icon to reflect something outside sterile conditions
        },
      ],
    };
  },
};
</script>

<style scoped>
.v-container {
  margin-left: var(--v-navigation-drawer-width, 256px) !important;
  width: calc(100% - var(--v-navigation-drawer-width, 256px)) !important;
  transition: margin-left 0.2s ease, width 0.2s ease;
}

@media (max-width: 1264px) {
  .v-container {
    margin-left: 0 !important;
    width: 100% !important;
  }
}
</style>
