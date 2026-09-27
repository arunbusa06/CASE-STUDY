const r=require('express').Router(),a=require('../utils/asyncHandler'),{protect}=require('../middleware/auth.middleware'),c=require('../controllers/auth.controller');
r.post('/register',a(c.register));r.post('/login',a(c.login));r.post('/logout',protect,a(c.logout));r.get('/profile',protect,a(c.profile));module.exports=r;
