const express = require('express');
const http = require('http');
const app = express();

const PORT = process.env.PORT || 3000;  // Render için şart

// Örnek endpoint
app.get('/', (req, res) => {
  res.send('Sunucu çalışıyor!');
});

const server = http.createServer(app);

server.listen(PORT, () => {
  console.log(`✅ Sunucu başarıyla başlatıldı: http://localhost:${PORT}`);
});

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`❌ Port ${PORT} kullanımda.`);
  } else {
    console.error('🚨 Sunucu hatası:', err);
  }
});
