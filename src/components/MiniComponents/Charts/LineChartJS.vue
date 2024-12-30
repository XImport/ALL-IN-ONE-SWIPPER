<template>
  <h4 class="text-center text-decoration-underline">
    <v-icon :color="IconColor">{{ IconName }}</v-icon> {{ title }}
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
  </h4>
  <Line id="my-line-chart-id" :options="chartOptions" :data="chartData" />
</template>

<script>
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Filler,
} from "chart.js";
// Import the annotation plugin
import annotationPlugin from "chartjs-plugin-annotation";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Filler,
  annotationPlugin // Register the plugin
);

export default {
  name: "LineChart",
  components: { Line },
  props: ["CHARTDATA", "title", "IconName", "IconColor"],
  data() {
    // Assume `chartData` has point colors defined
    const pointColor = this.CHARTDATA.datasets[1].backgroundColor; // Get the background color of the points
    const pointColor1 = this.CHARTDATA.datasets[0].backgroundColor; // Get the background color of the points

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
                return `représente: ${context.raw}`;
              },
            },
          },
          annotation: {
            annotations: {
              // Min Target Line
              minTargetLine: {
                type: "line",
                yMin: 2200000, // Minimum value for the target line
                yMax: 2200000, // Same value as yMin for a horizontal line
                borderColor: "#ec1f0e", // Color of the minimum target line
                borderWidth: 2, // Thickness of the line
                label: {
                  content: "Min Target Line", // Label for the minimum target line
                  enabled: true,
                  position: "center", // Position of the label
                  font: {
                    size: 14,
                    weight: "bold",
                  },
                  color: "red",
                },
              },
              // Max Target Line
              maxTargetLine: {
                type: "line",
                yMin: 2700000, // Maximum value for the target line
                yMax: 2700000, // Same value as yMin for a horizontal line
                borderColor: "#00bd1a", // Color of the maximum target line
                borderWidth: 2, // Thickness of the line
                label: {
                  content: "Max Target Line", // Label for the maximum target line
                  enabled: true,
                  position: "center", // Position of the label
                  font: {
                    size: 14,
                    weight: "bold",
                  },
                  color: "blue",
                },
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
      },
    };
  },
};
</script>
