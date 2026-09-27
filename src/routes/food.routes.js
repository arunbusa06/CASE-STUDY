const r=require('express').Router(),a=require('../utils/asyncHandler'),{protect,authorize}=require('../middleware/auth.middleware'),c=require('../controllers/food.controller');
r.get('/',a(c.list));r.post('/',protect,authorize('admin'),a(c.create));module.exports=r;
