const { Spot } = require('@binance/connector');
require('dotenv').config();

const client = new Spot(process.env.API_KEY, process.env.API_SECRET);

async function getPrice() {
  try {
    const result = await client.tickerPrice('BNBUSDT');
    console.log('BNB fiyatı:', result.data.price);
  } catch (err) {
    console.error('Hata:', err);
  }
}

setInterval(getPrice, 10000); // her 10 saniyede bir fiyat al