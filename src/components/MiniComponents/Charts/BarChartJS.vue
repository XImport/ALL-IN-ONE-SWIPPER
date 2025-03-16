<template>
  <div>
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
              style="display: inline-block; vertical-align: middle"
            ></v-img>
          </v-btn>
        </template>
      </v-tooltip>
    </h4>
    <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
  </div>
</template>

<script>
import { exportToExcel } from "../../../utils"; // Adjust the path if needed
import { Bar } from "vue-chartjs";

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
import ChartDataLabels from 'chartjs-plugin-datalabels';

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  ChartDataLabels
);

export default {
  name: "BarChart",
  components: { Bar },
  props: ["CHARTDATA", "title", "IconName", "IconColor","UNITE"],
  data() {
    const unite = this.UNITE
    return {
      
      chartData: this.CHARTDATA,
      chartOptions: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
            position: "top",
          },
          title: {
            display: false,
            text: this.title,
          },
          tooltip: {
            enabled: true,
            callbacks: {
              label: function (context) {
                return `${context.dataset.label}: ${context.raw.toLocaleString()} ${unite}`;
              },
            },
          },
          datalabels: {
            display: false
          }
        },
        scales: {
          x: {
            grid: {
              display: true,
              color: "rgba(0, 0, 0, 0.1)",
            },
            ticks: {
              display: true
            }
          },
          y: {
            grid: {
              display: true,
              color: "rgba(0, 0, 0, 0.1)",
            },
            beginAtZero: true,
            ticks: {
              display: true
            }
          },
        },
      },
    };
  },
  watch: {
    CHARTDATA: {
      deep: true,
      immediate: true,
      handler(newData) {
        this.chartData = {
          ...newData,
          datasets: newData.datasets.map((dataset) => ({
            ...dataset, // Keeps dataset configuration, including color settings
          })),
        };
      },
    },
  },
  methods: {
    ExportToExcel() {
      const rows = [];
      const { labels, datasets } = this.chartData;

      // Transform chart data into a table-like array
      labels.forEach((label, index) => {
        if (
          this.title ==
          "Analyse du CA Brut pour les 6 principaux clients (Par Date)"
        ) {
          const row = { Clients: label };
          datasets.forEach((dataset) => {
            row[dataset.label] = dataset.data[index];
          });
          rows.push(row);
        } else {
          const row = { Date: label };
          datasets.forEach((dataset) => {
            row[dataset.label] = dataset.data[index];
          });
          rows.push(row);
        }
      });

      exportToExcel(rows, `${this.title}.xlsx`);
    },
  },
};
</script>
