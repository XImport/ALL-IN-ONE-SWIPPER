<template>
  <h3 class="text-center text-decoration-underline">
    <v-icon :color="IconColor">{{ IconName }}</v-icon> {{ title }}
  </h3>
  <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
</template>

<script>
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

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "BarChart",
  components: { Bar },
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
                return `Value: ${context.raw}`;
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
        scales: {
          x: {
            grid: {
              display: true,
              color: "rgba(0, 0, 0, 0.1)",
            },
          },
          y: {
            grid: {
              display: true,
              color: "rgba(0, 0, 0, 0.1)",
            },

            beginAtZero: true,
          },
        },
        animations: {
          tension: {
            duration: 1000,
            easing: "easeInOutBounce",
            from: 1,
            to: 0,
            loop: true,
          },
        },
        interaction: {
          mode: "nearest", // Options: 'point', 'dataset', 'index', 'nearest'
          axis: "x",
          intersect: false,
        },
        elements: {
          bar: {
            borderWidth: 2,
            borderRadius: 5,
            backgroundColor: "rgba(75, 192, 192, 0.6)",
          },
        },
      },
    };
  },
};
</script>
