
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
app.use(express.static(__dirname));
app.listen(port, () => console.log(`Sunucu ${port} portunda çalışıyor`));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
