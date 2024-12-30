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

    <v-container fluid style="max-width: 100%">
      <v-row dense class="d-flex justify-space-between">
        <v-col cols="12" sm="12" class="pa-2">
          <h2 class="text-center text-decoration-underline">
            <v-icon color="pink">mdi-table-large</v-icon> Tableau de Bord des
            Indicateurs Commerciaux par Graphiques :
            <span class="text-pink">2024</span>
          </h2>
        </v-col>
      </v-row>
    </v-container>

    <v-container fluid style="max-width: 100%">
      <v-row dense class="d-flex justify-space-between">
        <v-col cols="12" sm="6" class="pa-2">
          <BarChartJS
            :CHARTDATA="COMMANDDEMANDEANDCOMMANDLIVRE"
            title="Analyse des Commandes Demandées et Livrées (Par Date)"
            IconName="mdi-poll"
            IconColor="purple"
          />
        </v-col>
        <v-col cols="12" sm="6" class="pa-2">
          <BarChartJS
            :CHARTDATA="QNTENTANDM3"
            title="Volume de Vente : Tonnes et Mètres Cubes (Par Date)"
            IconName="mdi-chart-tree"
            IconColor="green"
          />
        </v-col>
      </v-row>
    </v-container>
    <v-container fluid style="max-width: 100%">
      <v-row dense class="d-flex justify-space-between">
        <v-col cols="12" sm="6" class="pa-2">
          <LineChartJS
            :CHARTDATA="CANETCABRUT"
            title="Évolution du CA Brut et du CA Net (Par Date)"
            IconName="mdi-chart-ppf"
            IconColor="blue"
          />
        </v-col>
        <v-col cols="12" sm="6" class="pa-2">
          <BarChartJS
            :CHARTDATA="PMVGLOBALS"
            title="Situation du PVM : Nobles Graves Et Le  Stérile (Par Date)"
            IconName="mdi-chart-box"
            IconColor="pink"
          />
        </v-col>
      </v-row>
    </v-container>
    <v-container fluid style="max-width: 100%">
      <v-row dense class="d-flex justify-space-between">
        <v-col cols="12" sm="6" class="pa-2">
          <BarChartJS
            :CHARTDATA="TOP6CLIENTS"
            title="Analyse du CA Brut pour les 6 principaux clients (Par Date)"
            IconName="mdi-chart-box-multiple"
            IconColor="red"
          />
        </v-col>

        <v-col cols="12" sm="6" class="pa-2">
          <BarChartJS
            :CHARTDATA="CREANCERECOUVREMENTENCAISSEMENT"
            title="Performance des Créances Commerciales et du Recouvrement (Par Date)"
            IconName="mdi-chart-areaspline"
            IconColor="brown"
          />
        </v-col>
      </v-row>
    </v-container>

    <v-container fluid style="max-width: 100%">
      <v-row dense class="d-flex justify-space-between">
        <v-col cols="12" sm="6" class="pa-2">
          <div
            style="
              width: 100%;
              display: flex;
              justify-content: center;
              margin-top: 5%;
            "
          >
            <DonutsChartJS
              :CHARTDATA="VOLPARPRODUIT"
              title="État des Ventes par Produit en Tonnes (Par Date)"
              IconName="mdi-chart-pie"
              IconColor="orange"
            />
          </div>
        </v-col>

        <v-col cols="12" sm="6" class="pa-2">
          <div
            style="
              width: 100%;
              display: flex;
              justify-content: center;
              margin-top: 5%;
            "
          >
            <DonutsChartJS
              :CHARTDATA="CAPARPRODUIT"
              title="État des Ventes par Produit en CA NET (Par Date)"
              IconName="mdi-chart-pie"
              IconColor="orange"
            />
          </div>
        </v-col>
      </v-row>
    </v-container>

    <v-container fluid style="max-width: 100%; margin-left: 30% !important">
      <v-row dense class="d-flex align-center">
        <v-col cols="auto" class="pa-0">
          <h2 class="text-center text-decoration-underline mt-6">
            <v-icon color="pink">mdi-account-multiple-check</v-icon>
            Bilan des Objectifs Commerciaux Annuels Avec la Réalisation d'anneé
            <span class="text-pink">2024</span>
          </h2>
        </v-col>
      </v-row>
    </v-container>

    <v-container fluid style="max-width: 100%">
      <v-row dense class="d-flex justify-space-between">
        <v-col cols="12" sm="6" class="pa-2">
          <DataTABLE
            :Headers="TOneHeaders"
            :DATA="TOneDATA"
            DATATABLETITLE="Tableau des Objectifs et réalisations Ventes (Par Date)"
            TABLEICON="mdi-bag-checked"
            TABLECOLORICON="blue"
          />
        </v-col>
        <v-col cols="12" sm="6" class="pa-2">
          <DataTABLE
            :Headers="TTwoHeaders"
            :DATA="TTwoDATA"
            DATATABLETITLE="Tableau des Objectifs et Réalisation Créances Clients (Par Mois)"
            :reverse="true"
            TABLEICON="mdi-account-group"
            TABLECOLORICON="purple"
          />
        </v-col>
      </v-row>
    </v-container>
    <v-container fluid style="max-width: 100%">
      <v-row dense class="d-flex justify-space-between">
        <v-col cols="12" sm="6" class="pa-2">
          <DataTABLE
            :Headers="TTreeHeaders"
            :DATA="TTreeDATA"
            DATATABLETITLE="Tableau PVM par Catégorie (Par Date)"
            TABLEICON="mdi-chart-bar"
            TABLECOLORICON="red"
          />
        </v-col>
        <v-col cols="12" sm="6" class="pa-2">
          <DataTABLE
            :Headers="TFourHeaders"
            :DATA="TFourDATA"
            DATATABLETITLE="Tableau des Objectifs et Réalisations Recouvrement(Par Mois)"
            TABLEICON="mdi-cash-fast"
            TABLECOLORICON="green"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import AppHeaderBar from "../components/GlobalComponents/AppHeaderBar.vue";
