<template>
  <v-navigation-drawer
    v-model="dialogModel"
    width="900"
    location="right"
    temporary
  >
  

      

  <div  id="pdf-content">


    <v-container class="pa-2" >
      <v-img
  width="100%"
  aspect-ratio="16/9"
  cover
  src="https://i.postimg.cc/fbGvTyVy/Capture-d-cran-2025-02-12-141301.png"
></v-img>
      
     
      <!-- Header -->
      <v-row no-gutters class="pa-2 align-center justify-center mt-6">


   
        <v-btn
                            icon
                            compact
                            size="20"
                            class="ml-2"
                            style="margin-top: -1%;margin-right: 1.5%;"
                            @click="downloadPdf(clientName)"
                           
                           
                          >
                            <v-img
                              src="https://static-00.iconduck.com/assets.00/pdf-icon-1500x2048-5ftd129y.png"
                              width="20"
                              style="
                                display: inline-block;
                                vertical-align: middle;
                              "
                            ></v-img>
                          </v-btn>
        <h3
          class="text-h6 font-weight-medium text-decoration-underline font-weight-bold text-center"
        >
          Informations client:
        </h3>
        <v-btn
          icon="mdi-close"
          variant="outlined"
          density="compact"
          class="ml-4"
          @click="closeDialog"
        />
      </v-row>

      <v-divider class="my-1" />
   
     
      <div class="bg-grey-lighten-5 justify-center mx-auto py-2 mt-6">
        <div class="d-flex align-center pa-2 justify-center">
          <h3>{{ clientName }}</h3>
          <span
            class="text-body-2 font-weight-medium ml-2"
            v-if="clientData.etatfinancier == 'VIP'"
            ><v-chip color="green">
              {{ clientData.etatfinancier }}
            </v-chip></span
          >

          <span
            class="text-body-2 font-weight-medium ml-2"
            v-if="clientData.etatfinancier == 'DANGEROUS'"
            ><v-chip color="red">
              {{ clientData.etatfinancier }}
            </v-chip></span
          >
          <span
            class="text-body-2 font-weight-medium ml-2"
            
            >
            
            
            
            
            
            </span
          >


          <span
            class="text-body-2 font-weight-medium ml-2"
            v-if="clientData.etatfinancier == 'Fiable'"
            ><v-chip color="orange">
              {{ clientData.etatfinancier }}
            </v-chip></span
          >
          <span
            class="text-body-2 font-weight-medium ml-2"
            v-if="clientData.etatfinancier == 'Nocive'"
            ><v-chip color="blue">
              {{ clientData.etatfinancier }}
            </v-chip></span
          >
          <span
            class="text-body-2 font-weight-medium ml-2"
            v-if="clientData.etatfinancier == 'Nouveau'"
            ><v-chip color="grey">
              {{ clientData.etatfinancier }}
            </v-chip></span
          >
       
        </div>
      </div>
      <!-- ------------------------------ -->

      <!-- Stats Overview -->
      <v-container class="pa-1 border rounded my-2" style="max-width: 98%">
        <v-row no-gutters>
          <template v-for="(stat, index) in computedStats" :key="index">
            <v-col cols="6" sm="3" class="text-center py-2">
              <div class="text-caption text-medium-emphasis">
                {{ stat.label }} <span style="font-size: x-small !important ; color: black !important;" v-if="stat.smlabel"> ( {{ stat.smlabel }} )</span>
              </div>
              <div class="text-subtitle-2 font-weight-bold" >
                {{ stat.value }} <span v-if="stat.label != 'Quantité En T'">dhs</span> 
              </div>
            </v-col>
            <template v-if="index < computedStats.length - 1">
              <v-divider vertical />
            </template>
          </template>
        </v-row>
      </v-container>

      <!-- Customer Details -->
      <div class="px-2 py-2 d-flex align-center justify-center">
        <h3
          class="text-h6 font-weight-medium text-center font-weight-bold text-decoration-underline"
        >
          Détail du Client
        </h3>
      </div>

      <v-container class="pa-2 bg-grey-lighten-5 rounded">
        <v-row dense>
          <template v-for="(detail, index) in computedDetails" :key="index">
            <v-col cols="12" sm="6">
              <v-sheet
                class="pa-3 d-flex justify-space-between align-center rounded bg-white"
              >
                <span class="text-caption text-medium-emphasis">{{
                  detail.label
                }}</span>
                <span
                  class="text-body-2 font-weight-medium ml-2"
                  v-if="
                    detail.value != 'VIP' &&
                    detail.value != 'DANGEROUS' &&
                    detail.value != 'Fiable' &&
                    detail.value != 'Nocive' &&
                    detail.value != 'Nouveau' &&
                    detail.value != 'COMMERCIAL' &&
                    detail.value != 'CRJ' &&
                    detail.value != 'H.RECOUVREMENT' &&
                    detail.value != 'Client Rendu'
                  "
                  >{{ detail.value }}</span
                >

                <span
                  class="text-body-2 font-weight-medium ml-2"
                  v-if="detail.value == 'COMMERCIAL'"
                  ><v-chip color="green" size="x-small">
                    {{ detail.value }}
                  </v-chip></span
                >

                <span
                  class="text-body-2 font-weight-medium ml-2"
                  v-if="detail.value == 'CRJ'"
                  ><v-chip color="orange" size="x-small">
                    {{ detail.value }}
                  </v-chip></span
                >

                <span
                  class="text-body-2 font-weight-medium ml-2"
                  v-if="detail.value == 'H.RECOUVREMENT'"
                  ><v-chip color="yellow" size="x-small">
                    {{ detail.value }}
                  </v-chip></span
                >

                <span
                  class="text-body-2 font-weight-medium ml-2"
                  v-if="detail.value == 'VIP'"
                  ><v-chip color="green" size="x-small">
                    {{ detail.value }}
                  </v-chip></span
                >

                <span
                  class="text-body-2 font-weight-medium ml-2"
                  v-if="detail.value == 'DANGEROUS'"
                  ><v-chip color="red" size="x-small">
                    {{ detail.value }}
                  </v-chip></span
                >
                <span
                  class="text-body-2 font-weight-medium ml-2"
                  v-if="detail.value == 'Fiable'"
                  ><v-chip color="orange" size="x-small">
                    {{ detail.value }}
                  </v-chip></span
                >
                <span
                  class="text-body-2 font-weight-medium ml-2 text-black"
                  v-if="detail.value == 'Nocive'"
                  ><v-chip color="blue" size="x-small">
                    {{ detail.value }}
                  </v-chip></span
                >

                <span
                  class="text-body-2 font-weight-medium ml-2"
                  v-if="detail.value == 'Nouveau'"
                  ><v-chip color="grey" size="x-small">
                    {{ detail.value }}
                  </v-chip></span
                >
              </v-sheet>
            </v-col>
          </template>
        </v-row>

        <template v-for="(detail, index) in computedLastStats" :key="index">
          <v-sheet
            class="d-flex justify-space-between align-center pa-3 rounded bg-white mt-2"
          >
            <span class="text-caption text-medium-emphasis">{{
              detail.label
            }}</span>
            <span class="text-body-2 font-weight-medium">{{
              detail.value
            }}</span>
          </v-sheet>
        </template>
      </v-container>
    </v-container>
    <div class="px-2 pt-2 d-flex align-center justify-center">
      <h3
        class="text-subtitle-h6 font-weight-medium text-decoration-underline font-weight-bold"
      >
        Tarification des Produits :
      </h3>
    </div>
    <v-container class="pa-2">
      <v-row dense>
        <template v-for="(detail, index) in computedPrices" :key="index">
          <v-col cols="auto" sm="4" class="d-flex">
            <v-sheet class="ma-1 rounded flex-grow-1" elevation="0">
              <div class="pa-2 text-center">
                <div class="text-subtitle-2 text-medium-emphasis mb-1">
                  {{ detail.label }}
                </div>
                <div class="text-h6 font-weight-bold text-primary">
                  {{ detail.value }}
                </div>
              </div>
            </v-sheet>
            <v-divider
              v-if="index < computedPrices.length - 1"
              vertical
              class="my-2"
            />
          </v-col>
        </template>
      </v-row>
    </v-container>
    <div style="height: 50px !important;" ></div>
    <v-img
  width="100%"
  aspect-ratio="16/9"
  cover
  src="https://i.postimg.cc/VvL0YPW5/Capture-d-cran-2025-02-12-141404.png"
