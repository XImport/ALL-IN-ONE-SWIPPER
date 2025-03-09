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
    <v-container v-if="isDrawerOpen">
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
    <v-container v-if="!isDrawerOpen">
      <!-- PrimeVue MultiSelect for country selection -->
      <MultiSelect
        v-model="selectedClients"
        :options="Clients"
        optionLabel="CLIENTNAME"
        placeholder="Choisissez le nom du client ou des clients"
        filter
        :maxSelectedLabels="3"
        class="w-full md:w-56 mb-4"
        style="max-width: 100%; min-width: 21% !important; margin-left: 34%"
      >
        <template #option="slotProps">
          <div class="flex align-items-center">
            <div>{{ slotProps.option.CLIENTNAME }}</div>
          </div>
        </template>
      </MultiSelect>
    </v-container>
    <div v-if="isLoadingContent">
      <v-container>
        <h2
          class="text-center text-decoration-underline"
          style="margin-top: -2%"
        >
          <span class="text-red"> Partie 1 : </span>

          <span
            >Analyse Commerciale (
            <span class="text-pink">
              Ventes, Produits, Prix, Volume, Prix Client,Marge bénéficiaire
              ...</span
            >)</span
          >
        </h2>
      </v-container>
      <v-container style="max-width: 90%">
        <v-row no-gutters>
          <v-col cols="12" sm="6">
            <LineChartJS
              :CHARTDATA="CANETCABRUT"
              title="Progression du Chiffre d'Affaires Brut et Net "
              IconName="mdi-chart-ppf"
              IconColor="blue"
              :Min="200000"
              :Max="400000"
              :chartHeight="350"
            />
          </v-col>
          <v-col cols="12" sm="6">
            <BarCHART
              :CHARTDATA="QNTENTANDM3"
              title="Quantité Vendue : Tonnes et Mètres Cubes"
              IconName="mdi-chart-tree"
              IconColor="green"
              UNITE="du Volume Global"
            />
          </v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="12" sm="6">
            <BarCHART
              :CHARTDATA="PMVGLOBALS"
              title="Analyse du PVM : Nobles, Graves et Stérile "
              IconName="mdi-chart-ppf"
              IconColor="blue"
              UNITE="dhs/Tonne"
            />
          </v-col>
          <v-col cols="12" sm="6">
            <BarCHART
              :CHARTDATA="PRODUCTS_SOLD"
              title="Répartition du Volume de Vente par Produits"
              IconName="mdi-chart-tree"
              IconColor="green"
              UNITE="Tonne du Volume Global"
            />
          </v-col>
        </v-row>

        <v-row no-gutters>
          <v-col cols="12" sm="6">
            <BarCHART
              :CHARTDATA="PRODUCTS_MARGIN"
              title="Distribution des Coûts et Prix de Vente selon les Produits (dhs) "
              IconName="mdi-chart-ppf"
              IconColor="blue"
              UNITE="dhs"
            />
          </v-col>
          <v-col cols="12" sm="6">
            <div>
              <BarCHART
                :CHARTDATA="PRODUCTS_MARGIN_POURCENTANGE"
                title="Marge Bénéficiaire : Distribution en Pourcentage par Produit (%)"
                IconName="mdi-chart-pie"
                IconColor="orange"
                UNITE="%"
              />
            </div>
          </v-col>
        </v-row>

        <v-row no-gutters style="margin-top: 0%; margin-left: 10%">
          <v-col cols="12" sm="6">
            <DonutsChartJS
              :CHARTDATA="VOLPARPRODUIT"
              title="État des Ventes par Produit en Tonnes (Par Date)"
              IconName="mdi-chart-pie"
              IconColor="orange"
            />
          </v-col>
          <v-col cols="12" sm="6">
            <DonutsChartJS
              :CHARTDATA="CAPARPRODUIT"
              title="État des Ventes par Produit en CA NET (Par Date)"
              IconName="mdi-chart-pie"
              IconColor="orange"
            />
          </v-col>
        </v-row>
      </v-container>
      <v-container>
        <h2
          class="text-center text-decoration-underline"
          style="margin-top: -2%"
        >
          <span class="text-red"> Partie 2 : </span>

          <span
            >Analyse Paiement (
            <span class="text-pink">
              Délai de Paiement, Créances Clients, Recouvrement Effectuer... </span
            >)</span
          >
        </h2>
      </v-container>
      <v-container style="max-width: 95%">
        <v-row no-gutters>
          <v-col cols="12" sm="6">
            <LineChartJS
              :CHARTDATA="DELAI_PAIEMENT_VS_RECOUVREMENT"
              title="Délai de Paiement vs Date de Recouvrement "
              IconName="mdi-chart-ppf"
              IconColor="blue"
              :Min="120"
              :Max="30"
              :chartHeight="370"
              Unite="Jours"
            />
          </v-col>
          <v-col cols="12" sm="6">
            <BarCHART
              :CHARTDATA="CREANCE_CA"
              title="Évolution des Créances Clients et du Chiffre d'Affaires Brut "
              IconName="mdi-chart-tree"
              IconColor="green"
            />
          </v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="12" sm="6">
            <LineChartJS
              :CHARTDATA="DSO_CLIENTS"
              title="DSO CLIENTS"
              IconName="mdi-chart-ppf"
              IconColor="blue"
              :Min="120"
              :Max="CLIENT_PAYEMENT_DELAIY"
              :chartHeight="370"
              :chartWidth="472"
              Unite="Jours"
            />
          </v-col>
          <v-col cols="12" sm="6">
            <div style="margin-left: 20%">
              <DonutsChartJS
                :CHARTDATA="REPARTITION_MODES_PAYEMENTS"
                title="État des Ventes par Produit en CA NET (Par Date)"
                IconName="mdi-chart-pie"
                IconColor="orange"
                :chartHeight="370"
                :chartWidth="172"
              />
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import AppHeaderBar from "../components/GlobalComponents/AppHeaderBar.vue";
import MultiSelect from "primevue/multiselect";
import Chip from "primevue/chip";
import axiosInstance from "../Axios";
import BarCHART from "../components/MiniComponents/Charts/BarChartJS.vue";
import LineChartJS from "../components/MiniComponents/Charts/LineChartJS.vue";
import DonutsChartJS from "../components/MiniComponents/Charts/DonutsChartJS.vue";
export default defineComponent({
  name: "AnalyseClientView",
  components: {
    AppHeaderBar,
    MultiSelect,
    Chip,
    BarCHART,
    LineChartJS,
    DonutsChartJS,
  },
  data() {
    return {
      CLIENT_PAYEMENT_DELAIY: 0,
      isLoadingContent: false,
      DATA: {
        DébutDate: "",
        FinDate: "",
      },
      selectedClients: [],
      Clients: [{ CLIENTNAME: "New York", CODE: "NY" }],

      DSO_CLIENTS: {
        labels: [
          "Janvier",
          "Février",
          "Mars",
          "Avril",
          "Mai",
          "Juin",
          "Juillet",
        ],
        datasets: [
          {
            label: "DSO Clients",
            data: [10, 20, 30, 40, 50, 60, 70],
            backgroundColor: "#0c38a5",
            borderColor: "#0c38a5",
          },
        ],
      },
      REPARTITION_MODES_PAYEMENTS: {
        labels: ["ESPECE", "VIRMENT", "EFFET", "COMP", "CHEQ"],
        datasets: [
          {
            label: "Repartition des modes de paiement",
            data: [100],
            backgroundColor: ["#1f77b4"], // Blue
            borderColor: "#1f77b4",
          },
          {
            label: "Repartition des modes de paiement",
            data: [100],
            backgroundColor: ["#f50750"], // RED
            borderColor: "#f50750",
          },
          {
            label: "Repartition des modes de paiement",
            data: [100],
            backgroundColor: ["#ff7f0e"], // ORANGE
            borderColor: "#ff7f0e",
          },
          {
            label: "Repartition des modes de paiement",
            data: [100],
            backgroundColor: ["#FFFF00"], // YELLOW
            borderColor: "#FFFF00",
          },
          {
            label: "Repartition des modes de paiement",
            data: [100],
            backgroundColor: ["#FF00FF"], // MAGENTA
            borderColor: "#FF00FF",
          },
          {
            label: "Repartition des modes de paiement",
            data: [100],
            backgroundColor: ["#00FFFF"], // CYAN
            borderColor: "#00FFFF",
          },
        ],
      },
      QNTENTANDM3: {
        labels: [
          "Janvier",
          "Février",
          "Mars",
          "Avril",
          "Mai",
          "Juin",
          "Juillet",
          "Août",
          "Septembre",
          "Octobre",
          "Novembre",
          "Décembre",
        ],
        datasets: [
          {
            label: "QUANTITE EN T",
            data: [
              102456.34, 524109.75, 738102.21, 652907.8, 274654.99, 765312.65,
              341852.47, 612743.03, 137983.51, 849226.29, 745819.14, 609478.68,
            ],
            backgroundColor: ["#08a06e"],
          },
          {
            label: "QUANTITE EN M3",
            data: [
              258714.56, 389563.82, 193458.9, 332874.71, 110736.44, 359128.25,
              249586.33, 174398.77, 367823.01, 103489.53, 268491.08, 394560.87,
            ],
            backgroundColor: ["#f50750"],
          },
        ],
      },
      DELAI_PAIEMENT_VS_RECOUVREMENT: {
        labels: [
          "Janvier",
          "Février",
          "Mars",
          "Avril",
          "Mai",
          "Juin",
          "Juillet",
          "Août",
          "Septembre",
          "Octobre",
          "Novembre",
          "Décembre",
        ],
        datasets: [
          {
            label: "Délai de Paiement Accordé (jours)",
            data: [60, 60, 60, 70, 90, 70, 100, 80, 80, 70, 60, 60],
            backgroundColor: ["#0c38a5"],
            borderColor: "#0c38a5",
          },
          {
            label: "Date de Recouvrement Effectué (jours)",
            data: [20, 35, 50, 25, 95, 30, 120, 60, 30, 45, 35, 0],
            backgroundColor: ["#eca90e"],
            borderColor: "#eca90e",
          },
        ],
      },

      CREANCE_CA: {
        labels: [
          "Janvier",
          "Février",
          "Mars",
          "Avril",
          "Mai",
          "Juin",
          "Juillet",
          "Août",
          "Septembre",
          "Octobre",
          "Novembre",
          "Décembre",
        ],
        datasets: [
          {
            label: "SOMME DU CREANCE CLIENT",
            data: [
              3277180.43, 2593602.01, 2949653.39, 1881976.92, 3184468.64,
              2236468.42, 2162396.08, 2933008.64, 2027596.52, 1617562.78,
              2427159.58, 2036549.39,
            ],
            backgroundColor: ["#0c38a5"],
            borderColor: "#0c38a5",
          },
          {
            label: "SOMME DU CA BRUT",
            data: [
              3177180.43, 2493602.01, 2849653.39, 1781976.92, 3084468.64,
              2136468.42, 2062396.08, 2833008.64, 1927596.52, 1517562.78,
              2327159.58, 1936549.39,
            ],
            backgroundColor: ["#eca90e"],
            borderColor: "#eca90e",
          },
        ],
      },

      CANETCABRUT: {
        labels: [
          "Janvier",
          "Février",
          "Mars",
          "Avril",
          "Mai",
          "Juin",
          "Juillet",
          "Août",
          "Septembre",
          "Octobre",
          "Novembre",
          "Décembre",
        ],
        datasets: [
          {
            label: "SOMME DU CA BRUT",
            data: [
              3277180.43, 2593602.01, 2949653.39, 1881976.92, 3184468.64,
              2236468.42, 2162396.08, 2933008.64, 2027596.52, 1617562.78,
              2427159.58, 2036549.39,
            ],
            backgroundColor: ["#0c38a5"],
            borderColor: "#0c38a5",
          },
          {
            label: "SOMME DU CA NET",
            data: [
              3177180.43, 2493602.01, 2849653.39, 1781976.92, 3084468.64,
              2136468.42, 2062396.08, 2833008.64, 1927596.52, 1517562.78,
              2327159.58, 1936549.39,
            ],
            backgroundColor: ["#eca90e"],
            borderColor: "#eca90e",
          },
        ],
      },
      PMVGLOBALS: {
        labels: [
          "Janvier",
          "Février",
          "Mars",
          "Avril",
          "Mai",
          "Juin",
          "Juillet",
          "Août",
          "Septembre",
          "Octobre",
          "Novembre",
          "Décembre",
        ],
        datasets: [
          {
            label: "PVM NOBLES",
            data: [
              41.05, 41.48, 41.91, 42.34, 42.77, 43.2, 43.63, 44.06, 44.02,
              43.8, 43.47, 44.32,
            ],
            backgroundColor: ["#008000"],
          },
          {
            label: "PVM GRAVES",
            data: [
              29.05, 29.39, 29.73, 30.07, 30.41, 30.75, 31.09, 31.43, 31.77,
              32.11, 32.45, 32.87,
            ],
            backgroundColor: ["#FFA500"],
          },
          {
            label: "PVM STERILE",
            data: [
              15.01, 15.05, 15.09, 15.13, 15.17, 15.21, 15.25, 15.29, 15.33,
              15.37, 15.41, 15.45,
            ],
            backgroundColor: ["#FF0000"],
          },
        ],
      },
      PRODUCTS_SOLD: {
        labels: [
          "Janvier",
          "Février",
          "Mars",
          "Avril",
          "Mai",
          "Juin",
          "Juillet",
          "Août",
          "Septembre",
          "Octobre",
          "Novembre",
          "Décembre",
        ],
        datasets: [
          {
            label: "FILTRE",
            data: [500, 520, 530, 510, 550, 570, 590, 600, 620, 640, 660, 680],
            backgroundColor: ["#1f77b4"], // Blue
          },
          {
            label: "GABION",
            data: [450, 460, 470, 455, 480, 490, 500, 510, 525, 530, 540, 550],
            backgroundColor: ["#ff7f0e"], // Orange
          },
          {
            label: "GRAIN DE RIZ",
            data: [300, 310, 320, 315, 330, 340, 350, 360, 375, 380, 390, 400],
            backgroundColor: ["#2ca02c"], // Green
          },
          {
            label: "GRAVETTE G1",
            data: [400, 420, 430, 410, 440, 450, 470, 480, 500, 510, 520, 530],
            backgroundColor: ["#d62728"], // Red
          },
          {
            label: "GRAVETTE G2",
            data: [350, 360, 370, 355, 380, 390, 400, 410, 425, 430, 440, 450],
            backgroundColor: ["#9467bd"], // Purple
          },
          {
            label: "SABLE CONCASSAGE 0-4",
            data: [600, 610, 620, 605, 630, 640, 650, 660, 675, 680, 690, 700],
            backgroundColor: ["#8c564b"], // Brown
          },
          {
            label: "SABLE CONCASSAGE 0-2",
            data: [550, 560, 570, 555, 580, 590, 600, 610, 625, 630, 640, 650],
            backgroundColor: ["#e377c2"], // Pink
          },
          {
            label: "TOUT VENANT 0-31.5",
            data: [700, 710, 720, 705, 730, 740, 750, 760, 775, 780, 790, 800],
            backgroundColor: ["#7f7f7f"], // Gray
          },
          {
            label: "TOUT VENANT 0-40",
            data: [650, 660, 670, 655, 680, 690, 700, 710, 725, 730, 740, 750],
            backgroundColor: ["#bcbd22"], // Yellow-Green
          },
          {
            label: "TOUT VENANT 0-60",
            data: [600, 610, 620, 605, 630, 640, 650, 660, 675, 680, 690, 700],
            backgroundColor: ["#17becf"], // Cyan
          },
          {
            label: "TOUT VENANT 0-100",
            data: [550, 560, 570, 555, 580, 590, 600, 610, 625, 630, 640, 650],
            backgroundColor: ["#ff9896"], // Light Red
          },
          {
            label: "STERILE",
            data: [500, 510, 520, 505, 530, 540, 550, 560, 575, 580, 590, 600],
            backgroundColor: ["#98df8a"], // Light Green
          },
          {
            label: "STERILE FIN",
            data: [450, 460, 470, 455, 480, 490, 500, 510, 525, 530, 540, 550],
            backgroundColor: ["#ffbb78"], // Light Orange
          },
        ],
      },
      CAPARPRODUIT: {
        labels: [
          "Grain de Riz",
          "Gravette G1",
          "Gravette G2",
          "Sable Concassage 0/4",
          "Sable Concassage 0/2",
          "Tout Venant",
          "Gabion",
          "Stérile",
          "Stérile Fin",
        ],
        datasets: [
          {
            label: "CA Net Par Produits",
            data: [2, 35, 15, 37, 2, 6, 0.5, 1, 0.5],
            backgroundColor: [
              "#41B883",
              "#E46651",
              "#00D8FF",
              "#DD1B16",

              "#12be65",
              "#ecc43d",
              "#c45db9",
              "#6aca65",
              "#f2c68a",
            ],
          },
        ],
      },
      VOLPARPRODUIT: {
        labels: [
          "Grain de Riz",
          "Gravette G1",
          "Gravette G2",
          "Sable Concassage 0/4",
          "Sable Concassage 0/2",
          "Tout Venant",
          "Gabion",
          "Stérile",
          "Stérile Fin",
        ],
        datasets: [
          {
            label: "Volume Par Produits",
            data: [2, 35, 15, 37, 2, 6, 0.5, 1, 0.5],
            backgroundColor: [
              "#41B883",
              "#E46651",
              "#00D8FF",
              "#DD1B16",

              "#12be65",
              "#ecc43d",
              "#c45db9",
              "#6aca65",
              "#f2c68a",
            ],
          },
        ],
      },
      PRODUCTS_MARGIN: {
        labels: [
          "FILTRE",
          "GABION",
          "GRAIN DE RIZ",
          "GRAVETTE G1",
          "GRAVETTE G2",
          "SABLE CONCASSAGE 0-4",
          "SABLE CONCASSAGE 0-2",
          "TOUT VENANT 0-31.5",
          "TOUT VENANT 0-40",
          "TOUT VENANT 0-60",
          "TOUT VENANT 0-100",
          "STERILE",
          "STERILE FIN",
        ],
        datasets: [
          {
            label: "Cout de Revient",
            data: [
              150, 120, 100, 130, 110, 140, 125, 150, 145, 130, 135, 120, 115,
            ],
            backgroundColor: [
              "#4C9FD6", // Sky Blue
              "#FF8F1F", // Warm Orange
              "#88D48A", // Light Green
              "#FF5C5C", // Soft Red
              "#9E5F95", // Purple
              "#F08C4F", // Burnt Orange
              "#D44B73", // Warm Pink
              "#A8D5BA", // Mint Green
              "#57A8D8", // Light Blue
              "#F9C74F", // Golden Yellow
              "#A8E0B1", // Pastel Green
              "#F1A7B7", // Light Coral
              "#F8D4B3", // Peach
            ],
            borderColor: [
              "#4C9FD6",
              "#FF8F1F",
              "#88D48A",
              "#FF5C5C",
              "#9E5F95",
              "#F08C4F",
              "#D44B73",
              "#A8D5BA",
              "#57A8D8",
              "#F9C74F",
              "#A8E0B1",
              "#F1A7B7",
              "#F8D4B3",
            ],
            borderWidth: 1,
          },
          {
            label: "Prix de Vente",
            data: [
              160, 170, 160, 167, 132, 170, 195, 240, 345, 180, 185, 170, 195,
            ],
            backgroundColor: [
              "#4A67F4", // Royal Blue
              "#FF5D00", // Vivid Orange
              "#5ED86A", // Bright Green
              "#D1366D", // Magenta Red
              "#7D4FC2", // Deep Purple
              "#FF7262", // Light Red
              "#F7B400", // Sun Yellow
              "#16B8A7", // Teal
              "#B3E0A8", // Light Mint Green
              "#F03F7D", // Hot Pink
              "#B6E0FF", // Light Sky Blue
              "#FF6F32", // Coral Orange
              "#9FFF80", // Bright Lime Green
            ],
            borderColor: [
              "#4A67F4",
              "#FF5D00",
              "#5ED86A",
              "#D1366D",
              "#7D4FC2",
              "#FF7262",
              "#F7B400",
              "#16B8A7",
              "#B3E0A8",
              "#F03F7D",
              "#B6E0FF",
              "#FF6F32",
              "#9FFF80",
            ],
            borderWidth: 1,
          },
        ],
      },

      PRODUCTS_MARGIN_POURCENTANGE: {
        labels: [
          "FILTRE",
          "GABION",
          "GRAIN DE RIZ",
          "GRAVETTE G1",
          "GRAVETTE G2",
          "SABLE CONCASSAGE 0-4",
          "SABLE CONCASSAGE 0-2",
          "TOUT VENANT 0-31.5",
          "TOUT VENANT 0-40",
          "TOUT VENANT 0-60",
          "TOUT VENANT 0-100",
          "STERILE",
          "STERILE FIN",
        ],
        datasets: [
          {
            label: "Marge Bénéficiaire En %",
            data: [2, 35, 15, 37, 2, 6, 0.5, 1, 0.5, 1, 4, 5, 7],
            backgroundColor: [
              "#6E9F2E", // Forest Green
              "#F25D27", // Burnt Orange
              "#1E9B9B", // Teal
              "#D93A3A", // Crimson Red
              "#66BB6A", // Green
              "#F5C14C", // Soft Yellow
              "#8B6BBE", // Lavender Purple
              "#71A149", // Olive Green
              "#FFEC63", // Soft Yellow
              "#FFC107", // Amber
              "#7366BD", // Purple Blue
              "#FF5733", // Coral
              "#4CAF50", // Bright Green
            ],
          },
        ],
      },
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
        // this.CLIENT_PAYEMENT_DELAIY = response.data.DSO_clients.client_payement_delaiy;
        this.$store.commit("ChangeQuerysData", DATA);
        this.CLIENT_PAYEMENT_DELAIY =
          response.data.DSO_clients.client_payement_delaiy[0];
        const CA = {
          labels: [...response.data.CAGRAPH.GRAPHCADATESS],
          datasets: [
            {
              label: "SOMME DU CA BRUT",
              data: [...response.data.CAGRAPH.GRAPHCABRUT],
              backgroundColor: ["#0c38a5"],
              borderColor: "#0c38a5",
            },

            {
              label: "SOMME DU CA NET",
              data: [...response.data.CAGRAPH.GRAPHCANET],
              backgroundColor: ["#eca90e"],
              borderColor: "#eca90e",
            },
          ],
        };
        const QNT = {
          labels: [...response.data.VOLGRAPH.GRAPHVOLDATES],
          datasets: [
            {
              label: "QUANTITE EN T",
              data: [...response.data.VOLGRAPH.GRAPHVOLQNTENT],
              backgroundColor: ["#08a06e"],
            },
            {
              label: "QUANTITE EN M3",
              data: [...response.data.VOLGRAPH.GRAPHVOLQNTENM3],
              backgroundColor: ["#f50750"],
            },
          ],
        };
        const PMV = {
          labels: [...response.data.PMVGRAPH.PMVDATES],
          datasets: [
            {
              label: "PVM NOBLES",
              data: [...response.data.PMVGRAPH.PMVNOBLES],
              backgroundColor: ["#008000"],
            },
            {
              label: "PVM GRAVES",
              data: [...response.data.PMVGRAPH.PMVGRAVES],
              backgroundColor: ["#FFA500"],
            },
            {
              label: "PVM STERILE",
              data: [...response.data.PMVGRAPH.PMVSTERILE],
              backgroundColor: ["#FF0000"],
            },
          ],
        };
        const VOLUMEBYPRODUCTS = {
          labels: response.data.VOLUMEDATABYPRODUCTSBYDATES.PRODUITS, // Use product names as labels
          datasets: [
            {
              label: "Quantité",
              data: response.data.VOLUMEDATABYPRODUCTSBYDATES.QNTBYPRODUIT,
              backgroundColor: ["#ff6384", "#36a2eb", "#ffce56"],
            },
            {
              label: "CA NET",
              data: response.data.VOLUMEDATABYPRODUCTSBYDATES.CANETBYPRODUIT,
              backgroundColor: ["#ff6384", "#36a2eb", "#ffce56"],
            },
          ],
        };
        const VOLPARPRODUIT = {
          labels: [...response.data.QNTBYPRODUITGRAPH.PRODUITS],
          datasets: [
            {
              label: "Volume Par Produits",
              data: [...response.data.QNTBYPRODUITGRAPH.QNTBYPRODUIT],
              backgroundColor: [
                "#ff6384",
                "#36a2eb",
                "#ffce56",
                "#0c38a5",
                "#eca90e",
                "#008000",
                "#FFA500",
                "#FF0000",
                "#9E5F95",
                "#F08C4F",
                "#D44B73",
                "#A8D5BA",
                "#57A8D8",
                "#F9C74F",
                "#A8E0B1",
                "#F1A7B7",
                "#F8D4B3",
              ],
            },
          ],
        };

        const CAPARPRODUIT = {
          labels: [...response.data.CANETBYPRODUITGRAPH.PRODUITS],
          datasets: [
            {
              label: "CA Net Par Produits",
              data: [...response.data.CANETBYPRODUITGRAPH.CANETBYPRODUIT],
              backgroundColor: [
                "#ff6384",
                "#36a2eb",
                "#ffce56",
                "#0c38a5",
                "#eca90e",
                "#008000",
                "#FFA500",
                "#FF0000",
                "#9E5F95",
                "#F08C4F",
                "#D44B73",
                "#A8D5BA",
                "#57A8D8",
                "#F9C74F",
                "#A8E0B1",
                "#F1A7B7",
                "#F8D4B3",
              ],
            },
          ],
        };

        const PRODUCTS_MARGIN_PRICES = {
          labels: [
            ...response.data.CHARTCOUTREVIENWITHPRIXVENTE[0].PRODUCTSNAME,
          ],
          datasets: [
            {
              label: "Cout de Revient",
              data: [
                ...response.data.CHARTCOUTREVIENWITHPRIXVENTE[0].COUTREVIEN,
              ],
              backgroundColor: ["#0c38a5"],
              borderColor: "#0c38a5",
            },
            {
              label: "Prix de Vente",
              data: [
                ...response.data.CHARTCOUTREVIENWITHPRIXVENTE[0].PRIXVENTE,
              ],
              backgroundColor: ["#eca90e"],
              borderColor: "#eca90e",
            },
          ],
        };

        const PRODUCTS_MARGIN_POURCENTANGE_Marge = {
          labels: [
            ...response.data.MARGE_PRODUCTS_BY_CLIENTS_CHART.PRODUCTSNAME,
          ],
          datasets: [
            {
              label: "Marge Bénéficiaire En %",
              data: [...response.data.MARGE_PRODUCTS_BY_CLIENTS_CHART.MARGE],
              backgroundColor: [
                "#0c38a5",
                "#eca90e",
                "#008000",
                "#FFA500",
                "#FF0000",
                "#9E5F95",
                "#F08C4F",
                "#D44B73",
                "#A8D5BA",
                "#57A8D8",
                "#F9C74F",
                "#A8E0B1",
                "#F1A7B7",
                "#F8D4B3",
              ],
              borderColor: "#0c38a5",
            },
          ],
        };

        console.log("Selected Clients:", Clients);

        const DSO_CLIENTS_CHART = {
          labels:
            response.data.Daily_vs_payment_date_CHART.DSO_CLIENTS_CHART.data[
              response.data.Daily_vs_payment_date_CHART.DSO_CLIENTS_CHART
                .client_names[0]
            ].dates,
          datasets:
            response.data.Daily_vs_payment_date_CHART.DSO_CLIENTS_CHART.client_names.flatMap(
              (clientName) => {
                const clientData =
                  response.data.Daily_vs_payment_date_CHART.DSO_CLIENTS_CHART
                    .data[clientName];
                return [
                  {
                    label: `${clientName} - Délai de Paiement Accordé (jours)`,
                    data: Array(clientData.dates.length).fill(
                      clientData.client_delay_days
                    ),
                    backgroundColor: "#0c38a5",
                    borderColor: "#0c38a5",
                  },
                  {
                    label: `${clientName} - Date de Recouvrement Effectué (jours)`,
                    data: clientData.max_dso,
                    backgroundColor: "#eca90e",
                    borderColor: "#eca90e",
                  },
                ];
              }
            ),
        };

        const CREANCE_CA_API = {
          labels: [...response.data.CREANCE_CLIENT_CHART.dates],
          datasets: [
            {
              label: "SOMME DU CREANCE CLIENT",
              data: [...response.data.CREANCE_CLIENT_CHART.net_receivables],
              backgroundColor: ["#0c38a5"],
              borderColor: "#0c38a5",
            },
            {
              label: "RECOUVREMENT EFFECTUER",
              data: [...response.data.CREANCE_CLIENT_CHART.reglements],
              backgroundColor: ["#FFC0CB"],
              borderColor: "#FFC0CB",
            },
            {
              label: "VALEUR IMPAYE",
              data: [...response.data.CREANCE_CLIENT_CHART.impayes],
              backgroundColor: ["#FF0000"],
              borderColor: "#FF0000",
            },
            {
              label: "SOMME DU CA BRUT",
              data: [...response.data.CREANCE_CLIENT_CHART.ca_brut],
              backgroundColor: ["#eca90e"],
              borderColor: "#eca90e",
            },
          ],
        };
        const DSO_CLIENTS = {
          labels: [...response.data.DSO_clients.dates],
          datasets: [
            {
              label: "DSO Clients",
              data: [...response.data.DSO_clients.dso_values],
              backgroundColor: "#0c38a5",
              borderColor: "#0c38a5",
            },
          ],
        };
        const REPARTITION_MODES_PAYEMENTS = {
          labels: [
            ...response.data.RepartitionModesPayments_data.Mode_Payement,
          ],
          datasets: [
            {
              label: "Repartition des modes de paiement",
              data: [...response.data.RepartitionModesPayments_data.percentage],
              backgroundColor: [
                "#1f77b4", // Blue
                "#ff7f0e", // Orange
                "#2ca02c", // Green
                "#d62728", // Red
                "#9467bd", // Purple
                "#8c564b", // Brown
                "#e377c2", // Pink
                "#7f7f7f", // Gray
                "#bcbd22", // Yellow-green
                "#17becf", // Cyan
              ],
              borderColor: [
                "#1f77b4",
                "#ff7f0e",
                "#2ca02c",
                "#d62728",
                "#9467bd",
                "#8c564b",
                "#e377c2",
                "#7f7f7f",
                "#bcbd22",
                "#17becf",
              ],
              borderWidth: 1,
            },
          ],
        };

        this.DELAI_PAIEMENT_VS_RECOUVREMENT = DSO_CLIENTS_CHART;
        this.CREANCE_CA = CREANCE_CA_API;
        this.CREANCE_CA = CREANCE_CA_API;
        this.CANETCABRUT = CA;
        this.QNTENTANDM3 = QNT;
        this.PMVGLOBALS = PMV;
        this.VOLPARPRODUIT = VOLPARPRODUIT;
        this.PRODUCTS_SOLD = VOLUMEBYPRODUCTS;
        this.CAPARPRODUIT = CAPARPRODUIT;
        this.PRODUCTS_MARGIN = PRODUCTS_MARGIN_PRICES;
        this.PRODUCTS_MARGIN_POURCENTANGE = PRODUCTS_MARGIN_POURCENTANGE_Marge;
        this.DSO_CLIENTS = DSO_CLIENTS;
        this.REPARTITION_MODES_PAYEMENTS = REPARTITION_MODES_PAYEMENTS;
        this.isLoadingContent = true;

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
