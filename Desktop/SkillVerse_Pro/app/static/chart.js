<canvas id="skillChart"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>

const ctx = document.getElementById('skillChart');

new Chart(ctx, {
  type: 'bar',

  data: {

    labels: ['Cricket','Football','Programming'],

    datasets: [{

      label: 'Skill Scores',

      data: [80,60,90],

      backgroundColor: [
        '#6366f1',
        '#22c55e',
        '#f59e0b'
      ]

    }]

  }

});

</script>