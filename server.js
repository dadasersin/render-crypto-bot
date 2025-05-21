const express = require('express');
const http = require('http');
const app = express();

// Örnek endpoint
app.get('/', (req, res) => {
  res.send('Sunucu çalışıyor!');
});

// Sunucuyu başlat - 0 portu verildiğinde sistem boş port atar
const server = http.createServer(app);

server.listen(0, () => {
  const { port } = server.address();
  console.log(`✅ Sunucu başarıyla başlatıldı: http://localhost:${port}`);
});

// Hata yakalama
server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`❌ Port kullanımda. Lütfen başka bir port deneyin.`);
  } else {
    console.error('🚨 Sunucu hatası:', err);
  }
});
