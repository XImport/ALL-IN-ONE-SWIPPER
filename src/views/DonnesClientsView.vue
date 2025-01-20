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
import axiosInstance from "../Axios";
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
    async FetchQuery(DATA) {
      try {
        const response = await axiosInstance.post("/API/V1/InfoClients", DATA, {
          headers: {
            "Content-Type": "application/json",
          },
        });

        // Replace NaN with null before parsing
        const cleanedData = response.data.replace(/: NaN/g, ": null");
        const jsonData = JSON.parse(cleanedData);
        console.log(jsonData);
        const transformedData = jsonData.INFO_CLIENTS.map((client) => ({
          code: client.CODE?.toString() || "",
          name: client["NOM DU CLIENT"] || "",
          secteur: client["SECTEUR D'ACTIVITE"] || "",
          representant: client.REPRESENTANT || "",
          email: client.EMAIL || "",
          location: client.LOCALISATION || "",
          phonenumber: client["NUMERO TELEPHONE"] || "",
          entrydate: client["DATE D'EMCHEMENT"]?.split("T")[0] || "",
          caBrut: client["CA BRUT"] || 0,
          volume: client["Qté en T"] || 0,
          suivipar: client["SUIVI PAR"] || "",
          coutTransport: client["COUT TRANSPORT"] || 0,
          typegarantie: client["TYPE DE GARANTIE"] || "",
          Modereglement: client["MODE DE REGLEMENT"] || "", // Replace "looooool" with a proper value
          plafond: client["PLAFOND MENSUELLE"] || 0,
          etatfinancier: client["ETAT FINANCIERE"] || "",
          uniteVente: client["UNITE VENTE"] || "",
          pourcentagefacturation: client["POURCENTANGE FACTURATION"] || 0,
          TarificationProduits: {
            grainderiz: client["GRAIN DE RIZ"] || 0,
            gravetteg1: client["GRAVETTE G1"] || 0,
            gravetteg2: client["GRAVETTE G2"] || 0,
            sableconcassage04: client["SABLE CONCASSAGE 0-4"] || 0,
            sableconcassage02: client["SABLE CONCASSAGE 0-2"] || 0,
            toutvenant0315: client["TOUT VENANT 0-31.5"] || 0,
            toutvenant040: client["TOUT VENANT 0-40"] || 0,
            toutvenant060: client["TOUT VENANT 0-60"] || 0,
            toutvenant0100: client["TOUT VENANT 0-100"] || 0,
            sterile: client["STERILE"] || 0,
            sterilefin: client["STERILE FIN"] || 0,
          },
        }));

        this.DATATABLE = transformedData;
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    isDrawerOpen() {
      return this.$store.getters.GetDrawerState; // Assuming you store drawer state in Vuex
    },
    filterDATA() {
      return this.DATATABLE.filter((name) => {
        return Object.values(name).some((value) =>
          value
            ?.toString()
            .toLowerCase()
            .includes(this.filterText.toLowerCase())
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
          code: null,
          name: null,
          secteur: null,
          representant: null,
          email: null,
          localisation: null,
          phonenumber: null,
          entrydate: null,
          caBrut: null,
          suivipar: null,
          volume: null,
          coutTransport: null,
          typegarantie: null,
          Modereglement: null,
          plafond: null,
          etatfinancier: null,
          uniteVente: null,
          pourcentagefacturation: null,
          TarificationProduits: {
            grainderiz: null,
            gravetteg1: null,
            gravetteg2: null,
            sableconcassage04: null,
            sableconcassage02: null,
            toutvenant0315: null,
            toutvenant040: null,
            toutvenant060: null,
            toutvenant0100: null,
            sterile: null,
            sterilefin: null,
          },
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
