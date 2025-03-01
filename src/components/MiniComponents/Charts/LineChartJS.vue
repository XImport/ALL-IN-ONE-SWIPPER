<template>
  <div class="chart-container">
    <h4 class="text-center text-decoration-underline d-flex align-center justify-center">
      <v-icon :color="IconColor" class="mr-2">{{ IconName }}</v-icon>
      <span>{{ title }}</span>
      <v-tooltip location="top">
        <template v-slot:activator="{ props }">
          <v-btn
            icon
            density="comfortable"
            size="small"
            class="ml-2"
            v-bind="props"
            @click="ExportToExcel"
            variant="text"
          >
            <v-img
              src="https://static-00.iconduck.com/assets.00/ms-excel-icon-2048x2026-nws24wyy.png"
              width="22"
              height="22"
            ></v-img>
          </v-btn>
        </template>
        <span>Exporter Vers Excel</span>
      </v-tooltip>
    </h4>
    <div class="chart-wrapper">
      <Line 
        id="my-line-chart-id" 
        :options="chartOptions" 
        :data="chartData"
        :height="chartHeight" 
      />
    </div>
  </div>
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
import annotationPlugin from "chartjs-plugin-annotation";
import { exportToExcel } from "../../../utils"; // Adjust the path if needed

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Filler,
  annotationPlugin
);

export default {
  name: "LineChart",
  components: { Line },
  props: {
    CHARTDATA: {
      type: Object,
      required: true
    },
    title: {
      type: String,
      default: "Line Chart"
    },
    IconName: {
      type: String,
      default: "mdi-chart-line"
    },
    IconColor: {
      type: String,
      default: "primary"
    },
    Unite: {
      type: String,
      default: "dhs"
    },
    Min: {
      type: Number,
      default: null
    },
    Max: {
      type: Number,
      default: null
    },
    chartHeight: {
      type: Number,
      default: 380
    }
  },
  data() {
    return {
      chartData: this.CHARTDATA,
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
          mode: 'index',
          intersect: false,
        },
        plugins: {
          legend: {
            display: true,
            position: "top",
            labels: {
              usePointStyle: true,
              padding: 15,
              boxWidth: 10,
              font: {
                size: 11
              }
            }
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
            backgroundColor: 'rgba(255, 255, 255, 0.9)',
            titleColor: '#333',
            bodyColor: '#666',
            borderColor: '#ddd',
            borderWidth: 1,
            padding: 10,
            usePointStyle: true,
            callbacks: {
              label: function (context) {
                const value = context.raw;
                const label = context.dataset.label || '';
                return `${label}: ${new Intl.NumberFormat().format(value)}`;
              },
            },
          },
          annotation: {
            annotations: this.getAnnotations()
          },
        },
        layout: {
          padding: {
            top: 30,
            bottom: 10,
            left: 15,
            right: 20,
          },
        },
        scales: {
          x: {
            grid: {
              display: false
            },
            ticks: {
              maxRotation: 45,
              minRotation: 45
            }
          },
          y: {
            beginAtZero: false,
            grid: {
              color: 'rgba(0, 0, 0, 0.05)'
            },
            ticks: {
              callback: function(value) {
                return new Intl.NumberFormat().format(value);
              }
            }
          }
        },
        elements: {
          line: {
            tension: 0.3 // Smoother curves
          },
          point: {
            radius: 3,
            hoverRadius: 6
          }
        }
      },
    };
  },
  methods: {
    getAnnotations() {
      const annotations = {};
      
      if (this.Min !== null) {
        annotations.minTargetLine = {
          type: "line",
          yMin: this.Min,
          yMax: this.Min,
          borderColor: "#ec1f0e",
          borderWidth: 2,
          borderDash: [5, 5],
          label: {
            content: `"Min ${(this.Min).toLocaleString(2)} ${this.Unite}"`,
            display: true,
            position: "end",
            backgroundColor: 'rgba(236, 31, 14, 0.8)',
            font: {
              size: 11,
              weight: "bold",
            },
            color: "white",
            padding: 5
          }
        };
      }
      
      if (this.Max !== null) {
        annotations.maxTargetLine = {
          type: "line",
          yMin: this.Max,
          yMax: this.Max,
          borderColor: "#00bd1a",
          borderWidth: 2,
          borderDash: [5, 5],
          label: {
            content: `"Max ${(this.Max).toLocaleString(2)} ${this.Unite}"`,
            display: true,
            position: "end",
            backgroundColor: 'rgba(0, 189, 26, 0.8)',
            font: {
              size: 11,
              weight: "bold",
            },
            color: "white",
            padding: 5
          }
        };
      }
      
      return annotations;
    },
    updateAnnotations() {
      this.chartOptions = {
        ...this.chartOptions,
        plugins: {
          ...this.chartOptions.plugins,
          annotation: {
            annotations: this.getAnnotations()
          }
        }
      };
    },
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
  watch: {
    CHARTDATA: {
      deep: true,
      immediate: true,
      handler(newData) {
        this.chartData = {
          ...newData,
          datasets: newData.datasets.map((dataset) => ({
            ...dataset,
            pointBackgroundColor: dataset.borderColor || dataset.backgroundColor,
            pointBorderColor: '#fff',
            pointBorderWidth: 1,
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: dataset.borderColor || dataset.backgroundColor,
            pointHoverBorderWidth: 2
          })),
        };
      },
    },
    Min() {
      this.updateAnnotations();
    },
    Max() {
      this.updateAnnotations();
    }
  },
  mounted() {
    this.updateAnnotations();
  }
};
</script>

<style scoped>
.chart-container {
  position: relative;
  width: 100%;
  margin: 0 auto;
}

.chart-wrapper {
  position: relative;
  width: 100%;
  height: 100% !important;
  overflow: hidden;
}

@media (max-width: 600px) {
  .chart-wrapper {
    height: 350px !important; /* Adjusted for smaller screens */
  }
}
</style>
