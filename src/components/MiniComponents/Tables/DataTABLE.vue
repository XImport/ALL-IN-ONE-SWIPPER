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
      :items="DATA"
      :items-length="totalItems"
      :loading="loading"
      item-value="name"
      @update:options="loadItems"
      hide-default-footer
      class="custom-header-table"
    >
      <template v-slot:body="{ items }">
        <tr v-for="(item, index) in items" :key="index">
          <td class="font-weight-bold">{{ item.Key1.toLocaleString() }}</td>
          <td class="font-weight-bold">{{ item.Key2.toLocaleString() }}</td>
          <td class="font-weight-bold">{{ item.Key3.toLocaleString() }}</td>

          <td
            v-if="reverse"
            class="font-weight-bold"
            :style="getPercentageColor(item.Key2, item.Key3)"
          >
            {{ ((item.Key2 / item.Key3) * 100).toFixed(2) }}%
          </td>

          <td
            v-if="!reverse"
            class="font-weight-bold"
            :style="getPercentageColor(item.Key3, item.Key2)"
          >
            {{ ((item.Key3 / item.Key2).toFixed(2) * 100).toFixed(2) }}%
          </td>
        </tr>
      </template>
    </v-data-table-server>
  </div>
</template>
<script>
export default {
  props: {
    Headers: {
      type: Array,
      required: true,
    },
    DATA: {
      type: Array,
      required: true,
    },
    DATATABLETITLE: {
      type: String,
      required: true,
    },
    reverse: {
      type: Boolean,
      default: false,
    },
    TABLEICON: {
      type: String,
      required: true,
    },
    TABLECOLORICON: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      itemsPerPage: 5,
      serverItems: [],
      loading: true,
      totalItems: 0,
      currentPage: 1,
      localData: [...this.DATA],
      currentSort: [],
    };
  },

  computed: {
    // Process all items with formatting
    processedData() {
      return this.DATA.map((item) => ({
        ...item,
        Key2Formatted: this.formatNumber(item.Key2),
        Key3Formatted: this.formatNumber(item.Key3),
        Key4: this.calculateKey4(item.Key2, item.Key3),
      }));
    },

    // Get current page items
    processedItems() {
      return this.serverItems.map((item) => ({
        ...item,
        Key2Formatted: this.formatNumber(item.Key2),
        Key3Formatted: this.formatNumber(item.Key3),
        Key4: this.calculateKey4(item.Key2, item.Key3),
      }));
    },
  },

  methods: {
    getPercentageColor(value1, value2) {
      const percentage = (value1 / value2) * 100;
      return percentage < 70 ? { color: "orange" } : { color: "green" };
    },
    formatNumber(value) {
      return value.toLocaleString();
    },

    calculateKey4(key2, key3) {
      const percentage = this.reverse
        ? (key2 / key3) * 100
        : (key3 / key2) * 100;
      return `${percentage.toFixed(2)} %`;
    },

    refreshData() {
      this.loadItems({
        page: this.currentPage,
        itemsPerPage: this.itemsPerPage,
        sortBy: this.currentSort,
      });
    },

    async loadItems({ page, itemsPerPage, sortBy }) {
      this.loading = true;
      this.currentPage = page;
      this.currentSort = sortBy;

      try {
        const { items, total } = await this.fetchItems({
          page,
          itemsPerPage,
          sortBy,
        });
        this.serverItems = items;
        this.totalItems = total;
      } catch (error) {
        console.error("Error loading items:", error);
      } finally {
        this.loading = false;
      }
    },

    async fetchItems({ page, itemsPerPage, sortBy }) {
      return new Promise((resolve) => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage;
          const end = start + itemsPerPage;
          const items = [...this.processedData];

          if (sortBy && sortBy.length) {
            const { key, order } = sortBy[0];
            items.sort((a, b) => {
              // Remove formatting for numeric comparison
              const aValue = this.getNumericValue(a[key]);
              const bValue = this.getNumericValue(b[key]);
              return order === "desc" ? bValue - aValue : aValue - bValue;
            });
          }

          resolve({
            items: items.slice(start, end),
            total: items.length,
          });
        }, 200);
      });
    },

    getNumericValue(value) {
      if (typeof value === "string" && value.includes("%")) {
        return parseFloat(value);
      }
      return typeof value === "string"
        ? parseFloat(value.replace(/,/g, ""))
        : value;
    },

    getPercentageClass(value) {
      const percentage = parseFloat(value);
      return percentage >= 80 ? "text-green" : "text-orange";
    },
  },
};
</script>

<style>
/* Style remains unchanged */
.custom-header-table :deep(.v-data-table-header),
.custom-header-table :deep(thead),
.custom-header-table :deep(thead tr),
.custom-header-table :deep(thead th),
.custom-header-table :deep(.v-data-table__header) {
  background-color: #2196f3 !important;
  color: white !important;
}

.custom-header-table :deep(th),
.custom-header-table :deep(.v-data-table-header-cell) {
  color: white !important;
}

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

.text-green {
  color: #4caf50 !important;
  font-weight: bold;
}

.text-orange {
  color: #ff9800 !important;
  font-weight: bold;
}
</style>
