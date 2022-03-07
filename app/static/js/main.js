// plot loan and deposits
var ctx = document.getElementById("loans-deposits").getContext("2d");

var xAxislabel = Object.keys(dep);
var deposits = {
  label: "deposits",
  backgroundColor: "orange",
  data: xAxislabel.map((xAxislabel) => dep[xAxislabel].deposits),
};
var loans = {
  label: "loans",
  backgroundColor: "blue",
  data: xAxislabel.map((xAxislabel) => dep[xAxislabel].loans),
};

var data = {
  labels: xAxislabel,
  datasets: [deposits, loans],
};

var myBarChart = new Chart(ctx, {
  type: "bar",
  data: data,
  options: {
    barValueSpacing: 20,
  },
  scales: {
    yAxes: [
      {
        ticks: {
          min: 0,
        },
      },
    ],
  },
});

// plot marketshare

var ctx_ms = document.getElementById("market-share").getContext("2d");

var myChart = new Chart(ctx_ms, {
  type: "pie",
  data: {
    labels: Object.keys(market_share),
    datasets: [
      {
        label: "# Market share",
        data: Object.keys(market_share).map(function (key) {
          return market_share[key];
        }),
        backgroundColor: [
          "#0074D9",
          "#FF4136",
          "#2ECC40",
          "#FF851B",
          "#7FDBFF",
          "#B10DC9",
          "#FFDC00",
          "#001f3f",
          "#39CCCC",
          "#01FF70",
          "#85144b",
          "#F012BE",
          "#3D9970",
          "#111111",
          "#AAAAAA",
        ],
        borderWidth: 0,
      },
    ],
  },
  options: {
    tooltips: {
      enabled: false,
    },
    legend: {
      display: false, // <- the important part
    },
    events: [],
  },
});

// plot loan to deposit ratio

var ctx_ldr = document.getElementById("ldr").getContext("2d");

var xAxisLabels = Object.keys(ratio);

var capitecBank = {
  label: "Capitec",
  borderColor: "blue",
  data: xAxisLabels.map((xAxisLabel) => ratio[xAxisLabel].Capitec),
};

var investecBank = {
  label: "Investec",
  borderColor: "red",
  data: xAxisLabels.map((xAxisLabel) => ratio[xAxisLabel].Investec),
};

var Absa = {
  label: "ABSA",
  borderColor: "#AAAAAA",
  data: xAxisLabels.map((xAxisLabel) => ratio[xAxisLabel].ABSA),
};

var standard_bank = {
  label: "Standard Bank",
  borderColor: "#3D9970",
  data: xAxisLabels.map((xAxisLabel) => ratio[xAxisLabel].Standard_Bank),
};

var fnb = {
  label: "FNB",
  borderColor: "#F012BE",
  data: xAxisLabels.map((xAxisLabel) => ratio[xAxisLabel].FNB),
};

var nedbank = {
  label: "Nedbank",
  borderColor: "#001f3f",
  data: xAxisLabels.map((xAxisLabel) => ratio[xAxisLabel].Nedbank),
};
var data = {
  labels: xAxisLabels,
  datasets: [capitecBank, investecBank, Absa, standard_bank, fnb, nedbank],
};

var myLineChart = new Chart(ctx_ldr, {
  type: "line",
  data: data,
});

// plot morgages

var ctx_mortgages = document.getElementById("mortgages").getContext("2d");

var xAxisLabels = Object.keys(mortgages);

var capitecBank = {
  label: "Capitec",
  backgroundColor: "blue",
  data: xAxisLabels.map((xAxisLabel) => mortgages[xAxisLabel].Capitec),
};

var investecBank = {
  label: "Investec",
  backgroundColor: "red",
  data: xAxisLabels.map((xAxisLabel) => mortgages[xAxisLabel].Investec),
};

var Absa = {
  label: "ABSA",
  backgroundColor: "#AAAAAA",
  data: xAxisLabels.map((xAxisLabel) => mortgages[xAxisLabel].ABSA),
};

var standard_bank = {
  label: "Standard Bank",
  backgroundColor: "#3D9970",
  data: xAxisLabels.map((xAxisLabel) => mortgages[xAxisLabel].Standard_Bank),
};

var fnb = {
  label: "FNB",
  backgroundColor: "#F012BE",
  data: xAxisLabels.map((xAxisLabel) => mortgages[xAxisLabel].FNB),
};

console.log(fnb);

var nedbank = {
  label: "Nedbank",
  backgroundColor: "#001f3f",
  data: xAxisLabels.map((xAxisLabel) => mortgages[xAxisLabel].Nedbank),
};
var data = {
  labels: xAxisLabels,
  datasets: [capitecBank, investecBank, Absa, standard_bank, fnb, nedbank],
};

var myLineChart = new Chart(ctx_mortgages, {
  type: "bar",
  data: data,
});

// plot investments

var ctx_investments = document.getElementById("investment").getContext("2d");

var xAxisLabels = Object.keys(investments);

var capitecBank = {
  label: "Capitec",
  backgroundColor: "blue",
  data: xAxisLabels.map((xAxisLabel) => investments[xAxisLabel].Capitec),
};

var investecBank = {
  label: "Investec",
  backgroundColor: "red",
  data: xAxisLabels.map((xAxisLabel) => investments[xAxisLabel].Investec),
};

var Absa = {
  label: "ABSA",
  backgroundColor: "#AAAAAA",
  data: xAxisLabels.map((xAxisLabel) => investments[xAxisLabel].ABSA),
};

var standard_bank = {
  label: "Standard Bank",
  backgroundColor: "#3D9970",
  data: xAxisLabels.map((xAxisLabel) => investments[xAxisLabel].Standard_Bank),
};

var fnb = {
  label: "FNB",
  backgroundColor: "#F012BE",
  data: xAxisLabels.map((xAxisLabel) => investments[xAxisLabel].FNB),
};

console.log(fnb);

var nedbank = {
  label: "Nedbank",
  backgroundColor: "#001f3f",
  data: xAxisLabels.map((xAxisLabel) => investments[xAxisLabel].Nedbank),
};
var data = {
  labels: xAxisLabels,
  datasets: [capitecBank, investecBank, Absa, standard_bank, fnb, nedbank],
};

var myLineChart = new Chart(ctx_investments, {
  type: "bar",
  data: data,
});