import InfoCard from "../components/MiniComponents/InfoCard.vue";
import BarChartJS from "../components/MiniComponents/Charts/BarChartJS.vue";
import LineChartJS from "../components/MiniComponents/Charts/LineChartJS.vue";
import DonutsChartJS from "../components/MiniComponents/Charts/DonutsChartJS.vue";
import TableJS from "../components/MiniComponents/Tables/TableJS.vue";
import DataTABLE from "../components/MiniComponents/Tables/DataTABLE.vue";
export default {
  name: "BilanAnalytique",
  components: {
    AppHeaderBar,
    InfoCard,
    BarChartJS,
    LineChartJS,
    DonutsChartJS,
    TableJS,
    DataTABLE,
  },

  data() {
    return {
      TOneHeaders: [
        {
          title: "",
          align: "start",
          sortable: false,
          key: "Key1",
          class: "blue-header",
        },
        {
          title: "Objectif",
          key: "Key2",
          align: "start",
          class: "blue-header",
        },
        {
          title: "Réalisation",
          key: "Key3",
          align: "start",
          class: "blue-header",
        },
        {
          title: "Taux d'avancement ",
          key: "Key4",
          align: "start",
          class: "blue-header",
        },
      ],

      TOneDATA: [
        {
          Key1: "CA BRUT",
          Key2: 24568987.21, // Raw numeric value for Key2
          Key3: 23698741.32, // Raw numeric value for Key3
        },
        {
          Key1: "CA NET",
          Key2: 24568987.21, // Raw numeric value for Key2
          Key3: 23698741.32, // Raw numeric value for Key3
        },
        {
          Key1: "CA TRANSPORT",
          Key2: 24568987.21, // Raw numeric value for Key2
          Key3: 23698741.32, // Raw numeric value for Key3
        },
        {
          Key1: "MARGE DU TRANSPORT ",
          Key2: 24568987.21, // Raw numeric value for Key2
          Key3: 23698741.32, // Raw numeric value for Key3
        },
        {
          Key1: "PVM GLOBAL",
          Key2: 24568987.21, // Raw numeric value for Key2
          Key3: 23698741.32, // Raw numeric value for Key3
        },
      ],

      TTwoHeaders: [
        {
          title: "",
          align: "start",
          sortable: false,
          key: "Key1",
          class: "blue-header",
        },
        {
          title: "Objectif",
          key: "Key2",
          align: "start",
          class: "blue-header",
        },
        {
          title: "Réalisation",
          key: "Key3",
          align: "start",
          class: "blue-header",
        },
        {
          title: "Taux d'avancement ",
          key: "Key4",
          align: "start",
          class: "blue-header",
        },
      ],

      TTwoDATA: [
        {
          Key1: "Créance Commerciale",
          Key2: 1547963.21, // Raw numeric value for Key2
          Key3: 1887994.21, // Raw numeric value for Key3
        },
        {
          Key1: "Créance CRJ",
          Key2: 3254789.21, // Raw numeric value for Key2
          Key3: 9857623.32, // Raw numeric value for Key3
        },
        {
          Key1: "Créance H.Recouvrement",
          Key2: 1000000, // Raw numeric value for Key2
          Key3: 3845697.32, // Raw numeric value for Key3
        },
        {
          Key1: "Créance Contentieux",
          Key2: 1000000, // Raw numeric value for Key2
          Key3: 1365871.32, // Raw numeric value for Key3
        },
        {
          Key1: "Créance Global",
          Key2: 6802752.42, // Raw numeric value for Key2
          Key3: 16718617.32, // Raw numeric value for Key3
        },
      ],

      TTreeHeaders: [
        {
          title: "",
          align: "start",
          sortable: false,
          key: "Key1",
          class: "blue-header",
        },
        {
          title: "Objectif",
          key: "Key2",
          align: "start",
          class: "blue-header",
        },
        {
          title: "Réalisation",
          key: "Key3",
          align: "start",
          class: "blue-header",
        },
        {
          title: "Taux d'avancement ",
          key: "Key4",
          align: "start",
          class: "blue-header",
        },
      ],

      TTreeDATA: [
        {
          Key1: "PVM NOBLES",
          Key2: 44.21, // Raw numeric value for Key2
          Key3: 42.32, // Raw numeric value for Key3
        },
        {
          Key1: "PVM GRAVES",
          Key2: 34.21, // Raw numeric value for Key2
          Key3: 33.21, // Raw numeric value for Key3
        },
        {
          Key1: "PVM STERILE",
          Key2: 15.5, // Raw numeric value for Key2
          Key3: 14.97, // Raw numeric value for Key3
        },
      ],

      TFourHeaders: [
        {
          title: "",
          align: "start",
          sortable: false,
          key: "Key1",
          class: "blue-header",
        },
        {
          title: "Objectif",
          key: "Key2",
          align: "start",
          class: "blue-header",
        },
        {
          title: "Réalisation",
          key: "Key3",
          align: "start",
          class: "blue-header",
        },
        {
          title: "Taux d'avancement ",
          key: "Key4",
          align: "start",
          class: "blue-header",
        },
      ],

      TFourDATA: [
        {
          Key1: "Recouvrement",
          Key2: 24547965.21, // Raw numeric value for Key2
          Key3: 21654741.21, // Raw numeric value for Key3
        },
        {
          Key1: "Encaissement",
          Key2: 20654741.21, // Raw numeric value for Key2
          Key3: 19745321.32, // Raw numeric value for Key3
        },
        {
          Key1: "Compensation",
          Key2: 4000000, // Raw numeric value for Key2
          Key3: 3798631.32, // Raw numeric value for Key3
        },
      ],

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
            label: "Commandes Demandées",
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
            label: "Commandes Demandées",
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

      TOP6CLIENTS: {
        labels: [
          "BERHIMA TRANS",
          "NORD SUD DE TRANSPORT ",
          "VILLA MARIN TRANS",
          "CIMAT",
          "MANSOURI SJH",
          "TGCC",
        ],
        datasets: [
          {
            label: "CA BRUT",
            data: [
              4231658.32, 3658974, 1893254.28, 4987698.32, 2456879.32,
              1789547.32,
            ],
            backgroundColor: [
              "#00C853",
              "#0091EA",
              "#C51162",
              "#D50000",
              "#FF6D00",
              "#3E2723",
            ],
          },
        ],
      },

      COMMANDDEMANDEANDCOMMANDLIVRE: {
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
            label: "Commandes Demandées",
            data: [6, 10, 8, 4, 8, 14, 12, 6, 4, 6, 8, 10],
            backgroundColor: ["#0c38a5"],
          },
          {
            label: "Commandes Livrées",
            data: [6, 11, 9, 6, 8, 16, 13, 6, 4, 6, 10, 10],
            backgroundColor: ["#6c057b"],
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

      CREANCERECOUVREMENTENCAISSEMENT: {
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
            label: "Créance Commerciale",
            data: [
              2365987.2, 2700983.4, 3035989.6, 3370995.8, 3706002.0, 4041008.2,
              4376014.4, 4711020.6, 5046026.8, 5381033.0, 5716049.2, 6051055.4,
            ],
            backgroundColor: ["#BF360C"],
          },
          {
            label: "Recouvrement Commerciale",
            data: [
              3254987.32, 3034172.92, 2813358.52, 2592544.12, 2371730.72,
              2150916.32, 1930101.92, 1709287.52, 1488473.12, 1267660.72,
              1046846.32, 825634.92,
            ],
            backgroundColor: ["#F57C00"],
          },
          {
            label: "Encaissement Financiere ",
            data: [
              2547987.1, 2581432.3, 2614877.5, 2648322.7, 2681767.9, 2715213.1,
              2748658.3, 2782103.5, 2549365.7, 2572809.9, 2596254.1, 2619698.3,
            ],
            backgroundColor: ["#2E7D32"],
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
          Title: "PVM Global",
          IconColor: "lime-darken-4",
          TextNumber: 36.35,
          Icon: "mdi-circle-multiple", // Used a globe icon for global scope
        },
        {
          Title: "PVM Hors Stérile",
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

.v-btn {
  box-shadow: none;
}
</style>
