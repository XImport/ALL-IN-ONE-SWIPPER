<template>
  <v-dialog v-model="ClientDialog" width="950" persistent>
    <v-card min-width="950px" class="mx-auto rounded-lg">
      <!-- Header -->
      <v-card-title class="d-flex align-center pa-6 bg-grey-lighten-4">
        <v-avatar size="48" class="mr-4">
          <v-avatar color="brown" size="large">
            <span class="text-h5">{{
              ClientDialogDATA?.name?.slice(0, 3) || "NA"
            }}</span>
          </v-avatar>
        </v-avatar>
        <div class="flex-grow-1">
          <div class="d-flex align-center mb-1">
            <span class="text-h5 font-weight-medium">{{
              ClientDialogDATA.name
            }}</span>
          </div>
          <div class="d-flex align-center">
            <v-icon size="small" class="mr-2">mdi-wrench</v-icon>
            <v-chip
              size="small"
              color="orange-lighten-1"
              class="mr-2 font-weight-medium"
            >
              Secteur D'activité
            </v-chip>
            <v-chip
              size="small"
              color="light-green-lighten-1"
              class="font-weight-medium"
            >
              {{ ClientDialogDATA.secteur }}
            </v-chip>
          </div>
        </div>
        <v-btn
          icon="mdi-close"
          variant="text"
          @click="closeDialog()"
          class="ml-2"
        ></v-btn>
      </v-card-title>

      <!-- Stats -->
      <v-card-text class="pa-6">
        <v-row class="d-flex justify-space-between align-center text-center">
          <v-col cols="3">
            <div class="text-h6 font-weight-bold mb-1">
              {{ ClientDialogDATA.caBrut?.toLocaleString() || "NA" }}
            </div>
            <div class="text-caption text-grey-darken-1">CA BRUT</div>
          </v-col>
          <v-col cols="3">
            <div class="text-h6 font-weight-bold mb-1">
              {{ ClientDialogDATA.volume?.toLocaleString() || "NA" }}
            </div>
            <div class="text-caption text-grey-darken-1">VOLUME LIVREE</div>
          </v-col>
          <v-col cols="3">
            <div class="text-h6 font-weight-bold mb-1">
              {{ (421214.21).toLocaleString() }}
            </div>
            <div class="text-caption text-grey-darken-1">Créance Client</div>
          </v-col>
          <v-col cols="3">
            <div class="text-h6 font-weight-bold mb-1">
              {{ ClientDialogDATA.coutTransport?.toLocaleString() || "NA" }}
            </div>
            <div class="text-caption text-grey-darken-1">Cout Transport</div>
          </v-col>
        </v-row>
      </v-card-text>

      <!-- Customer Details -->
      <v-card-text class="pa-6">
        <h3 class="text-h6 font-weight-medium mb-6">Détails du client</h3>
        <v-row>
          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Répresentant
              </div>
              <div class="text-body-1">{{ ClientDialogDATA.representant }}</div>
            </div>
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Phone Number
              </div>
              <div class="text-body-1">{{ ClientDialogDATA.phonenumber }}</div>
            </div>
            <div>
              <div class="text-caption text-grey-darken-1 mb-1">Email</div>
              <div class="text-body-1">
                {{ ClientDialogDATA.email }}
              </div>
            </div>
          </v-col>

          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Localisation
              </div>
              <div class="text-body-1">{{ ClientDialogDATA.location }}</div>
            </div>
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">Suivi Par</div>
              <div class="text-body-1">
                <v-chip color="green">{{ ClientDialogDATA.suivipar }}</v-chip>
              </div>
            </div>
            <div>
              <div class="text-caption text-grey-darken-1 mb-1">
                Date D'emchement
              </div>
              <div class="text-body-1">{{ ClientDialogDATA.entrydate }}</div>
            </div>
          </v-col>
          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Type de Garantie
              </div>
              <div class="text-body-1">{{ ClientDialogDATA.typegarantie }}</div>
            </div>

            <div></div>
          </v-col>
          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Pourcentange du Facturation
              </div>
              <div class="text-body-1 font-weight-bold">
                {{
                  (
                    ClientDialogDATA.pourcentagefacturation * 100
                  ).toLocaleString()
                }}
                %
              </div>
            </div>

            <div></div>
          </v-col>
          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Mode de Réglement
              </div>
              <div class="text-body-1">
                <v-chip color="green">{{
                  ClientDialogDATA.Modereglement
                }}</v-chip>
              </div>
            </div>

            <div></div>
          </v-col>
          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Unite de Vente
              </div>
              <div class="text-body-1">{{ ClientDialogDATA.uniteVente }}</div>
            </div>

            <div></div>
          </v-col>
          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Plafond Mensuelle
              </div>
              <div class="text-body-1">
                {{
                  ClientDialogDATA.plafond?.toLocaleString() ||
                  ClientDialogDATA.plafond
                }}
              </div>
            </div>

            <div></div>
          </v-col>
          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Etat Financiere du Client
              </div>
              <div class="text-body-1">
                <v-chip color="orange">{{
                  ClientDialogDATA.etatfinancier
                }}</v-chip>
              </div>
            </div>

            <div></div>
          </v-col>
        </v-row>
      </v-card-text>

      <v-card-text class="pa-4">
        <!-- Header Section -->
        <div class="d-flex justify-space-between align-center mb-6">
          <h3 class="text-h6 primary--text">Tarification des Produits</h3>
        </div>

        <!-- Product Cards Grid -->
        <v-row>
          <!-- Individual Product Cards -->
          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'GRAIN DE RIZ',
                price: ClientDialogDATA.TarificationProduits.grainderiz,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'GRAVETTE G1',
                price: ClientDialogDATA.TarificationProduits.gravetteg1,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'GRAVETTE G2',
                price: ClientDialogDATA.TarificationProduits.gravetteg2,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'SABLE CONCASSAGE 0-4',
                price: ClientDialogDATA.TarificationProduits.sableconcassage04,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'SABLE CONCASSAGE 0-2',
                price: ClientDialogDATA.TarificationProduits.sableconcassage02,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'TOUT VENANT 0-31,5',
                price: ClientDialogDATA.TarificationProduits.toutvenant0315,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'TOUT VENANT 0-40',
                price: ClientDialogDATA.TarificationProduits.toutvenant040,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'TOUT VENANT 0-60',
                price: ClientDialogDATA.TarificationProduits.toutvenant060,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'TOUT VENANT 0-100',
                price: ClientDialogDATA.TarificationProduits.toutvenant0100,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'STERILE',
                price: ClientDialogDATA.TarificationProduits.sterile,
              }"
            />
          </v-col>

          <v-col cols="12" sm="6" lg="4">
            <ProductPrice
              :product="{
                productname: 'STERILE FIN',
                price: ClientDialogDATA.TarificationProduits.sterilefin,
              }"
            />
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import ProductPrice from "./ProductPrice.vue";
export default {
  components: { ProductPrice },
  computed: {
    ClientDialog() {
      return this.$store.getters.GetClientDialog;
    },
    ClientDialogDATA() {
      return this.$store.getters.GetOneClientData;
    },
    // DetectColorByCatégorie(catégorie) {
    //   if (catégorie == "Nobles") {
    //     return "text-green";
    //   }
    //   if (catégorie == "Graves") {
    //     return "text-grey";
    //   }
    //   return "text-orange";
    // },
  },
  methods: {
    ChangeDialogState() {
      this.$store.commit("ChangeClientDialog");
    },
    closeDialog() {
      this.$store.commit("ChangeClientDialog");
    },
    DetectColorByCatégorie(catégorie) {
      switch (catégorie) {
        case "Nobles":
          return "text-green";
        case "Graves":
          return "text-orange";
        case "Stérile":
          return "text-red";
        default:
          return "text-grey-darken-1";
      }
    },

    getCategoryColor(category) {
      const colors = {
        Nobles: "primary",
        Graves: "secondary",
        Stérile: "success",
        // Add more categories as needed
        default: "grey-darken-1",
      };
      return colors[category] || colors.default;
    },
    getCategoryTextColor(category) {
      const colors = {
        Nobles: "text-green",
        Graves: "text-orange",
        Stérile: "text-red",
        // Add more categories as needed
        default: "text-grey-darken-1",
      };
      return colors[category] || colors.default;
    },
  },
  data() {
    return {
      hover: false,
      shortcuts: [
        { action: "Ouvrir les Paramètres", key: "Ctrl + S" },
        { action: "Actualiser", key: "Ctrl + R" },
      ],
      customer: {
        name: "Santi Cazorla",
        studio: "Fikri Studio",
        lastActivity: "5 days ago",
        company: "Microsoft",
        tickets: 16,
        overdueTickets: 4,
        avgResponseTime: "25:00",
        totalResponseTime: "1:32:08",
        source: "Contact us form",
        phone: "(209) 555-0104",
        emails: ["hello@santi.com", "ask.me@santi.com"],
        location: "United Kingdom, Europe",
        languages: ["English", "Italian"],
        timezone: "UTC+07:00",
        activeTicket: {
          id: "TC-196",
          title: "Defective Item Received",
          requestDate: "03/18/2023, 09:00AM",
        },
      },
      Produits: [
        {
          id: 1,
          productname: "Grain de Riz",
          price: 28,
          catégorie: "Graves",
          codeProduct: "Grz",
        },
        {
          id: 2,
          productname: "Gravette G1",
          price: 40,
          catégorie: "Nobles",
          codeProduct: "Gr1",
        },
        {
          id: 3,
          productname: "Gravette G2",
          price: 40,
          catégorie: "Nobles",
          codeProduct: "Gr2",
        },
        {
          id: 4,
          productname: "Sable Concassage 0-4",
          price: 40,
          catégorie: "Nobles",
          codeProduct: "Sable 0-4",
        },
        {
          id: 5,
          productname: "Tout Venant 0-31.5",
          price: 28,
          catégorie: "Graves",
          codeProduct: "Tv0315",
        },
        {
          id: 6,
          productname: "Tout Venant 0-40",
          price: 28,
          catégorie: "Graves",
          codeProduct: "Tv040",
        },
        {
          id: 7,
          productname: "Tout Venant 0-60",
          price: 28,
          catégorie: "Graves",
          codeProduct: "Tv060",
        },
        {
          id: 8,
          productname: "Tout Venant 0-100",
          price: 28,
          catégorie: "Graves",
          codeProduct: "Tv0100",
        },
        {
          id: 9,
          productname: "Stérile",
          price: 15,
          catégorie: "Stérile",
          codeProduct: "Stérile",
        },
        {
          id: 10,
          productname: "Stérile Fin",
          price: 25,
          catégorie: "Stérile",
          codeProduct: "StérileFin",
        },
      ],
    };
  },
};
</script>

<style>
.v-card-text {
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
}
.v-card-text:last-child {
  border-bottom: none;
}

.v-card.on-hover {
  transform: translateY(-4px);
  transition: all 0.3s ease-in-out;
}

.v-card {
  transition: all 0.3s ease-in-out;
}

.bg-grey-lighten-4 {
  background-color: rgb(243, 246, 249) !important;
}
</style>
