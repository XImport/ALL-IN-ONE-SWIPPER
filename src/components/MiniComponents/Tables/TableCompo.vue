<template>
  <div class="card">
    <DataTable
      :value="DATA"
      paginator
      :rows="10"
      :rowsPerPageOptions="[5, 10, 50, 100]"
      resizableColumns
      columnResizeMode="expand"
      tableStyle="min-width: 100%"
      showGridlines
      :showFilterMatchModes="true"
      :show-filter-operator="false"
      responsiveLayout="scroll"
      v-model:filters="filters"
      filterDisplay="menu"
      :globalFilterFields="[
        'key1',
        'key2',
        'key3',
        'key4',
        'key5',
        'key6',
        'key7',
      ]"
    >
      <!-- <template #header>
        <div class="flex justify-center mx-auto">
          <span class="p-input-icon-left">
            <i class="pi pi-search" />
            <InputText
              v-model="filters.global.value"
              placeholder="Rechercher..."
            />
          </span>
        </div>
      </template> -->

      <Column
        field="code"
        :header="Headers.H1"
        style="max-width: 5% !important"
        :sortable="true"
        filterMatchMode="contains"
        class="font-weight-bold"
      >
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            @input="filterCallback()"
            placeholder="Rechercher..."
            class="p-column-filter"
          />
        </template>
      </Column>

      <Column
        field="name"
        :header="Headers.H2"
        style="width: 10%"
        :sortable="true"
        filterMatchMode="contains"
        class="font-weight-bold"
      >
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            @input="filterCallback()"
            placeholder="Rechercher..."
            class="p-column-filter"
            :style="{ backgroundColor: '#f0f0f0' }"
          />
        </template>
      </Column>

      <Column
        field="secteur"
        :header="Headers.H3"
        style="width: 15%"
        :sortable="true"
        filterMatchMode="contains"
      >
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            @input="filterCallback()"
            placeholder="Rechercher..."
            class="p-column-filter"
          />
        </template>
      </Column>

      <Column
        field="representant"
        :header="Headers.H4"
        style="width: 15%"
        :sortable="true"
        filterMatchMode="contains"
      >
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            @input="filterCallback()"
            placeholder="Rechercher..."
            class="p-column-filter"
          />
        </template>
      </Column>

      <Column
        field="email"
        :header="Headers.H5"
        style="width: 20%"
        :sortable="true"
        filterMatchMode="contains"
        class="text-blue"
      >
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            @input="filterCallback()"
            placeholder="Rechercher..."
            class="p-column-filter"
          />
        </template>
      </Column>

      <Column
        field="phonenumber"
        :header="Headers.H6"
        style="width: 10%"
        :sortable="true"
        filterMatchMode="contains"
      >
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            @input="filterCallback()"
            placeholder="Rechercher..."
            class="p-column-filter"
          />
        </template>
      </Column>

      <Column
        field="entrydate"
        :header="Headers.H7"
        style="width: 10%"
        :sortable="true"
        filterMatchMode="contains"
      >
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            @input="filterCallback()"
            placeholder="Rechercher..."
            class="p-column-filter"
          />
        </template>
      </Column>

      <Column header="Détail" style="width: 10%; margin-left: 50%">
        <template #body="slotProps">
          <v-btn
            style="margin-left: 20%"
            density="compact"
            color="blue"
            @click="viewDetails(slotProps.data)"
            icon="mdi-dots-horizontal-circle"
          ></v-btn>
        </template>
      </Column>
    </DataTable>
  </div>
</template>

<script>
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import InputText from "primevue/inputtext";
import { FilterMatchMode, FilterOperator } from "primevue/api";

export default {
  name: "ClientTable",
  props: ["DATA", "Headers"],
  components: {
    DataTable,
    Column,
    InputText,
  },
  data() {
    return {
      filters: {
        code: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }],
        },

        name: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }],
        },

        secteur: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }],
        },

        representant: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }],
        },

        email: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }],
        },

        phonenumber: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }],
        },

        entrydate: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }],
        },
      },
    };
  },
  methods: {
    viewDetails(rowData) {
      console.log("Viewing details for:", rowData.name);
      this.$store.commit("ChangeClientDialog");
      this.$store.commit("ChangeOneClientData", rowData);
    },
  },
};
</script>

<style scoped>
.card {
  padding: 1rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  background: #fff;
  margin-top: -2%;
}

.p-datatable :deep(th),
.p-datatable :deep(td) {
  text-align: center;
  vertical-align: middle;
}

.p-datatable-header {
  font-weight: bold;
  text-align: left;
  padding: 0.75rem 1rem;
}

.p-paginator {
  justify-content: flex-end;
  padding: 0.5rem;
}

.p-button {
  padding: 0.5rem 1rem;
  cursor: pointer;
}

:deep(.p-column-filter) {
  width: 100%;
}

.card[data-v-237ec1c5] {
  padding: 1rem;
  box-shadow: none;
  border-radius: 8px;
  background: #fff;
}

:deep(.p-datatable-header) {
  background: transparent;
  border: none;
  padding: 0 0 1rem 0;
}

:deep(.p-input-icon-left) {
  width: 100%;
  max-width: 300px;
}

:deep(.p-input-icon-left input) {
  width: 100%;
  padding-left: 2.5rem;
}

:deep(.p-column-filter-add-rule) {
  display: none !important;
}

.p-column-filter-overlay-menu .p-column-filter-add-rule {
  padding: 0.5rem 1rem;
  display: none !important;
}
/* ::v-deep .v-data-table-header {
  background-color: #dcdcdc;
}

::v-deep .p-datatable .p-datatable-thead > tr > th {
  background-color: #3b1c99;
  color: white;
}

::v-deep .p-datatable .p-datatable-thead > tr > th:hover {
  background-color: #3b1c99;
  color: white;
}

::v-deep .p-sortable-column-icon {
  color: white !important;
}

::v-deep .pi-filter-icon {
  color: white !important;
} */

::v-deep .p-column-title {
  font-weight: bold;
  color: black !important;
}
</style>
