<template>
  <v-dialog v-model="ClientDialog" width="950" persistent>
    <v-card min-width="950px" class="mx-auto rounded-lg">
      <!-- Header -->
      <v-card-title class="d-flex align-center pa-6 bg-grey-lighten-4">
        <v-avatar size="48" class="mr-4">
          <v-img
            src="https://kalsisolar.com/images/543955831.jpg"
            alt="Customer avatar"
            class="rounded-lg"
          ></v-img>
        </v-avatar>
        <div class="flex-grow-1">
          <div class="d-flex align-center mb-1">
            <span class="text-h5 font-weight-medium">{{
              ClientDialogDATA.key2
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
              {{ ClientDialogDATA.key3 }}
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
              {{ (125458.32).toLocaleString() }}
            </div>
            <div class="text-caption text-grey-darken-1">CA BRUT</div>
          </v-col>
          <v-col cols="3">
            <div class="text-h6 font-weight-bold mb-1">
              {{ (15458.32).toLocaleString() }}
            </div>
            <div class="text-caption text-grey-darken-1">VOLUME LIVREE</div>
          </v-col>
          <v-col cols="3">
            <div class="text-h6 font-weight-bold mb-1">Départ</div>
            <div class="text-caption text-grey-darken-1">MODE LIVRAISON</div>
          </v-col>
          <v-col cols="3">
            <div class="text-h6 font-weight-bold mb-1">Tonne</div>
            <div class="text-caption text-grey-darken-1">UNITE DE VENTE</div>
          </v-col>
        </v-row>
      </v-card-text>

      <!-- Customer Details -->
      <v-card-text class="pa-6">
        <h3 class="text-h6 font-weight-medium mb-6">Customer Details</h3>
        <v-row>
          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">Source</div>
              <div class="text-body-1">{{ customer.source }}</div>
            </div>
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Phone Number
              </div>
              <div class="text-body-1">{{ customer.phone }}</div>
            </div>
            <div>
              <div class="text-caption text-grey-darken-1 mb-1">Email</div>
              <div
                v-for="email in customer.emails"
                :key="email"
                class="text-body-1"
              >
                {{ email }}
              </div>
            </div>
          </v-col>
          <v-col cols="6">
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">Location</div>
              <div class="text-body-1">{{ customer.location }}</div>
            </div>
            <div class="mb-6">
              <div class="text-caption text-grey-darken-1 mb-1">
                Language Spoken
              </div>
              <div class="text-body-1">{{ customer.languages.join(", ") }}</div>
            </div>
            <div>
              <div class="text-caption text-grey-darken-1 mb-1">Timezone</div>
              <div class="text-body-1">{{ customer.timezone }}</div>
            </div>
          </v-col>
        </v-row>
      </v-card-text>

      <!-- Active Ticket -->
      <v-card-text class="pa-6">
        <div class="d-flex justify-space-between align-center mb-6">
          <h3 class="text-h6 font-weight-medium">Active Ticket</h3>
          <v-btn
            color="primary"
            variant="text"
            class="text-none"
            prepend-icon="mdi-ticket"
          >
            View More Tickets
          </v-btn>
        </div>
        <v-card variant="outlined" class="rounded-lg">
          <v-card-text class="pa-4">
            <div class="d-flex align-center mb-4">
              <span class="text-subtitle-1 font-weight-medium">
                #{{ customer.activeTicket.id }}
              </span>
              <span class="ml-2 text-body-1">{{
                customer.activeTicket.title
              }}</span>
              <v-chip
                color="primary"
                size="small"
                class="ml-auto font-weight-medium"
              >
                Open
              </v-chip>
            </div>
            <v-row>
              <v-col cols="4">
                <div class="text-caption text-grey-darken-1 mb-1">
                  Ticket Type
                </div>
                <div class="d-flex align-center">
                  <v-icon size="small" color="grey-darken-1" class="mr-2">
                    mdi-help-circle-outline
                  </v-icon>
                  <span class="text-body-2">Question</span>
                </div>
              </v-col>
              <v-col cols="4">
                <div class="text-caption text-grey-darken-1 mb-1">Priority</div>
                <v-chip
                  size="small"
                  color="warning"
                  variant="flat"
                  class="font-weight-medium"
                >
                  Medium
                </v-chip>
              </v-col>
              <v-col cols="4">
                <div class="text-caption text-grey-darken-1 mb-1">
                  Request Date
                </div>
                <div class="text-body-2">
                  {{ customer.activeTicket.requestDate }}
                </div>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  computed: {
    ClientDialog() {
      return this.$store.getters.GetClientDialog;
    },
    ClientDialogDATA() {
      return this.$store.getters.GetOneClientData;
    },
  },
  methods: {
    ChangeDialogState() {
      this.$store.commit("ChangeClientDialog");
    },
    closeDialog() {
      this.$store.commit("ChangeClientDialog");
    },
  },
  data() {
    return {
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
</style>
