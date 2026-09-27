const notFound=(req,res,next)=>{const e=new Error(`Route not found: ${req.method} ${req.originalUrl}`);e.statusCode=404;next(e);};
const errorHandler=(err,req,res,next)=>{let status=err.statusCode||500,msg=err.message||'Internal server error',details=err.details;
if(err.name==='ValidationError'){status=400;msg='Validation error';details=Object.values(err.errors).map(e=>({field:e.path,message:e.message}));}
else if(err.code===11000){status=409;msg='Resource already exists';details={field:Object.keys(err.keyValue||{})[0],message:'A record with this value already exists.'};}
else if(err.name==='CastError'){status=400;msg='Invalid resource ID';}
const body={success:false,message:msg,error:status===500?'internal_server_error':msg.toLowerCase().replace(/\\s+/g,'_'),statusCode:status};if(details)body.details=details;if(status===500&&process.env.NODE_ENV!=='production')body.debug=err.message;res.status(status).json(body);};
module.exports={notFound,errorHandler};
