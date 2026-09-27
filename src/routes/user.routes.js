const r=require('express').Router(),a=require('../utils/asyncHandler'),{protect,authorize}=require('../middleware/auth.middleware'),c=require('../controllers/user.controller');
r.get('/',protect,authorize('admin'),a(c.list));module.exports=r;
