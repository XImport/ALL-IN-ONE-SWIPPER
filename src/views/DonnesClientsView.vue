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
      <div v-if="SpinnerLoader">
        <v-progress-linear
          color="yellow-darken-2"
          indeterminate
          style="margin-top: 5%"
        ></v-progress-linear>
        <div style="position: absolute; top: 30%; left: 40%">
          <div class="bg-white pa-12 rounded-xl">
            <h1 class="text-center text-decoration-underline">
              Préparation des données ...
            </h1>
            <h3 class="text-center text-grey mt-2">Merci de patienter 🔍😁</h3>
          </div>
        </div>
      </div>
      <div v-if="LoadingContent">
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
                    >{{ DATATABLE.length }} <span>clients</span
                    ><span>
                      <v-tooltip
                        text="Exporter Vers Excel"
                        location="top"
                        activator="parent"
                      >
                        <template v-slot:activator="{ props }">
                          <v-btn
                            icon
                            compact
                            size="20"
                            class="ml-2"
                            style="margin-top: -1%"
                            v-bind="props"
                            @click="ExportToExcel(EXPORTDATATABLE, Headers2)"
                          >
                            <v-img
                              src="https://static-00.iconduck.com/assets.00/ms-excel-icon-2048x2026-nws24wyy.png"
                              width="25"
                              style="
                                display: inline-block;
                                vertical-align: middle;
                              "
                            ></v-img>
                          </v-btn>
                        </template>
                      </v-tooltip>
                    </span>
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
  </div>
</template>

<script>
import AppHeaderBar from "../components/GlobalComponents/AppHeaderBar.vue";
import TableJS from "../components/MiniComponents/Tables/TableJS.vue";
import TableCompo from "../components/MiniComponents/Tables/TableCompo.vue";
import DialogClientsDetails from "../components/MiniComponents/DialogClientsDetails.vue";
import axiosInstance from "../Axios";
import { exportToExcel } from "../utils";
import * as XLSX from "xlsx";
export default {
  components: {
    AppHeaderBar,
    TableJS,
    TableCompo,
    DialogClientsDetails,
  },
  methods: {
    ExportToExcel(data, headers, filename = "INFO_CLIENTS_TABLE_DATA.xlsx") {
      if (!Array.isArray(data) || data.length === 0) {
        console.error("Invalid data provided!");
        return;
      }

      // Map data to match the given headers
      const formattedData = data.map((item) => ({
        [headers.H1]: item["CODE"],
        [headers.H2]: item["NOM DU CLIENT"],
        [headers.H3]: item["SECTEUR D'ACTIVITE"],
        [headers.H4]: item["TRANSPORTEUR"],
        [headers.H5]: item["REPRESENTANT"],
        [headers.H6]: item["EMAIL"],
        [headers.H7]: item["NUMERO TELEPHONE"],
        [headers.H8]: item["DATE D'EMCHEMENT"],

        [headers.H9]: item["TYPE DE GARANTIE"],
        [headers.H10]: item["MODE DE REGLEMENT"],
        [headers.H11]: item["PLAFOND MENSUELLE"],
        [headers.H12]: item["LOCALISATIONT"],
        [headers.H13]: item["SUIVI PAR"],
        [headers.H14]: item["POURCENTANGE FACTURATION"],
        [headers.H15]: item["UNITE VENTE"],

        [headers.H16]: item["ETAT FINANCIERE"],
        [headers.H17]: item["Mode de Paiement"],
        [headers.H18]: item["Transport"],
        [headers.H19]: item["GRAIN DE RIZ"],
        [headers.H20]: item["GRAVETTE G1"],
        [headers.H21]: item["GRAVETTE G2"],
        [headers.H22]: item["SABLE CONCASSAGE 0-4"],

        [headers.H23]: item["SABLE CONCASSAGE 0-2"],

        [headers.H24]: item["TOUT VENANT 0-31.5"],

        [headers.H25]: item["TOUT VENANT 0-40"],

        [headers.H26]: item["TOUT VENANT 0-60"],

        [headers.H27]: item["TOUT VENANT 0-100"],

        [headers.H28]: item["STERILE"],

        [headers.H29]: item["STERILE FIN"],
      }));

      // Create a new workbook
      const workbook = XLSX.utils.book_new();

      // Convert data to a worksheet
      const worksheet = XLSX.utils.json_to_sheet(formattedData);

      // Append the worksheet to the workbook
      XLSX.utils.book_append_sheet(workbook, worksheet, "Sheet1");

      // Write the workbook and trigger download
      XLSX.writeFile(workbook, filename);
    },

    ChangeDrawerState() {
      this.$store.commit("ChangeDrawerState");
    },
    async FetchQuery(DATA) {
      this.SpinnerLoader = true;
      this.LoadingContent = false;

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
        this.EXPORTDATATABLE = jsonData.INFO_CLIENTS;
        const transformedData = jsonData.INFO_CLIENTS.map((client) => ({
          code: client.CODE?.toString() || "",
          name: client["NOM DU CLIENT"] || "",
          secteur: client["SECTEUR D'ACTIVITE"] || "",
          representant: client.REPRESENTANT || "",
          email: client.EMAIL || "",
          location: client.LOCALISATION || "", // :::::
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
          ISTRANSPORTEUR: client["TRANSPORTEUR"],
          pourcentagefacturation: client["POURCENTANGE FACTURATION"] || 0,
          TransportPrice: client["Transport"] || 0,
          Modedepaiement: client["Mode de Paiement"] || 0,

          CTransport: client["Transport Frs"] || 0,
          TarificationProduits: {
            gabion: client["GABION"] || 0,
            filtre: client["FILTRE"] || 0,
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
        this.SpinnerLoader = false;

        this.LoadingContent = true;
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
      EXPORTDATATABLE: null,
      DATA: {
        DébutDate: "",
        FinDate: "",
      },
      LoadingContent: false,
      SpinnerLoader: false,

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
      Headers2: {
        H1: "CODE",
        H2: "NOM DU CLIENT",
        H3: "SECTEUR D'ACTIVITE ",
        H4: "TRANSPORTEUR",
        H5: "REPRESENTANT",
        H6: "EMAIL",
        H7: "NUMERO TELEPHONE",
        H8: "DATE D'EMCHEMENT",
        H9: "TYPE DE GARANTIE",
        H10: "MODE DE REGLEMENT",
        H11: "PLAFOND MENSUELLE",
        H12: "LOCALISATION",
        H13: "SUIVI PAR",
        H14: "POURCENTANGE FACTURATION",
        H15: "UNITE VENTE",
        H16: "ETAT FINANCIERE",
        H17: "Mode de Paiement",
        H18: "Transport",
        H19: "GRAIN DE RIZ",
        H20: "GRAVETTE G1",
        H21: "GRAVETTE G2",
        H22: "SABLE CONCASSAGE 0-4",
        H23: "SABLE CONCASSAGE 0-2",
        H24: "TOUT VENANT 0-31.5",

        H25: "TOUT VENANT 0-40",
        H26: "TOUT VENANT 0-60",
        H27: "TOUT VENANT 0-100",
        H28: "STERILE",
        H29: "STERILE FIN",
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
