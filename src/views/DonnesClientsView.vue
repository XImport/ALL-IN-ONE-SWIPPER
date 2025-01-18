<template>
  <div>
    <AppHeaderBar
      :DATA="DATA"
      :FetchQuery="FetchQuery"
      :StaticInfo="{ icon: 'mdi-database', title: 'Données Clients' }"
    />
    <div
      style="position: fixed; top: 150px; left: 0%; z-index: 5 !important"
      v-show="!isDrawerOpen"
    >
      <v-btn
        icon="mdi-arrow-collapse-right"
        elevation="3"
        @click="ChangeDrawerState()"
        size="x-large"
      ></v-btn>
    </div>
    <div
      style="position: fixed; top: 150px; left: 15%; z-index: 5 !important"
      v-show="isDrawerOpen"
    >
      <v-btn
        icon="mdi-arrow-collapse-left"
        elevation="3"
        @click="ChangeDrawerState()"
        size="x-large"
      ></v-btn>
    </div>
    <div
      :class="{
        'content-with-drawer': isDrawerOpen,
        'content-full-width': !isDrawerOpen,
      }"
    >
      <v-container
        fluid
        class="px-0 pb-2 justify-center align-center"
        style="max-width: 80%"
      >
        <div class="d-flex flex-row align-center px-4 gap-4">
          <div class="flex-grow-0 flex-shrink-0" style="width: 100%">
            <div style="margin-right: 25%">
              <h2 class="text-center text-decoration-underline">
                <v-icon class="pb-2" color="purple">mdi-account-group</v-icon>
                Nombre total de clients enregistrés :
                <span class="text-red"
                  >{{ DATATABLE.length }} <span>clients</span>
                </span>
              </h2>
            </div>
            <v-container
              style="max-width: 70%; margin-right: 25%; margin-top: 0%"
            >
              <v-text-field
                label="Recherche par nom ...
"
                v-model="filterText"
                variant="solo"
              ></v-text-field>
            </v-container>
          </div>
        </div>
      </v-container>
      <DialogClientsDetails />
      <TableCompo :DATA="filterDATA" :Headers="Headers" />
    </div>
  </div>
</template>

