<template>
  <div>
    <AppHeaderBar
      :DATA="DATA"
      :FetchQuery="FetchQuery"
      :StaticInfo="{ icon: 'mdi-poll', title: 'Évaluation Client' }"
      :GoButton="true"
    />
  </div>

  <!-- Toggle Drawer Button -->
  <div
    style="position: fixed; top: 300px; left: 0%; z-index: 5 !important"
    v-show="!isDrawerOpen"
  >
    <v-btn
      icon="mdi-arrow-collapse-right"
      elevation="3"
      @click="ChangeDrawerState"
      size="x-large"
    ></v-btn>
  </div>
  <div
    style="position: fixed; top: 300px; left: 15%; z-index: 5 !important"
    v-show="isDrawerOpen"
  >
    <v-btn
      icon="mdi-arrow-collapse-left"
      elevation="3"
      @click="ChangeDrawerState"
      size="x-large"
    ></v-btn>
  </div>

  <!-- Content Area -->
  <div
    :class="{
      'content-with-drawer': isDrawerOpen,
      'content-full-width': !isDrawerOpen,
    }"
    style="margin-top: 4% !important"
  >
    <v-container>
      <!-- PrimeVue MultiSelect for country selection -->
      <MultiSelect
        v-model="selectedClients"
        :options="Clients"
        optionLabel="CLIENTNAME"
        placeholder="Choisissez le nom du client ou des clients"
        filter
        :maxSelectedLabels="3"
        class="w-full md:w-56 mb-4"
        style="max-width: 100%; min-width: 21% !important; margin-left: 23%"
      >
        <template #option="slotProps">
          <div class="flex align-items-center">
            <div>{{ slotProps.option.CLIENTNAME }}</div>
          </div>
        </template>
      </MultiSelect>
    </v-container>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import AppHeaderBar from "../components/GlobalComponents/AppHeaderBar.vue";
import MultiSelect from "primevue/multiselect";
import Chip from "primevue/chip";
import axiosInstance from "../Axios";

export default defineComponent({
  name: "AnalyseClientView",
  components: {
    AppHeaderBar,
    MultiSelect,
    Chip,
  },
  data() {
    return {
      DATA: {
        DébutDate: "",
        FinDate: "",
      },
      selectedClients: [],
      Clients: [{ CLIENTNAME: "New York", CODE: "NY" }],
    };
  },
  created() {
    axiosInstance.get("/API/V1/QueryClients").then((response) => {
      this.Clients.map(() => {});
      this.Clients = response.data.INFO_CLIENTS;
    });
  },
  methods: {
    async FetchQuery(DATA) {
      console.log("Selected Clients:", this.selectedClients);

      try {
        let Clients = [];
        this.selectedClients.map((client) => {
          Clients.push(client.CLIENTNAME);
        });
        let Payload = { ...DATA, Clients: Clients }; // ✅ Correct payload structure
        console.log(Payload);
        const response = await axiosInstance.post(
          "/API/V1/AnalyseClient",
          Payload,
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        // Store the response data in Vuex
        this.$store.commit("ChangeQuerysData", DATA);

        console.log("API Response:", response.data);
      } catch (error) {
        console.error("Error fetching client analysis:", error);
      }
    },

    ChangeDrawerState() {
      this.$store.commit("ChangeDrawerState");
    },
    removeCountry(country) {
      this.selectedClients = this.selectedClients.filter(
        (item) => item.code !== country.code
      );
    },
  },
  computed: {
    isDrawerOpen() {
      return this.$store.getters.GetDrawerState;
    },
  },
});
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

/* Add some PrimeVue styling overrides if needed */
:deep(.p-multiselect-token) {
  margin-right: 0.5rem;
}

:deep(.p-multiselect) {
  min-width: 15rem;
}
</style>
