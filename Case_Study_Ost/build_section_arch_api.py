from content_builder import (
    add_sec_heading,
    add_sub_heading,
    add_sub_sub_heading,
    add_para,
    add_bullet,
    add_code_snippet,
    add_image_figure
)
from table_builder import build_academic_table

def generate_section_arch_api(doc):
    print("Generating Section V (Architecture & Tech Stack) and Section VI (API & DB Analysis)...")

    # ==========================================
    # SECTION V: SYSTEM ARCHITECTURE AND TECHNOLOGY STACK
    # ==========================================
    add_sec_heading(doc, "V. SYSTEM ARCHITECTURE AND TECHNOLOGY STACK")
    
    add_para(doc,
        "The proposed food delivery platform is architectured as a multi-tier, decoupled distributed system. The architecture separates client presentation, "
        "network gateway mediation, server-side business processing, and document persistence into distinct, independently scalable tiers."
    )

    add_sub_heading(doc, "A. Overall Architecture")
    add_para(doc,
        "The flow of data through the system follows a disciplined linear pipeline: Client Applications → REST API Gateway → Node.js / Express.js Backend → "
        "Authentication & Authorization Guards → Input Validation Middleware → Business Logic Controllers → MongoDB Persistence Tier → Centralized "
        "Error / Response Formatter → Client. Concurrently, Postman connects directly to the REST API endpoints to execute automated functional and "
        "reliability verification suites."
    )

    add_image_figure(doc, "fig1_system_architecture.png", "Fig. 1. Proposed Multi-Tier Web Service Architecture and Testing Harness.")

    add_sub_heading(doc, "B. Client Presentation Tier")
    add_para(doc,
        "The presentation tier encompasses four specialized front-end interfaces: the Customer Mobile/Web Application, the Restaurant Partner Dashboard, "
        "the Delivery Courier Mobile Application, and the Central Administrative Portal. These clients maintain zero direct database connectivity; all "
        "user interactions are translated into HTTP REST requests transmitting JSON payloads."
    )

    add_sub_heading(doc, "C. REST API and Gateway Tier")
    add_para(doc,
        "Acting as the single point of entry, the API Gateway enforces Transport Layer Security (TLS 1.3 / HTTPS) encryption, terminates SSL connections, "
        "regulates Cross-Origin Resource Sharing (CORS) headers, and applies IP-based rate limiting to protect backend worker threads from denial-of-service surges."
    )

    add_sub_heading(doc, "D. Node.js and Express.js Backend Service Tier")
    add_para(doc,
        "The core application runtime is powered by Node.js, utilizing its asynchronous, non-blocking I/O event-loop model to manage thousands of concurrent "
        "client connections with minimal memory overhead. The Express.js web application framework orchestrates routing, middleware chaining, and HTTP request lifecycle "
        "management, providing an agile foundation for modular service controllers."
    )

    add_sub_heading(doc, "E. Authentication and Authorization Layer")
    add_para(doc,
        "This security middleware intercepts incoming requests to private endpoints. It validates cryptographic signatures on incoming JWT Bearer tokens, "
        "extracts user claims, and checks the user's role against route-level permission matrices (Customer, Restaurant, Delivery, Admin)."
    )

    add_sub_heading(doc, "F. Input Validation Layer")
    add_para(doc,
        "Prior to invoking controller logic, incoming requests pass through declarative schema validators. This layer sanitizes string inputs to prevent injection, "
        "enforces field presence, verifies BSON ObjectID formats, and bounds numerical values."
    )

    add_sub_heading(doc, "G. Centralized Error-Handling Layer")
    add_para(doc,
        "Express global error-handling middleware intercepts all rejected promises and synchronous exceptions. It guarantees that clients receive sanitized, "
        "deterministic JSON responses while logging comprehensive error traces internally."
    )

    add_sub_heading(doc, "H. MongoDB Persistence Tier")
    add_para(doc,
        "MongoDB provides document-oriented data persistence. Its flexible BSON data model naturally represents hierarchical food delivery entities (such as "
        "embedded cart items and historical order milestones) while supporting horizontal sharding and replica sets for high availability."
    )

    add_sub_heading(doc, "I. Postman Quality Assurance Layer")
    add_para(doc,
        "Postman functions as an external validation harness, sending synthetic requests across all endpoints, evaluating status codes, asserting payload "
        "schemas, verifying error responses, and executing automated regression runs."
    )

    add_sub_heading(doc, "J. Technology Stack Specification")
    add_para(doc, "The proposed technologies, frameworks, and tools are summarized in Table I:")

    headers_t1 = ["Layer / Domain", "Proposed Technology", "Licensing", "Technical Justification"]
    rows_t1 = [
        ["Runtime Environment", "Node.js (LTS)", "MIT License", "Asynchronous, event-driven I/O optimized for concurrent, high-throughput network applications."],
        ["Web Framework", "Express.js", "MIT License", "Minimalist, flexible routing and middleware chaining ideal for building robust REST APIs."],
        ["Document Database", "MongoDB", "SSPL / Open", "Flexible schema, high-performance JSON/BSON document persistence, horizontal scaling."],
        ["Data Modeling ODM", "Mongoose", "MIT License", "Schema-based document validation, middleware hooks, and strict type casting for MongoDB."],
        ["API Architecture", "RESTful Architecture", "Open Standard", "Stateless, resource-oriented modeling with standard HTTP methods and JSON data format."],
        ["Testing & Automation", "Postman / Newman", "Proprietary / Free", "Automated API verification, contract testing, assertions, and CI regression suites."],
        ["Authentication", "JSON Web Tokens (JWT)", "RFC 7519", "Stateless, cryptographically signed claims-based security eliminating session storage overhead."],
        ["Security & Headers", "Helmet & Express-Rate-Limit", "MIT License", "Automated HTTP header hardening, XSS protection, and IP-based request throttling."],
        ["Central Logging", "Winston Logger", "MIT License", "Multi-transport, structured JSON logging with automated redaction of sensitive credentials."]
    ]
    build_academic_table(doc, headers_t1, rows_t1, caption="TABLE I. PROPOSED TECHNOLOGY STACK SPECIFICATION")

    # ==========================================
    # SECTION VI: API AND DATABASE ANALYSIS
    # ==========================================
    add_sec_heading(doc, "VI. API AND DATABASE ANALYSIS")
    
    add_para(doc,
        "A rigorous database schema and predictable API design are paramount to software reliability. This section presents the document collection design, "
        "REST endpoint contracts, detailed endpoint breakdowns, and the CRUD mapping matrix."
    )

    add_sub_heading(doc, "A. MongoDB Document Schema Design")
    add_para(doc,
        "The persistence layer is partitioned into six core collections designed to balance normalization with query performance:"
    )

    headers_t2 = ["Collection", "Primary Key", "Important Attributes & Embedded Schemas", "Indexing & Integrity Rules"]
    rows_t2 = [
        ["users", "_id (ObjectID)", "name, email, passwordHash, role (Customer/Restaurant/Delivery/Admin), phone, addresses[]", "Unique index on email; role enumeration check."],
        ["restaurants", "_id (ObjectID)", "name, ownerId, address, cuisineType, operationalStatus (OPEN/CLOSED), deliveryRadiusKm", "2dsphere geospatial index on coordinates; index on ownerId."],
        ["menuItems", "_id (ObjectID)", "restaurantId, name, description, price, category, isAvailable, dietaryTags[]", "Compound index on (restaurantId, category); price >= 0."],
        ["carts", "_id (ObjectID)", "customerId, restaurantId, items: [{ menuItemId, quantity, unitPrice, specialNotes }], subtotal, updatedAt", "Unique index on customerId; single restaurant constraint per cart."],
        ["orders", "_id (ObjectID)", "customerId, restaurantId, deliveryRiderId, items[], totalAmount, status (PENDING/ACCEPTED/etc.), paymentDetails", "Indexes on customerId, restaurantId, status; state machine rules."],
        ["deliveries", "_id (ObjectID)", "orderId, riderId, pickupAddress, dropoffAddress, status (ASSIGNED/PICKED_UP/DELIVERED), timestamps{}", "Index on orderId, riderId; OTP delivery verification code."]
    ]
    build_academic_table(doc, headers_t2, rows_t2, caption="TABLE II. MONGODB DOCUMENT COLLECTIONS SPECIFICATION")

    add_sub_heading(doc, "B. REST API Endpoint Specification")
    add_para(doc, "The complete endpoint matrix covering core business operations is detailed in Table III:")

    headers_t3 = ["HTTP Method", "Endpoint URI", "Role / Auth Required", "Purpose & Operation Scope"]
    rows_t3 = [
        ["POST", "/api/auth/register", "Public", "Register new customer, restaurant, or courier account with validated inputs."],
        ["POST", "/api/auth/login", "Public", "Authenticate user credentials and issue cryptographically signed JWT."],
        ["GET", "/api/users/profile", "Bearer Token (Any Role)", "Retrieve authenticated user's profile details and delivery address book."],
        ["GET", "/api/restaurants", "Public", "Retrieve list of active restaurants with optional pagination and cuisine filters."],
        ["GET", "/api/restaurants/:id", "Public", "Retrieve specific restaurant profile, operational hours, and ratings."],
        ["GET", "/api/restaurants/:id/menu", "Public", "Retrieve active menu catalog categorized by food sections for a restaurant."],
        ["GET", "/api/cart", "Bearer Token (Customer)", "Retrieve current authenticated customer's transient active shopping cart."],
        ["POST", "/api/cart/items", "Bearer Token (Customer)", "Add or increment item quantity in cart; enforces single-restaurant constraint."],
        ["DELETE", "/api/cart/items/:id", "Bearer Token (Customer)", "Remove specific item line or clear customer's shopping cart."],
        ["POST", "/api/orders", "Bearer Token (Customer)", "Checkout validated cart, create persistent order in PENDING status."],
        ["GET", "/api/orders", "Bearer Token (All Roles)", "List orders filtered by customer, restaurant owner, or courier role."],
        ["GET", "/api/orders/:id", "Bearer Token (All Roles)", "Retrieve complete order details, item lines, total price, and live status."],
        ["PATCH", "/api/orders/:id", "Bearer Token (Rest./Admin)", "Update order lifecycle state (e.g., ACCEPTED, PREPARING, CANCELLED)."],
        ["GET", "/api/deliveries/:id", "Bearer Token (Rider/Cust.)", "Retrieve delivery routing coordinates, courier location, and ETA."],
        ["PATCH", "/api/deliveries/:id", "Bearer Token (Delivery)", "Update delivery status (e.g., PICKED_UP, DELIVERED) with OTP confirmation."]
    ]
    build_academic_table(doc, headers_t3, rows_t3, caption="TABLE III. PROPOSED REST API ENDPOINTS SPECIFICATION")

    add_image_figure(doc, "fig2_request_response_flow.png", "Fig. 2. API Request Interception, Validation Pipeline, and Response Lifecycle.")

    add_sub_heading(doc, "C. Detailed Endpoint Technical Breakdown")
    add_para(doc, "To ensure contract clarity, key representative endpoints are analyzed across technical dimensions:")

    add_sub_sub_heading(doc, "1) POST /api/auth/register")
    add_bullet(doc, "Public onboarding endpoint.", bold_prefix="Authentication: ")
    add_bullet(doc, "JSON object containing name, email, password, role, and phone.", bold_prefix="Request Body: ")
    add_bullet(doc, "HTTP 201 Created with { success: true, data: { userId, email, role } }.", bold_prefix="Expected Response: ")
    add_bullet(doc, "HTTP 400 (Validation failure), HTTP 409 (Email already registered), HTTP 500 (Server exception).", bold_prefix="Possible Errors: ")

    add_sub_sub_heading(doc, "2) POST /api/auth/login")
    add_bullet(doc, "Public credential exchange endpoint.", bold_prefix="Authentication: ")
    add_bullet(doc, "JSON object containing email and password.", bold_prefix="Request Body: ")
    add_bullet(doc, "HTTP 200 OK with { success: true, data: { token, expiresIn, user: { id, name, role } } }.", bold_prefix="Expected Response: ")
    add_bullet(doc, "HTTP 400 (Malformed payload), HTTP 401 (Invalid email or password).", bold_prefix="Possible Errors: ")

    add_sub_sub_heading(doc, "3) GET /api/restaurants/:id")
    add_bullet(doc, "Public inspection endpoint.", bold_prefix="Authentication: ")
    add_bullet(doc, "URL parameter :id (24-char hex string).", bold_prefix="Request Body: None. ")
    add_bullet(doc, "HTTP 200 OK with restaurant profile details.", bold_prefix="Expected Response: ")
    add_bullet(doc, "HTTP 400 (Invalid ObjectID format), HTTP 404 (Restaurant not found).", bold_prefix="Possible Errors: ")

    add_sub_sub_heading(doc, "4) POST /api/cart/items")
    add_bullet(doc, "Bearer Token (Customer role required).", bold_prefix="Authentication: ")
    add_bullet(doc, "JSON object containing restaurantId, menuItemId, quantity (positive integer), and specialNotes.", bold_prefix="Request Body: ")
    add_bullet(doc, "HTTP 200 OK with updated cart items, subtotal, and item count.", bold_prefix="Expected Response: ")
    add_bullet(doc, "HTTP 400 (Negative/zero quantity), HTTP 404 (Item/restaurant not found), HTTP 409 (Items from multiple restaurants in single cart).", bold_prefix="Possible Errors: ")

    add_sub_sub_heading(doc, "5) POST /api/orders")
    add_bullet(doc, "Bearer Token (Customer role required).", bold_prefix="Authentication: ")
    add_bullet(doc, "JSON object containing deliveryAddressId, paymentMethod, and optional voucherCode.", bold_prefix="Request Body: ")
    add_bullet(doc, "HTTP 201 Created with order summary, orderId, totalAmount, and status 'PENDING'.", bold_prefix="Expected Response: ")
    add_bullet(doc, "HTTP 400 (Empty cart or missing address), HTTP 404 (Cart not found), HTTP 422 (Restaurant currently closed or item out of stock).", bold_prefix="Possible Errors: ")

    add_sub_sub_heading(doc, "6) PATCH /api/orders/:id")
    add_bullet(doc, "Bearer Token (Restaurant Partner or Administrator).", bold_prefix="Authentication: ")
    add_bullet(doc, "JSON object containing status (e.g., 'ACCEPTED', 'PREPARING', 'REJECTED') and optional reason.", bold_prefix="Request Body: ")
    add_bullet(doc, "HTTP 200 OK with updated order document and transition timestamp.", bold_prefix="Expected Response: ")
    add_bullet(doc, "HTTP 400 (Invalid status string), HTTP 403 (Caller does not own restaurant), HTTP 404 (Order not found), HTTP 422 (Illegal state transition).", bold_prefix="Possible Errors: ")

    add_image_figure(doc, "fig3_order_processing_flow.png", "Fig. 3. Order Lifecycle State Machine and Transition Integrity Rules.")

    add_sub_heading(doc, "D. CRUD Operations Analysis")
    add_para(doc, "The mapping between persistent operations, HTTP methods, and system entities is summarized in Table IV:")

    headers_t4 = ["Operation", "HTTP Method", "Target Collection", "Validation & Security Controls"]
    rows_t4 = [
        ["Create User", "POST", "users", "Schema validation on email, password hashing via bcrypt (salt factor 10), unique constraint."],
        ["Read Restaurant", "GET", "restaurants", "Public read, route parameter format check, query filtering, projection of active merchants."],
        ["Create Menu Item", "POST", "menuItems", "RBAC guard (Restaurant owner only), foreign key restaurantId validation, price >= 0 check."],
        ["Update Cart", "POST", "carts", "Atomic upsert on customerId, quantity boundary check, single restaurant integrity check."],
        ["Delete Cart Item", "DELETE", "carts", "RBAC guard (Customer only), verification of item existence in active cart document."],
        ["Create Order", "POST", "orders", "Atomic transaction converting cart items to order document, stock verification, subtotal computation."],
        ["Update Order Status", "PATCH", "orders", "RBAC guard (Restaurant / Admin), state machine transition rules, audit log creation."],
        ["Update Delivery Status", "PATCH", "deliveries", "RBAC guard (Delivery rider only), OTP matching for final DELIVERED state confirmation."]
    ]
    build_academic_table(doc, headers_t4, rows_t4, caption="TABLE IV. CRUD OPERATIONS AND INTEGRITY CONTROLS MATRIX")

    print("Section V & VI generated successfully!")

print("build_section_arch_api module ready.")
