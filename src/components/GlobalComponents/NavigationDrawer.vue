<template>
  <v-navigation-drawer floating permanent class="business-navigation-drawer">
    <!-- Logo/Brand Section -->
    <v-container class="brand-container pa-4">
      <v-img
        :width="160"
        aspect-ratio="1/1"
        cover
        src="https://i.imgur.com/98cmCfa.png"
        class="mx-auto brand-logo"
      ></v-img>
    </v-container>

    <v-divider class="mx-3 mb-4"></v-divider>

    <!-- Navigation Menu -->
    <div class="px-2">
      <v-btn
        v-for="(menu, index) in menuItems"
        :key="index"
        :class="[
          'nav-btn mb-2',
          { 'btn-active': activeItem === menu.title.toLowerCase() },
        ]"
        block
        variant="text"
        @click="activeItem = menu.title.toLowerCase()"
      >
        <template #prepend>
          <v-icon size="20" class="me-2 text-black">{{ menu.icon }}</v-icon>
        </template>
        <span class="nav-text">{{ menu.title }}</span>
      </v-btn>
    </div>

    <!-- Logout Button -->
    <template v-slot:append>
      <v-container class="pa-2" style="max-width: 90%">
        <v-btn
          v-for="(menu1, index) in menuControles"
          :key="index"
          :prepend-icon="menu1.icon"
          :class="[
            'nav-btn mb-2',
            { 'btn-active': activeItem === menu1.title.toLowerCase() },
          ]"
          block
          variant="text"
          @click="activeItem = menu1.title.toLowerCase()"
        >
          <template #prepend>
            <v-icon size="20" class="me-2 text-black">{{ menu1.icon }}</v-icon>
          </template>
          <span class="nav-text">{{ menu1.title }}</span>
        </v-btn>
        <!-- <v-btn block class="bg-primary">
          <v-icon color="white pr-2">mdi-logout</v-icon> Déconnexion
        </v-btn> -->
        <div style="min-height: 20px" />
      </v-container>
    </template>
  </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return {
      activeItem: "bilan analytique",
      menuItems: [
        {
          title: "Bilan Analytique",
          icon: "mdi-chart-bar",
        },
        {
          title: "Données Clients",
          icon: "mdi-database",
        },
        {
          title: "Suivi des créances",
          icon: "mdi-account-group",
        },
        {
          title: "Contrôle des seuils",
          icon: "mdi-chart-box",
        },
      ],
      menuControles: [
        {
          title: "Parametre",
          icon: "mdi-cog",
        },
        {
          title: "Déconecter",
          icon: "mdi-logout",
        },
      ],
    };
  },
};
</script>

<style scoped>
.business-navigation-drawer {
  background: linear-gradient(to bottom, #ffffff, #f8f9fa);
  border-radius: 0px 0px 20px 0px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  max-width: 280px;
  overflow: hidden;
}

.brand-container {
  background: linear-gradient(135deg, #f8f9fa, #ffffff);
  border-bottom-left-radius: 24px;
  border-bottom-right-radius: 24px;
}

.brand-logo {
  transition: transform 0.3s ease;
}

.brand-logo:hover {
  transform: scale(1.05);
}

.nav-btn {
  height: 44px !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-weight: 600 !important;
  border-radius: 8px !important;
  justify-content: flex-start !important;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;

  text-align: left;
}

.nav-btn::before {
  content: "";
  position: absolute;
  left: -4px;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 60%;
  background-color: #1976d2;
  border-radius: 0 4px 4px 0;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.btn-active {
  background: linear-gradient(
    90deg,
    rgba(25, 118, 210, 0.12),
    rgba(25, 118, 210, 0.05)
  ) !important;
  color: #1976d2 !important;
  font-weight: 600 !important;
}

.btn-active::before {
  opacity: 1;
}

.btn-active :deep(.v-icon) {
  color: #1976d2 !important;
}

.nav-btn:hover {
  background-color: rgba(25, 118, 210, 0.04);
  transform: translateX(4px);
}

.nav-text {
  font-size: 0.925rem;
  white-space: nowrap;

  overflow: hidden;
  text-overflow: ellipsis;
}

:deep(.v-icon) {
  color: #64748b;
  transition: color 0.3s ease;
}

/* Responsive adjustments */
@media (max-width: 960px) {
  .business-navigation-drawer {
    max-width: 240px;
  }

  .brand-container {
    padding: 16px !important;
  }

  .nav-text {
    font-size: 0.875rem;
  }
}
</style>
