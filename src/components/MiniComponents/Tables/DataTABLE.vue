<template>
  <div>
    <div>
      <h3 class="text-center pb-6 text-decoration-underline">
        <v-icon :color="TABLECOLORICON">{{ TABLEICON }}</v-icon>
        {{ DATATABLETITLE }}
        <v-tooltip text="Exporter Vers Excel" location="top" activator="parent">
          <template v-slot:activator="{ props }">
            <v-btn icon compact size="20" class="ml-2" v-bind="props">
              <v-img
                src="https://static-00.iconduck.com/assets.00/ms-excel-icon-2048x2026-nws24wyy.png"
                width="25"
                class=""
                style="display: inline-block; vertical-align: middle"
              ></v-img>
            </v-btn>
          </template>
        </v-tooltip>
      </h3>
    </div>
    <v-data-table-server
      v-model:items-per-page="itemsPerPage"
      :headers="Headers"
      :items="serverItems"
      :items-length="totalItems"
      :loading="loading"
      item-value="name"
      @update:options="loadItems"
      hide-default-footer
      class="custom-header-table"
    >
      <template v-slot:item.Key2="{ item }">
        <!-- Display the localized Key2 value -->
        {{ item.Key2Formatted }}
      </template>
      <template v-slot:item.Key3="{ item }">
        <!-- Display the localized Key3 value -->
        {{ item.Key3Formatted }}
      </template>
      <template v-slot:item.Key4="{ item }">
        <span :class="getPercentageClass(item.Key4)">{{ item.Key4 }}</span>
      </template>
    </v-data-table-server>
  </div>
</template>

<script>
export default {
  props: [
    "Headers",
    "DATA",
    "DATATABLETITLE",
    "reverse",
    "TABLEICON",
    "TABLECOLORICON",
  ],
  data() {
    return {
      itemsPerPage: 5,

      serverItems: [],
      loading: true,
      totalItems: 0,
    };
  },
  methods: {
    loadItems({ page, itemsPerPage, sortBy }) {
      this.loading = true;
      this.fakeApiFetch({ page, itemsPerPage, sortBy }).then(
        ({ items, total }) => {
          this.serverItems = items;
          this.totalItems = total;
          this.loading = false;
        }
      );
    },
    fakeApiFetch({ page, itemsPerPage, sortBy }) {
      // Loop through each item in DATA to format Key2 and Key3 and calculate Key4
      this.DATA.forEach((item) => {
        // Format Key2 and Key3 using toLocaleString for display
        item.Key2Formatted = item.Key2.toLocaleString();
        item.Key3Formatted = item.Key3.toLocaleString();

        // Dynamically calculate Key4 using the raw numeric values of Key2 and Key3
        if (this.reverse) {
          item.Key4 = ((item.Key2 / item.Key3) * 100).toFixed(2) + " %";
        } else {
          item.Key4 = ((item.Key3 / item.Key2) * 100).toFixed(2) + " %";
        }
      });

      return new Promise((resolve) => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage;
          const end = start + itemsPerPage;
          const items = this.DATA.slice();

          // Sort logic if needed
          if (sortBy.length) {
            const sortKey = sortBy[0].key;
            const sortOrder = sortBy[0].order;
            items.sort((a, b) => {
              const aValue = a[sortKey];
              const bValue = b[sortKey];
              return sortOrder === "desc" ? bValue - aValue : aValue - bValue;
            });
          }

          const paginated = items.slice(start, end);
          resolve({ items: paginated, total: items.length });
        }, 500);
      });
    },

    getPercentageClass(value) {
      // Extract number from string and convert to float
      const percentage = parseFloat(value);
      return percentage >= 80 ? "text-green" : "text-orange"; // Adjusted logic for 80% threshold
    },
  },
};
</script>

<style>
/* Target all possible header selectors to ensure override */
.custom-header-table :deep(.v-data-table-header),
.custom-header-table :deep(thead),
.custom-header-table :deep(thead tr),
.custom-header-table :deep(thead th),
.custom-header-table :deep(.v-data-table__header) {
  background-color: #2196f3 !important;
  color: white !important;
}

/* Ensure text color remains white */
.custom-header-table :deep(th),
.custom-header-table :deep(.v-data-table-header-cell) {
  color: white !important;
}

/* Handle sorting icons */
.custom-header-table :deep(.v-data-table-header i),
.custom-header-table :deep(.v-data-table-header .v-icon) {
  color: white !important;
}

.v-data-table__thead {
  background-color: #3b1c99 !important;
  color: white !important;
}

.v-data-table-column--align-start {
  font-weight: bold !important;
}

/* Percentage colors */
.text-green {
  color: #4caf50 !important;
  font-weight: bold;
}

.text-orange {
  color: #ff9800 !important;
  font-weight: bold;
}
</style>
