
const ctx = document.getElementById('priceChart').getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'BNB/USDT Fiyatı',
      data: [],
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1
    }]
  }
});

async function fetchData() {
  const res = await fetch('https://api.binance.com/api/v3/klines?symbol=BNBUSDT&interval=1m&limit=50');
  const data = await res.json();
  const prices = data.map(d => parseFloat(d[4]));
  const times = data.map(d => new Date(d[0]).toLocaleTimeString());
  chart.data.labels = times;
  chart.data.datasets[0].data = prices;
  chart.update();
}

function buyCrypto() {
  alert('Alım işlemi yapıldı (simülasyon).');
}
function sellCrypto() {
  alert('Satım işlemi yapıldı (simülasyon).');
}

function toggleIndicator(indicator) {
  alert(indicator + ' göstergesi durumu değiştirildi.');
}

setInterval(fetchData, 5000);
fetchData();
