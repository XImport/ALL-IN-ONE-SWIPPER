import { createMemoryHistory, createRouter } from 'vue-router';

import BilanAnalytiqueView from "../views/BilanAnalytiqueView.vue";
import ControledesSeuilsView from "../views/ControledesSeuilsView.vue";
import DonnesClientsView from "../views/DonnesClientsView.vue";
import SuividesCreancesView from "../views/SuividesCreancesView.vue";

// Define routes
export const routes = [
  { path: '/', component: BilanAnalytiqueView },
  { path: '/controleseuils', component: ControledesSeuilsView },
  { path: '/donnesclients', component: DonnesClientsView },
  { path: '/suividescreances', component: SuividesCreancesView },
];

// Create router instance
export const router = createRouter({
  history: createMemoryHistory(),
  routes,
});

export default router;