const mongoose=require('mongoose'),bcrypt=require('bcryptjs');
const schema=new mongoose.Schema({name:{type:String,required:true,trim:true,minlength:2,maxlength:80},email:{type:String,required:true,unique:true,lowercase:true,trim:true},password:{type:String,required:true,minlength:8,select:false},role:{type:String,enum:['customer','admin'],default:'customer'}},{timestamps:true});
schema.pre('save',async function(next){if(!this.isModified('password'))return next();this.password=await bcrypt.hash(this.password,12);next();});
schema.methods.comparePassword=function(p){return bcrypt.compare(p,this.password);};module.exports=mongoose.model('User',schema);
