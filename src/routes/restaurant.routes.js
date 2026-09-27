const r=require('express').Router(),a=require('../utils/asyncHandler'),{protect,authorize}=require('../middleware/auth.middleware'),c=require('../controllers/restaurant.controller');
r.get('/',a(c.list));r.get('/:id',a(c.get));r.post('/',protect,authorize('admin'),a(c.create));module.exports=r;
