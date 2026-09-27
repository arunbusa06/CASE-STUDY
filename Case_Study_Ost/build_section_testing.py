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

def generate_section_testing(doc):
    print("Generating Section VII: Software Quality and API Testing...")

    # ==========================================
    # SECTION VII: SOFTWARE QUALITY AND API TESTING
    # ==========================================
    add_sec_heading(doc, "VII. SOFTWARE QUALITY AND API TESTING")
    
    add_para(doc,
        "Software testing is an empirical investigation conducted to provide stakeholders with information about the quality of the software-under-test. "
        "In modern web service architectures, API testing represents a high-leverage verification stratum situated above unit tests and below end-to-end "
        "user-interface tests. Because REST APIs decouple business logic from client presentation, systematic API validation enables early defect detection, "
        "verifies contract conformance, and guarantees software reliability under adverse operational conditions."
    )

    add_sub_heading(doc, "A. Comprehensive Testing Strategy")
    add_para(doc,
        "The proposed testing framework adopts a multi-dimensional strategy designed to probe the API surface exhaustively. Testing encompasses functional "
        "verification of core business workflows, positive acceptance checks, negative exception paths, boundary value analysis, cryptographic authentication "
        "integrity, granular role-based authorization, schema compliance, error payload sanitization, security header defense, and continuous regression automation. "
        "Postman serves as the primary test execution engine, orchestrating automated assertion scripts, dynamic environment configurations, and collection runs."
    )

    add_image_figure(doc, "fig5_api_testing_workflow.png", "Fig. 4. Proposed API Testing Strategy, Verification Gates, and Postman Workflow.")

    add_sub_heading(doc, "B. Functional Testing")
    add_para(doc,
        "Functional testing verifies that each API endpoint performs its intended business capability in accordance with functional specifications. Workflows "
        "evaluated include full customer onboarding, restaurant menu catalog retrieval, multi-item shopping cart accumulation, checkout and order placement, "
        "restaurant order acceptance, courier pickup assignment, and real-time delivery status updates."
    )

    add_sub_heading(doc, "C. Positive Testing")
    add_para(doc,
        "Positive testing validates that endpoints behave correctly when presented with well-formed, valid input data within normal operational parameters. "
        "Assertions verify that the server returns HTTP 200 OK or HTTP 201 Created, responds within acceptable latency thresholds, and returns JSON payloads "
        "conforming strictly to expected response schemas."
    )

    add_sub_heading(doc, "D. Negative Testing")
    add_para(doc,
        "Negative testing evaluates the resilience of the API when subjected to invalid, malformed, or hostile inputs. Crucially, the system must not crash, "
        "expose stack traces, or corrupt persistence layers. Negative test scenarios include submitting duplicate registration emails, supplying incorrect passwords, "
        "referencing nonexistent resources, and sending corrupted JSON syntax. The API is expected to reject these requests gracefully with 4xx series HTTP status codes."
    )

    add_sub_heading(doc, "E. Boundary Value Testing")
    add_para(doc,
        "Boundary testing investigates system behavior at the extreme limits of input ranges. In a food delivery application, critical boundaries include "
        "item quantities (testing 0, 1, maximum allowable order thresholds such as 50 items, and overflow numbers), pricing boundaries (0.00 vs negative amounts), "
        "string lengths for delivery instructions (empty string, 1 character, 500-character boundary, and 501+ character overflows), and search radius coordinates."
    )

    add_sub_heading(doc, "F. Authentication Testing")
    add_para(doc,
        "Authentication testing probes the security of protected endpoints by attempting access with omitted Authorization headers, malformed Bearer schemes, "
        "expired tokens, forged JWT signatures, and invalid token secrets. In all failure cases, the API must consistently return HTTP 401 Unauthorized with "
        "standard error payloads."
    )

    add_sub_heading(doc, "G. Authorization Testing")
    add_para(doc,
        "Authorization testing verifies that users cannot access resources or execute operations outside their assigned role permissions. Scenarios evaluate "
        "Horizontal Privilege Escalation (e.g., Customer A attempting to view or cancel Customer B's order via /api/orders/:id) and Vertical Privilege "
        "Escalation (e.g., a Customer attempting to call PATCH /api/orders/:id to mark an order as 'DELIVERED'). Expected responses are strictly HTTP 403 Forbidden."
    )

    add_sub_heading(doc, "H. API Validation Testing")
    add_para(doc,
        "Validation testing verifies that request bodies, query strings, and path parameters satisfy all structural constraints before controller execution. "
        "Table V defines the proposed validation rules enforced across critical endpoints:"
    )

    headers_t5 = ["Entity / Endpoint", "Field Under Test", "Validation Rule & Constraint", "Failure HTTP Status"]
    rows_t5 = [
        ["User / Register", "email", "Mandatory; RFC 5322 compliant regex; normalized lowercase.", "HTTP 400 Bad Request"],
        ["User / Register", "password", "Minimum 8 chars; requires uppercase, lowercase, digit, special char.", "HTTP 400 Bad Request"],
        ["User / Register", "role", "Enumeration check: ['Customer', 'Restaurant', 'Delivery', 'Admin'].", "HTTP 400 Bad Request"],
        ["Restaurant / :id", ":id route parameter", "Valid 24-character hexadecimal BSON ObjectID string.", "HTTP 400 Bad Request"],
        ["Cart / Items", "quantity", "Positive integer strictly >= 1 and <= 50; rejects floats & strings.", "HTTP 400 Bad Request"],
        ["Order / Checkout", "deliveryAddressId", "Mandatory; valid ObjectID matching an active address for user.", "HTTP 400 Bad Request"],
        ["Order / Status", "status", "Enumeration matching legal state transitions: ['ACCEPTED', 'PREPARING', etc.].", "HTTP 422 Unprocessable"]
    ]
    build_academic_table(doc, headers_t5, rows_t5, caption="TABLE V. REQUEST VALIDATION AND BOUNDARY RULES MATRIX")

    add_sub_heading(doc, "I. Error-Handling Testing")
    add_para(doc,
        "Error-handling testing confirms that all internal server anomalies, database connectivity drops, and unhandled promise rejections are intercepted "
        "by the centralized error-handling middleware. The tests assert that: (1) no unhandled process crashes occur, (2) no stack traces or server file "
        "paths are leaked in client responses, (3) HTTP status codes accurately reflect error semantics (summarized in Table VI), and (4) the error payload "
        "strictly matches the standardized JSON contract."
    )

    headers_t6 = ["HTTP Code", "RFC 9110 Category", "System Usage in Food Delivery API", "Client Interpretation"]
    rows_t6 = [
        ["200 OK", "Successful", "Successful entity retrieval, menu browsing, cart update.", "Request succeeded; parse data object."],
        ["201 Created", "Successful", "Successful user registration, order creation, review creation.", "Resource created; parse generated ID."],
        ["400 Bad Request", "Client Error", "Validation failure, missing required fields, malformed ObjectID.", "Fix payload formatting and resubmit."],
        ["401 Unauthorized", "Client Error", "Missing, expired, or cryptographically invalid JWT token.", "Authenticate or refresh token."],
        ["403 Forbidden", "Client Error", "Authenticated user lacks role permissions for the endpoint.", "Access denied; elevate role permissions."],
        ["404 Not Found", "Client Error", "Referenced restaurant, order, menu item, or route not found.", "Entity does not exist; verify ID."],
        ["409 Conflict", "Client Error", "Duplicate email registration, items from multiple restaurants.", "Conflict with current resource state."],
        ["422 Unproc. Entity", "Client Error", "Illegal state transition (e.g. CART directly to DELIVERED).", "Syntactically valid but logically illegal."],
        ["429 Too Many Req.", "Client Error", "Rate limit exceeded (too many requests in window).", "Throttle requests; respect Retry-After."],
        ["500 Server Error", "Server Error", "Unhandled exception, database drop, internal crash.", "Server fault; alert operations team."]
    ]
    build_academic_table(doc, headers_t6, rows_t6, caption="TABLE VI. STANDARD HTTP ERROR CODES AND SEMANTIC USAGE")

    add_sub_heading(doc, "J. Security Testing")
    add_para(doc,
        "Security testing evaluates defenses against common API threats identified in the OWASP API Security Top 10. Probes evaluate NoSQL query injection "
        "(submitting MongoDB operators such as {'$ne': ''} within password fields), Cross-Site Scripting (XSS) input vectors in special dietary notes, "
        "Cross-Origin Resource Sharing (CORS) preflight validation, and verification of security response headers (X-Content-Type-Options, Strict-Transport-Security)."
    )

    add_sub_heading(doc, "K. Performance Testing Strategy")
    add_para(doc,
        "While this study does not claim empirical benchmark figures, it defines a structured performance testing protocol using Postman and load-generation "
        "tools. The protocol evaluates API response latency percentiles (p50, p95, p99), connection pool saturation under simulated concurrent users, and system "
        "throughput under sustained order submission workflows."
    )

    add_sub_heading(doc, "L. Continuous Regression Testing")
    add_para(doc,
        "Regression testing ensures that ongoing bug fixes and feature additions do not inadvertently degrade existing functionality or violate established API "
        "contracts. Postman collections are executed systematically through automated collection runs and CI pipelines (via Newman), validating hundreds of "
        "assertions on every code revision."
    )

    add_sub_heading(doc, "M. Postman Test Execution and Master Test Cases Matrix")
    add_para(doc,
        "Table VII provides a comprehensive master matrix of twenty-two representative test cases designed to validate the food delivery web service. "
        "The cases span positive, negative, boundary, authentication, authorization, and server-error scenarios, establishing a rigorous quality baseline:"
    )

    headers_tc = ["Test ID", "Target API Endpoint", "Test Scenario & Objective", "Representative Input Data", "Status", "Expected Result Envelope", "Testing Type"]
    rows_tc = [
        ["TC-01", "POST /api/auth/register", "Valid Customer Registration", "{name: 'Alice', email: 'alice@test.com', pass: 'Secret@123', role: 'Customer'}", "201", "{success: true, data: {userId: '...'}}", "Positive / Functional"],
        ["TC-02", "POST /api/auth/register", "Invalid Registration (Duplicate Email)", "{name: 'Alice', email: 'alice@test.com', pass: 'Secret@123'}", "409", "{success: false, error: {code: 'EMAIL_EXISTS'}}", "Negative / Integrity"],
        ["TC-03", "POST /api/auth/register", "Invalid Registration (Weak Password)", "{name: 'Bob', email: 'bob@test.com', pass: '123'}", "400", "{success: false, error: {code: 'INVALID_PASSWORD'}}", "Negative / Boundary"],
        ["TC-04", "POST /api/auth/login", "Valid User Login", "{email: 'alice@test.com', password: 'Secret@123'}", "200", "{success: true, data: {token: 'jwt...'}}", "Positive / Functional"],
        ["TC-05", "POST /api/auth/login", "Invalid Login (Bad Password)", "{email: 'alice@test.com', password: 'WrongPassword'}", "401", "{success: false, error: {code: 'INVALID_CREDENTIALS'}}", "Negative / Security"],
        ["TC-06", "GET /api/users/profile", "Missing Authorization Token", "Headers: { } (No Authorization header)", "401", "{success: false, error: {code: 'TOKEN_MISSING'}}", "Negative / Auth"],
        ["TC-07", "GET /api/users/profile", "Invalid / Tampered Bearer Token", "Headers: {Authorization: 'Bearer invalid.token.xyz'}", "401", "{success: false, error: {code: 'TOKEN_INVALID'}}", "Negative / Auth"],
        ["TC-08", "PATCH /api/orders/:id", "Unauthorized Operation (Customer -> Status)", "Role: Customer; Body: {status: 'DELIVERED'}", "403", "{success: false, error: {code: 'FORBIDDEN_ROLE'}}", "Negative / Authz"],
        ["TC-09", "GET /api/restaurants", "Valid Restaurant Catalog Fetch", "Query: ?cuisine=Italian&page=1&limit=10", "200", "{success: true, data: {restaurants: [...]}}", "Positive / Functional"],
        ["TC-10", "GET /api/restaurants/:id", "Valid Restaurant ID Request", "Param: :id = '507f1f77bcf86cd799439011'", "200", "{success: true, data: {name: 'Pasta Palace'}}", "Positive / Functional"],
        ["TC-11", "GET /api/restaurants/:id", "Invalid Restaurant ID Format", "Param: :id = 'invalid-mongo-id-123'", "400", "{success: false, error: {code: 'INVALID_ID_FORMAT'}}", "Negative / Validation"],
        ["TC-12", "GET /api/restaurants/:id", "Nonexistent Restaurant ID", "Param: :id = '507f1f77bcf86cd799439099' (not in DB)", "404", "{success: false, error: {code: 'RESTAURANT_NOT_FOUND'}}", "Negative / Exception"],
        ["TC-13", "POST /api/cart/items", "Valid Cart Item Addition", "{restaurantId: '...', menuItemId: '...', quantity: 2}", "200", "{success: true, data: {items: [...], subtotal: 30}}", "Positive / Functional"],
        ["TC-14", "POST /api/cart/items", "Negative Quantity Addition", "{restaurantId: '...', menuItemId: '...', quantity: -3}", "400", "{success: false, error: {code: 'INVALID_QUANTITY'}}", "Negative / Boundary"],
        ["TC-15", "POST /api/cart/items", "Quantity Upper Boundary (50 items)", "{restaurantId: '...', menuItemId: '...', quantity: 50}", "200", "{success: true, data: {items: [...]}}", "Boundary / Stress"],
        ["TC-16", "POST /api/cart/items", "Quantity Exceeding Boundary (51 items)", "{restaurantId: '...', menuItemId: '...', quantity: 51}", "400", "{success: false, error: {code: 'QUANTITY_EXCEEDED'}}", "Negative / Boundary"],
        ["TC-17", "POST /api/orders", "Empty Order Placement (Cart Empty)", "Active cart has 0 items; Body: {addressId: '...'}", "400", "{success: false, error: {code: 'EMPTY_CART'}}", "Negative / Business Logic"],
        ["TC-18", "POST /api/orders", "Valid Order Checkout", "{deliveryAddressId: '...', paymentMethod: 'CARD'}", "201", "{success: true, data: {orderId: 'ORD1001', status: 'PENDING'}}", "Positive / Functional"],
        ["TC-19", "POST /api/orders", "Order Placement at Closed Restaurant", "Target restaurant operationalStatus is 'CLOSED'", "422", "{success: false, error: {code: 'RESTAURANT_CLOSED'}}", "Negative / State Logic"],
        ["TC-20", "PATCH /api/orders/:id", "Illegal State Transition (PENDING -> DELIVERED)", "Body: {status: 'DELIVERED'} without prior states", "422", "{success: false, error: {code: 'ILLEGAL_TRANSITION'}}", "Negative / State Machine"],
        ["TC-21", "POST /api/cart/items", "Multi-Restaurant Cart Conflict", "Add item from Restaurant B when Cart has Restaurant A", "409", "{success: false, error: {code: 'RESTAURANT_CONFLICT'}}", "Negative / Integrity"],
        ["TC-22", "GET /api/orders/:id", "Simulated Database Connection Drop", "Database cluster unreachable / timeout triggered", "500", "{success: false, error: {code: 'INTERNAL_SERVER_ERROR'}}", "Negative / Reliability"]
    ]
    build_academic_table(doc, headers_tc, rows_tc, caption="TABLE VII. MASTER API TEST CASES SPECIFICATION MATRIX")

    print("Section VII generated successfully!")

print("build_section_testing module ready.")
