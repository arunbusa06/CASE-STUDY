require('dotenv').config();
const app = require('./app');
const connectDB = require('./utils/db');
const PORT = process.env.PORT || 5000;
connectDB().then(() => app.listen(PORT, () => console.log(`Food Delivery API running on ${PORT}`)))
  .catch(err => { console.error('Database connection failed:', err.message); process.exit(1); });
