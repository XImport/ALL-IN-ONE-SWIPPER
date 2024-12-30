<template>
  <div class="ag-theme-alpine">
    <ag-grid-vue
      :rowData="rowData"
      :columnDefs="colDefs"
      style="height: 500px; width: 100%"
      :modules="modules"
      :defaultColDef="defaultColDef"
      :enableRangeSelection="true"
      :animateRows="true"
      :rowSelection="rowSelection"
      :pagination="true"
      :paginationPageSize="paginationPageSize"
      @grid-ready="onGridReady"
      @cell-clicked="onCellClicked"
      @selection-changed="onSelectionChanged"
      :sideBar="sideBar"
      :rowGroupPanelShow="rowGroupPanelShow"
      :statusBar="statusBar"
    >
    </ag-grid-vue>
  </div>
</template>

<script>
import { ref } from "vue";
import { AgGridVue } from "ag-grid-vue3";
import { ClientSideRowModelModule } from "ag-grid-community";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";

export default {
  name: "App",
  components: {
    AgGridVue,
  },
  setup() {
    const gridApi = ref(null);
    const gridColumnApi = ref(null);
    const modules = ref([ClientSideRowModelModule]);

    // Row Data
    const rowData = ref([
      { make: "Tesla", model: "Model Y", price: 64950, electric: true },
      { make: "Ford", model: "F-Series", price: 33850, electric: false },
      { make: "Toyota", model: "Corolla", price: 29600, electric: false },
    ]);

    // Column Definitions with advanced features
    const colDefs = ref([
      {
        field: "make",
        sortable: true,
        filter: true,
        checkboxSelection: true,
        headerCheckboxSelection: true,
        pinned: "left",
      },
      {
        field: "model",
        sortable: true,
        filter: true,
        editable: true,
      },
      {
        field: "price",
        sortable: true,
        filter: "agNumberColumnFilter",
        editable: true,
        valueFormatter: (params) => {
          return "$ " + params.value.toLocaleString();
        },
      },
      {
        field: "electric",
        sortable: true,
        filter: true,
        cellRenderer: (params) => {
          return params.value ? "✅" : "❌";
        },
      },
    ]);

    // Default column configuration
    const defaultColDef = ref({
      flex: 1,
      minWidth: 100,
      resizable: true,
      sortable: true,
      filter: true,
      floatingFilter: true,
    });

    // Row selection configuration
    const rowSelection = ref("multiple");
    const paginationPageSize = ref(10);

    // Sidebar configuration
    const sideBar = ref({
      toolPanels: [
        {
          id: "columns",
          labelDefault: "Columns",
          labelKey: "columns",
          iconKey: "columns",
          toolPanel: "agColumnsToolPanel",
        },
        {
          id: "filters",
          labelDefault: "Filters",
          labelKey: "filters",
          iconKey: "filter",
          toolPanel: "agFiltersToolPanel",
        },
      ],
    });

    // Status bar configuration
    const statusBar = ref({
      statusPanels: [
        { statusPanel: "agTotalAndFilteredRowCountComponent", align: "left" },
        { statusPanel: "agTotalRowCountComponent", align: "center" },
        { statusPanel: "agFilteredRowCountComponent" },
        { statusPanel: "agSelectedRowCountComponent" },
        { statusPanel: "agAggregationComponent" },
      ],
    });

    const rowGroupPanelShow = ref("always");

    // Grid event handlers
    const onGridReady = (params) => {
      gridApi.value = params.api;
      gridColumnApi.value = params.columnApi;
      params.api.sizeColumnsToFit();
    };

    const onCellClicked = (params) => {
      console.log("Cell clicked:", params);
    };

    const onSelectionChanged = () => {
      const selectedRows = gridApi.value.getSelectedRows();
      console.log("Selection Changed:", selectedRows);
    };

    return {
      modules,
      rowData,
      colDefs,
      defaultColDef,
      rowSelection,
      paginationPageSize,
      sideBar,
      statusBar,
      rowGroupPanelShow,
      onGridReady,
      onCellClicked,
      onSelectionChanged,
    };
  },
};
</script>

<style>
.ag-theme-alpine {
  /* Header Styles */
  --ag-header-height: 30px;
  --ag-header-foreground-color: #000;
  --ag-header-background-color: #f8f8f8;
  --ag-header-cell-hover-background-color: #dfdfdf;
  --ag-header-cell-moving-background-color: #c7c7c7;

  /* Row Styles */
  --ag-row-hover-color: #f0f0f0;
  --ag-selected-row-background-color: rgba(0, 145, 234, 0.1);
  --ag-odd-row-background-color: #fafafa;

  /* Cell Styles */
  --ag-cell-horizontal-padding: 8px;
  --ag-cell-vertical-padding: 4px;
  --ag-cell-horizontal-border: solid 1px;
  --ag-cell-border-color: #e2e2e2;

  /* Font Styles */
  --ag-font-size: 13px;
  --ag-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;

  /* Sizing */
  --ag-list-item-height: 30px;

  /* Inputs */
  --ag-input-focus-border-color: #2196f3;
  --ag-input-border-color: #babfc7;

  /* Menu */
  --ag-menu-option-active-color: #2196f3;

  /* Scrollbars */
  --ag-scrollbar-background: #f0f0f0;
  --ag-scrollbar-thumb-color: #bfbfbf;
}

/* Optional: Custom scrollbar styles */
.ag-theme-alpine ::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

.ag-theme-alpine ::-webkit-scrollbar-track {
  background: var(--ag-scrollbar-background);
}

.ag-theme-alpine ::-webkit-scrollbar-thumb {
  background: var(--ag-scrollbar-thumb-color);
  border-radius: 4px;
}
</style>
