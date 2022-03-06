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

var ctx = document.getElementById('market-share')

var myChart = new Chart(ctx, {
  type: "pie",
  data: {
    labels: Object.keys(market_share),
    datasets: [
      {
        label: "# Frecuencies Words",
        data: Object.keys(market_share).map(function (key) {
          return market_share[key];
        }),
        backgroundColor:["#0074D9", "#FF4136", "#2ECC40", "#FF851B", "#7FDBFF", "#B10DC9", "#FFDC00", "#001f3f", "#39CCCC", "#01FF70", "#85144b", "#F012BE", "#3D9970", "#111111", "#AAAAAA"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  },
});