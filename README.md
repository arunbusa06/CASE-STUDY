# Food Delivery API — Complete Implementation

Educational REST API aligned with the case-study API groups: authentication, restaurants, food items, orders, admin users, and health check.

## Stack
Node.js, Express, MongoDB/Mongoose, JWT, bcrypt, centralized error handling.

## Run locally
1. Install Node.js 18+ and run MongoDB.
2. Copy `.env.example` to `.env`; set a strong `JWT_SECRET`.
3. Run `npm install`
4. Run `npm run seed` to create demo accounts and sample restaurant/food.
5. Run `npm run dev`. Base URL: `http://localhost:5000/api`.
6. Import `postman/Food_Delivery_API.postman_collection.json` into Postman.
7. Use IDs printed by seeding for `restaurant_id` and `food_item_id`. Login request automatically stores `token` and `user_id`.

## Local demo credentials
Admin: `admin@example.com` / `Admin12345!`
Customer: `customer@example.com` / `Customer12345!`
Change these before deployment; never publish secrets or real tokens.

## Endpoints
- GET `/api/health`
- POST `/api/auth/register`, POST `/api/auth/login`, POST `/api/auth/logout`, GET `/api/auth/profile`
- GET `/api/restaurants`, GET `/api/restaurants/:id`, POST `/api/restaurants` (admin)
- GET `/api/food-items`, POST `/api/food-items` (admin)
- POST `/api/orders`, GET `/api/orders/my-orders`, GET `/api/orders/:id`, PATCH `/api/orders/:id/status` (admin)
- GET `/api/users` (admin)

Logout is stateless: remove the token in the client. This project is an educational implementation, not a complete production payment/delivery platform.
