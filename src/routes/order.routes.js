const r=require('express').Router(),a=require('../utils/asyncHandler'),{protect,authorize}=require('../middleware/auth.middleware'),c=require('../controllers/order.controller');
r.post('/',protect,a(c.create));r.get('/my-orders',protect,a(c.mine));r.get('/:id',protect,a(c.get));r.patch('/:id/status',protect,authorize('admin'),a(c.status));module.exports=r;
