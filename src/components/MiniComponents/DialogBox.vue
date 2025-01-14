<template>
  <v-dialog v-model="Dialog" width="600" persistent>
    <v-card class="rounded-lg">
      <v-card-title class="bg-indigo-darken-3 py-4">
        <v-icon icon="mdi-information-box" class="me-2" />
        <span class="text-p">Paramètres Rapides & Raccourcis : </span>
        <v-spacer></v-spacer>
      </v-card-title>

      <v-card-text class="pa-4">
        <v-table density="comfortable">
          <thead>
            <tr>
              <th class="text-subtitle-1 font-weight-bold">Action</th>
              <th class="text-subtitle-1 font-weight-bold">Raccourci</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(shortcut, index) in shortcuts" :key="index">
              <td>{{ shortcut.action }}</td>
              <td>
                <v-chip
                  size="small"
                  variant="flat"
                  class="font-weight-medium bg-indigo-darken-3"
                >
                  {{ shortcut.key }}
                </v-chip>
              </td>
            </tr>
          </tbody>
        </v-table>
      </v-card-text>

      <v-card-actions class="pa-2">
        <v-container style="max-width: 70%; margin-right: 15%">
          <v-btn
            variant="flat"
            class="bg-indigo-darken-3"
            block
            prepend-icon="mdi-window-close"
            @click="ChangeDialogState()"
          >
            Fermer
          </v-btn>
        </v-container>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  computed: {
    Dialog() {
      return this.$store.getters.GetDialogState;
    },
  },
  methods: {
    ChangeDialogState() {
      this.$store.commit("ChangeDialogState");
    },
  },
  data() {
    return {
      shortcuts: [
        { action: "Ouvrir les Paramètres", key: "Ctrl + S" },
        { action: "Actualiser", key: "Ctrl + R" },
      ],
    };
  },
};
</script>

<style></style>