<script>
import AppHeaderBar from "../components/GlobalComponents/AppHeaderBar.vue";
import TableJS from "../components/MiniComponents/Tables/TableJS.vue";
import TableCompo from "../components/MiniComponents/Tables/TableCompo.vue";
import DialogClientsDetails from "../components/MiniComponents/DialogClientsDetails.vue";
export default {
  components: {
    AppHeaderBar,
    TableJS,
    TableCompo,
    DialogClientsDetails,
  },
  methods: {
    ChangeDrawerState() {
      this.$store.commit("ChangeDrawerState");
    },
    FetchQuery() {
      console.log("hello world");
    },
  },
  computed: {
    isDrawerOpen() {
      return this.$store.getters.GetDrawerState; // Assuming you store drawer state in Vuex
    },
    filterDATA() {
      return this.DATATABLE.filter((name) => {
        return Object.values(name).some((value) =>
          value.toString().toLowerCase().includes(this.filterText.toLowerCase())
        );
      });
    },
  },
  data() {
    return {
      filterText: "",
      DATA: {
        DébutDate: "",
        FinDate: "",
      },

      DATATABLE: [
        {
          key1: "C001",
          key2: "Jean Dupont",
          key3: "Commerce",
          key4: "Marie Lemoine",
          key5: "jean.dupont@example.com",
          key6: "0123456789",
          key7: "2023-01-01",
        },
        {
          key1: "C002",
          key2: "Claire Martin",
          key3: "Technologie",
          key4: "Paul Girard",
          key5: "claire.martin@example.com",
          key6: "0987654321",
          key7: "2023-01-10",
        },
        {
          key1: "C003",
          key2: "Luc Lefevre",
          key3: "Finance",
          key4: "Sophie Durand",
          key5: "luc.lefevre@example.com",
          key6: "0765432109",
          key7: "2023-02-02",
        },
        {
          key1: "C004",
          key2: "Alice Durand",
          key3: "Marketing",
          key4: "Jean Lefevre",
          key5: "alice.durand@example.com",
          key6: "0678901234",
          key7: "2023-03-15",
        },
        {
          key1: "C005",
          key2: "David Moreau",
          key3: "Informatique",
          key4: "Catherine Gauthier",
          key5: "david.moreau@example.com",
          key6: "0654321098",
          key7: "2023-04-20",
        },
        {
          key1: "C006",
          key2: "Emma Dupuis",
          key3: "Energie",
          key4: "Vincent Girard",
          key5: "emma.dupuis@example.com",
          key6: "0612345678",
          key7: "2023-05-10",
        },
        {
          key1: "C007",
          key2: "Pauline Lefevre",
          key3: "Marketing",
          key4: "Julien Bonnet",
          key5: "pauline.lefevre@example.com",
          key6: "0765439876",
          key7: "2023-06-11",
        },
        {
          key1: "C008",
          key2: "Martin Lefevre",
          key3: "Design",
          key4: "Alice Lambert",
          key5: "martin.lefevre@example.com",
          key6: "0732456789",
          key7: "2023-07-05",
        },
        {
          key1: "C009",
          key2: "Lucie Bonnet",
          key3: "Management",
          key4: "Michel Guerin",
          key5: "lucie.bonnet@example.com",
          key6: "0698765432",
          key7: "2023-08-01",
        },
        {
          key1: "C010",
          key2: "Sophie Gauthier",
          key3: "E-commerce",
          key4: "Julien Dupont",
          key5: "sophie.gauthier@example.com",
          key6: "0654327654",
          key7: "2023-09-14",
        },
        {
          key1: "C011",
          key2: "Nicolas Martin",
          key3: "Logistique",
          key4: "Pauline Lefevre",
          key5: "nicolas.martin@example.com",
          key6: "0612348765",
          key7: "2023-10-20",
        },
        {
          key1: "C012",
          key2: "Camille Boucher",
          key3: "Communication",
          key4: "Bernard Lemoine",
          key5: "camille.boucher@example.com",
          key6: "0756789876",
          key7: "2023-11-02",
        },
        {
          key1: "C013",
          key2: "Henri Lefevre",
          key3: "Technologie",
          key4: "Marie Girard",
          key5: "henri.lefevre@example.com",
          key6: "0789654321",
          key7: "2023-12-12",
        },
        {
          key1: "C014",
          key2: "Isabelle Bonnet",
          key3: "Marketing",
          key4: "Antoine Boucher",
          key5: "isabelle.bonnet@example.com",
          key6: "0678906789",
          key7: "2024-01-07",
        },
        {
          key1: "C015",
          key2: "Thomas Martin",
          key3: "Business",
          key4: "Hélène Lefevre",
          key5: "thomas.martin@example.com",
          key6: "0634567890",
          key7: "2024-02-08",
        },
        {
          key1: "C016",
          key2: "Marie Bernard",
          key3: "Finance",
          key4: "Louis Lemoine",
          key5: "marie.bernard@example.com",
          key6: "0676543210",
          key7: "2024-03-15",
        },
        {
          key1: "C017",
          key2: "Gerard Lefevre",
          key3: "Informatique",
          key4: "Sophie Lefevre",
          key5: "gerard.lefevre@example.com",
          key6: "0765438765",
          key7: "2024-04-18",
        },
        {
          key1: "C018",
          key2: "Alice Gauthier",
          key3: "Commerce",
          key4: "Michel Dupont",
          key5: "alice.gauthier@example.com",
          key6: "0698765432",
          key7: "2024-05-22",
        },
        {
          key1: "C019",
          key2: "Vincent Bonnet",
          key3: "Design",
          key4: "Catherine Lefevre",
          key5: "vincent.bonnet@example.com",
          key6: "0789654321",
          key7: "2024-06-03",
        },
        {
          key1: "C020",
          key2: "Julien Gauthier",
          key3: "Consulting",
          key4: "Nathalie Lefevre",
          key5: "julien.gauthier@example.com",
          key6: "0678901234",
          key7: "2024-07-01",
        },
      ],

      Headers: {
        H1: "Code",
        H2: "Nom du client",
        H3: "Secteur d'activité",
        H4: "Représentant",
        H5: "Email",
        H6: "Numéro Télephone",
        H7: "Date",
      },
    };
  },
};
</script>

<style scoped>
.content-with-drawer {
  margin-left: 15% !important;
  width: calc(100% - 280px) !important;
  transition: margin-left 0.3s ease, width 0.3s ease;
  margin-top: 5%;
}

.content-full-width {
  margin-left: 0;
  margin: auto;
  width: 95%;
  transition: margin-left 0.3s ease, width 0.3s ease;
  margin-top: 5%;
}

.font-weight-bold {
  color: #000; /* Matches the bold black title */
}
.text-subtitle-2 {
  color: #555; /* Matches the lighter text */
}

.v-card {
  box-shadow: none !important;
}

.v-text-field {
  box-shadow: none;
}
</style>
