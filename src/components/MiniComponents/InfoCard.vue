<template>
  <v-card
    class="metric-card pa-4 rounded-xl"
    variant="flat"
    :rounded="true"
    style="max-width: 10%"
  >
    <div class="d-flex justify-space-between align-start">
      <div class="metric-content">
        <div
          class="text-subtitle-1 text-medium-emphasis mb-1 font-weight-bold text-h4"
        >
          <span class="text-black"> {{ Title }}</span>
        </div>
        <div class="d-flex align-baseline">
          <span class="text-h6 font-weight-bold"
            >{{ FormatNumber(TextNumber) }}
          </span>
        </div>
        <div class="growth-indicator">
          <span class="text-success text-caption">
            +8.2%
            <span class="text-caption text-medium-emphasis">
              since last month</span
            >
          </span>
        </div>
      </div>
      <v-icon size="35" :color="IconColor">{{ Icon }}</v-icon>
    </div>
  </v-card>
</template>

<script>
export default {
  name: "MetricCard",
  props: ["Title", "TextNumber", "Icon", "IconColor"],
  methods: {
    FormatNumber(number) {
      // If the number is in millions, format it to millions (MDHS)
      if (typeof number === "string") {
        return number; // Return the string as-is
      }
      if (number >= 1000000) {
        const formattedNumber = (number / 1000000).toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        });
        return `${formattedNumber} MDHS`; // Add the MDHS label
      }
      // If the number is in thousands, format it to thousands (KDHS)
      else if (number >= 1000) {
        const formattedNumber = (number / 1000).toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        });
        return `${formattedNumber} KDHS`; // Add the KDHS label
      }
      // If it's less than 1000, return the number as is
      else {
        return `${number.toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        })} DHS`;
      }
    },
  },
};
</script>

<style scoped>
.metric-card {
  background-color: #ffffff;
  border: 1px solid #f0f0f0;
  min-width: 240px;
}

.text-medium-emphasis {
  color: #000000;
}

.growth-indicator {
  display: inline-flex;
  align-items: center;
}

.text-success {
  color: #4caf50;
}
</style>