></v-img>
  </div>




  </v-navigation-drawer>
</template>

<script>





// import html2pdf from 'html2pdf.js';


import { jsPDF } from 'jspdf';

import html2pdf from 'html2pdf.js/dist/html2pdf.bundle.min'



export default {
  name: "DialogClientsDetails",
  components: {
   
  },
  data() {
    return {
      isExporting: false,
      pdfRef: null,

      clientTags: [
        { label: "Nocive", color: "error" },
        { label: "Transporteur", color: "warning" },
      ],
      details: [],
      hover: false,
    };
  },

  computed: {
    splitText() {
      return function (text) {
        if (!text) return "";

        const words = text.trim().split(/\s+/);

        if (words.length === 1) {
          return words[0].slice(0, 3).toUpperCase();
        }

        return words
          .map((word) => word[0])
          .join("")
          .toUpperCase();
      };
    },
    dialogModel: {
      get() {
        return this.$store.getters.GetClientDialog;
      },
      set(value) {
        this.$store.commit("ChangeClientDialog", value);
      },
    },

    clientData() {
      return this.$store.getters.GetOneClientData;
    },

    clientName() {
      return this.clientData?.name || "LAMLIH TRANS";
    },

    clientInitials() {
      return "LT"; // You can compute this from client name
    },

    computedStats() {
      const data = this.clientData || {};
      return [
        {
          label: "CA BRUT",
          value: this.formatCurrency(data.caBrut || 0),
        },
        {
          label: "Quantité En T",
          value: `${this.formatNumber(data.volume || 0)} T`,
        },
        {
          label: "Créance Client",
          smlabel : 'A Jour',
          value: this.formatCurrency(data.creanceGlobal || 0), // This should come from API
        },
        {
          label: "Cout Transport",
          value: this.formatCurrency(data.coutTransport || 0),
        },
      ];
    },
    computedDetails() {
      const data = this.clientData || {};
      return [
        {
          label: "CODE :",
          value: this.formatCurrency(data.code || 0),
        },
        {
          label: "Nom du Client :",
          value: this.formatCurrency(data.name || 0),
        },

        {
          label: "Secteur d'activité :",
          value: `${this.formatNumber(data.secteur || 0)}`,
        },
        {
          label: "Représentant (e) :",
          value: `${this.formatNumber(data.representant || 0)}`,
        },
        {
          label: "Email :",
          value: `${this.formatNumber(data.email || 0)}`,
        },
        {
          label: "Mode de Paiement :",
          value: `${this.formatNumber(data.Modedepaiement || 0)}`,
        },
        {
          label: "Mode de Réglement :",
          value: `${this.formatNumber(data.Modereglement || 0)}`,
        },
        {
          label: "Téléphone :",
          value: `${this.formatNumber(data.phonenumber || 0)}`,
        },

        {
          label: "Date D'entree :",
          value: `${this.formatNumber(data.entrydate || 0)}`,
        },
        {
          label: "Suivi Par : ",
          value: `${this.formatNumber(data.suivipar || 0)}`,
        },
        {
          label: "Type de Garantie : ",
          value: `${this.formatNumber(data.typegarantie || 0)}`,
        },
        {
          label: "Plaphond Accordé (par Mois): ",
          value: `${this.formatNumber(data.plafond || 0)} dhs`,
        },

        {
          label: "Etat Financiere :",
          value: `${this.formatNumber(data.etatfinancier || 0)}`,
        },
        {
          label: "% du Facturation :",
          value: `${this.formatNumber(
            data.pourcentagefacturation * 100 || 0
          )} %`,
        },

        {
          label: "Unité de Vente :",
          value: `${this.formatNumber(data.uniteVente || 0)}`,
        },
        {
          label: "Type de Livraison",
          value: `${this.formatNumber(data.ISTRANSPORTEUR || 0)} `,
        },
      ];
    },

    computedLastStats() {
      const data = this.clientData || {};
      return [
        {
          label: "Localisation",
          value: this.formatCurrency(data.locations || 0),
        },
      ];
    },
    computedPrices() {
      const data = this.clientData || {};
      return [
        {
          label: "Prix Transport",
          value: this.formatCurrency(data.TransportPrice || 0),
        },

        {
          label: "Gabion",
          value: this.formatCurrency(data.TarificationProduits?.gabion || 0),
        },
        {
          label: "Filtre 0/250",
          value: this.formatCurrency(data.TarificationProduits?.filtre || 0),
        },
        {
          label: "Grain de Riz",
          value: this.formatCurrency(
            data.TarificationProduits?.grainderiz || 0
          ),
        },
        {
          label: "Gravette G1",
          value: this.formatCurrency(
            data.TarificationProduits?.gravetteg1 || 0
          ),
        },
        {
          label: "Gravette G2",
          value: this.formatCurrency(
            data.TarificationProduits?.gravetteg2 || 0
          ),
        },
        {
          label: "Sable Concassage 0-4",
          value: this.formatCurrency(
            data.TarificationProduits?.sableconcassage04 || 0
          ),
        },
        {
          label: "Sable Concassage 0-2",
          value: this.formatCurrency(
            data.TarificationProduits?.sableconcassage02 || 0
          ),
        },
        {
          label: "Tout Venant 0-31.5",
          value: this.formatCurrency(
            data.TarificationProduits?.toutvenant0315 || 0
          ),
        },
        {
          label: "Tout Venant 0-40",
          value: this.formatCurrency(
            data.TarificationProduits?.toutvenant040 || 0
          ),
        },
        {
          label: "Tout Venant 0-60",
          value: this.formatCurrency(
            data.TarificationProduits?.toutvenant060 || 0
          ),
        },
        {
          label: "Tout Venant 0-100",
          value: this.formatCurrency(
            data.TarificationProduits?.toutvenant0100 || 0
          ),
        },
        {
          label: "Stérile",
          value: this.formatCurrency(data.TarificationProduits?.sterile || 0),
        },
        {
          label: "Stérile Fin",
          value: this.formatCurrency(
            data.TarificationProduits?.sterilefin || 0
          ),
        },
        {
          label: "Cout Transport",
          value: this.formatCurrency(data.CTransport || 0),
        },
      ];
    },
  },

  watch: {
    clientData: {
      immediate: true,
      handler(newData) {
        if (newData) {
          this.updateClientDetails(newData);
        }
      },
    },
  },

  methods: {

    closeDialog() {
      this.dialogModel = false;
    },
    downloadPdf(ClientName) {
  const element = document.getElementById('pdf-content');
  const opt = {
          margin: [2, 2, 2, 2],
          filename: `Fiche_Client_${ClientName}.pdf`,
          image: { type: 'jpeg', quality: 0.98 },
          html2canvas: { 
            scale: 2,
            useCORS: true,
            letterRendering: true
          },
          jsPDF: { 
            unit: 'mm', 
            format: 'a4', 
            orientation: 'portrait' 
          }
        };

  html2pdf().set(opt).from(element).save();
},
      
    

    formatCurrency(value) {
      return `${value.toLocaleString()} `
    },
      
    formatNumber(value) {
      return value.toLocaleString();
    },


  

    updateClientDetails(data) {
      // Update client details based on new data
      this.details = [
        { label: "Company", value: data.company || "-" },
        { label: "Phone", value: data.phone || "-" },
        { label: "Email", value: data.email || "-" },
        { label: "Address", value: data.address || "-" },
        // Add more details as needed
      ];
    },

    getCategoryColor(category) {
      const colors = {
        Nobles: "primary",
        Graves: "secondary",
        Stérile: "success",
        default: "grey-darken-1",
      };
      return colors[category] || colors.default;
    
  },
}
};
</script>

<style scoped>
.border {
  border: 1px solid rgba(0, 0, 0, 0.12) !important;
}

.border-thin {
  border: thin solid rgba(0, 0, 0, 0.12) !important;
}

/* Transition effects */
.v-navigation-drawer {
  transition: transform 0.3s ease-in-out;
}

/* .v-sheet {
  transition: all 0.2s ease-in-out;
} */

.custom-nowrap {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis; /* Optional: adds '...' if text is too long */
}

.border {
  border: 1px solid rgba(0, 0, 0, 0.08) !important;
}

.v-navigation-drawer {
  transition: transform 0.3s ease-in-out;
}

.custom-nowrap {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.v-sheet {
  transition: background-color 0.2s ease;
}

/* .v-sheet:hover {
  background-color: rgb(250, 250, 250) !important;
} */
</style>
