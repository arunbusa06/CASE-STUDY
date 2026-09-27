const mongoose=require('mongoose');
module.exports=async function(){if(!process.env.MONGODB_URI)throw new Error('MONGODB_URI is missing; configure .env');await mongoose.connect(process.env.MONGODB_URI);console.log('MongoDB connected');};
