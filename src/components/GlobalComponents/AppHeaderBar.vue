<template>
  <div>
    <v-container fluid class="px-0 pb-2">
      <v-row no-gutters align="center" class="px-4">
        <!-- Title Section -->
        <v-col cols="auto" class="mr-auto" style="margin-left: 20%">
          <h2 class="text-decoration-underline">
            <v-icon class="pr-2" color="green">mdi-chart-tree</v-icon>Bilan
            Analytique
            <v-tooltip
              text="Exporter Vers Excel"
              location="top"
              activator="parent"
            >
              <template v-slot:activator="{ props }">
                <v-btn icon compact size="25" class="ml-2" v-bind="props">
                  <v-img
                    src="https://static-00.iconduck.com/assets.00/ms-excel-icon-2048x2026-nws24wyy.png"
                    width="25"
                    class=""
                    style="display: inline-block; vertical-align: middle"
                  ></v-img>
                </v-btn>
              </template>
            </v-tooltip>
          </h2>
        </v-col>

        <!-- Date Pickers and Theme Toggle Section -->
        <v-col
          cols="auto"
          class="d-flex align-center mx-4"
          style="margin-right: 10% !important"
        >
          <div class="d-flex align-center gap-4">
            <VueDatePicker
              class="datepicker"
              placeholder="Date de début"
              v-model="startdate"
              :format="format1"
            />
            <VueDatePicker
              class="datepicker"
              placeholder="Date de fin"
              v-model="enddate"
              :format="format2"
            />
            <v-tooltip
              text="Analyser les données"
              location="top"
              activator="parent"
            >
              <template v-slot:activator="{ props }">
                <v-btn icon compact size="35" class="" v-bind="props">
                  <v-img
                    src="https://static-00.iconduck.com/assets.00/go-icon-2048x769-18k4edx0.png"
                    width="35"
                    class=""
                    style="display: inline-block; vertical-align: middle"
                  ></v-img>
                </v-btn>
              </template>
            </v-tooltip>
            <div class="theme-switch-wrapper">
              <button
                class="theme-switch"
                :class="{ dark: isDark }"
                @click="toggleTheme"
              >
                <div class="icons">
                  <span class="sun">
                    <v-icon>mdi-white-balance-sunny</v-icon>
                  </span>
                  <span class="moon">
                    <v-icon>mdi-moon-full</v-icon>
                  </span>
                </div>
                <div class="slider" :class="{ dark: isDark }"></div>
              </button>
            </div>
          </div>
        </v-col>

        <!-- User Profile Section -->
        <v-col cols="auto" style="margin-right: 5% !important">
          <v-list class="pa-0">
            <v-list-item
              prepend-avatar="https://cdn-icons-png.flaticon.com/512/219/219986.png"
              subtitle="Hamza.nouinou@ttsud.ma"
              title="Hamza Nouinou"
            />
          </v-list>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

export default {
  name: "BilanAnalytique",
  components: { VueDatePicker },
  data() {
    return {
      isDark: false,
      startdate: "",
      enddate: "",
      date: new Date(), // Date is initialized as the current date
    };
  },
  methods: {
    toggleTheme() {
      this.isDark = !this.isDark;
      this.$vuetify.theme.dark = this.isDark;
    },
    format1(date) {
      const day = date.getDate();
      const month = date.getMonth() + 1;
      const year = date.getFullYear();
      return ` ${day}/${month}/${year}`;
    },
    format2(date) {
      const day = date.getDate();
      const month = date.getMonth() + 1;
      const year = date.getFullYear();
      return ` ${day}/${month}/${year}`;
    },
  },
};
</script>

<style scoped>
.gap-4 {
  gap: 1rem;
}

.datepicker {
  width: 170px;
}

.theme-switch-wrapper {
  margin-left: 1rem;
}

.theme-switch {
  position: relative;
  width: 64px;
  height: 32px;
  background-color: #e9ecef;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  padding: 0;
  overflow: hidden;
}

.theme-switch.dark {
  background-color: #484848;
}

.icons {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  padding: 0 6px;
  position: relative;
  z-index: 1;
}

.sun,
.moon {
  font-size: 16px;
  line-height: 1;
  color: #000000;
}

.slider {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 28px;
  height: 28px;
  background-color: white;
  border-radius: 50%;
  transition: transform 0.3s ease;
}

.slider.dark {
  transform: translateX(32px);
  background-color: #ffffff;
}

/* Responsive adjustments */
@media (max-width: 959px) {
  .datepicker {
    width: 140px;
  }
  .theme-switch-wrapper {
    margin-left: 0.5rem;
  }
}

@media (max-width: 599px) {
  .datepicker {
    width: 120px;
  }
  .v-container {
    padding: 0px;
  }
}

.v-btn {
  box-shadow: none !important;
}
</style>
