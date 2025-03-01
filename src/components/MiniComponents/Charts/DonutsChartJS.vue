<template>
  <div
    class="donut-container"
    style="max-width: 427px; height: auto;"
  >
    <h4 class="text-center text-decoration-underline">
      <v-icon :color="IconColor">{{ IconName }}</v-icon> {{ title }}
      <v-tooltip text="Exporter Vers Excel" location="top" activator="parent">
        <template v-slot:activator="{ props }">
          <v-btn
            icon
            compact
            size="20"
            class="ml-2"
            v-bind="props"
            @click="ExportToExcel"
          >
            <v-img
              src="https://static-00.iconduck.com/assets.00/ms-excel-icon-2048x2026-nws24wyy.png"
              width="25"
              class=""
              style="display: inline-block; vertical-align: middle"
            ></v-img>
          </v-btn>
        </template>
      </v-tooltip>
    </h4>
    <Doughnut
      id="my-donut-chart-id"
      :options="chartOptions"
      :data="chartData"
    />
  </div>
</template>

<script>
import { Doughnut } from "vue-chartjs";
import { exportToExcel } from "../../../utils"; // Adjust the path if needed
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  ArcElement, // This is for donut (arc) chart elements
  CategoryScale,
  LinearScale
);

export default {
  name: "DonutChart",
  components: { Doughnut },
  props: ["CHARTDATA", "title", "IconName", "IconColor"],
  data() {
    return {
      chartData: this.CHARTDATA,
      chartOptions: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
            position: "top", // Options: 'top', 'bottom', 'left', 'right'
          },
          title: {
            display: false,
            text: this.title,
            font: {
              size: 18,
            },
          },
          tooltip: {
            enabled: true,
            callbacks: {
              label: function (context) {
                return `représente: ${context.raw} %`;
              },
            },
          },
        },
        layout: {
          padding: {
            top: 20,
            bottom: 10,
            left: 15,
            right: 15,
          },
        },
        // To make sure the donut chart is styled correctly
        elements: {
          arc: {
            borderWidth: 2, // Border width for the donut slices
          },
        },
        // Optional: Adjust cutoutPercentage to change the donut hole size
        cutoutPercentage: 100, // Adjust the hole size (values range from 0 to 100)
      },
    };
  },
  watch: {
    CHARTDATA: {
      handler(newData) {
        this.chartData = newData;
      },
      deep: true,
    },
  },
  methods: {
    ExportToExcel() {
      const rows = [];
      const { labels, datasets } = this.chartData;

      // Transform chart data into a table-like array
      labels.forEach((label, index) => {
        const row = { Date: label };
        datasets.forEach((dataset) => {
          row[dataset.label] = dataset.data[index];
        });
        rows.push(row);
      });
      exportToExcel(rows, `${this.title}.xlsx`);
    },
  },
};
</script>

<style scoped>
.donut-container {
  max-width: 100%;
  width: 100%; /* Allow full width */
  height: 100%; /* Allow height to auto-scale */
}
</style>
