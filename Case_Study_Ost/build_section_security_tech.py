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

def generate_section_security_tech(doc):
    print("Generating Section VIII (Security & Reliability) and Section IX (Technical Analysis)...")

    # ==========================================
    # SECTION VIII: API SECURITY AND RELIABILITY ANALYSIS
    # ==========================================
    add_sec_heading(doc, "VIII. API SECURITY AND RELIABILITY ANALYSIS")
    
    add_para(doc,
        "In distributed food delivery platforms handling sensitive personal information, real-time geolocations, and financial transactions, "
        "security and reliability are co-dependent engineering requirements. Security failures inevitably degrade software reliability, while "
        "unreliable error-handling mechanisms expose critical security vulnerabilities. This section provides an architectural analysis of the "
        "security controls and reliability principles designed into the proposed system."
    )

    add_sub_heading(doc, "A. Authentication Security")
    add_para(doc,
        "User credentials are protected in storage through strong, irreversible cryptographic hashing using bcrypt with a recommended salt factor of 10. "
        "Plaintext passwords are never persisted or logged. Identity tokens are signed using HMAC-SHA256 (or RSA-256 for asymmetric verification) with "
        "strict expiration lifetimes (e.g., 60 minutes). Refresh tokens are stored in HttpOnly, SameSite, Secure cookies to mitigate Cross-Site Scripting (XSS) "
        "token exfiltration."
    )

    add_sub_heading(doc, "B. Granular Role-Based Authorization")
    add_para(doc,
        "To mitigate Broken Object Level Authorization (OWASP API1:2023) and Broken Function Level Authorization (OWASP API5:2023), every route handler "
        "enforces dual-stage verification: (1) functional role matching against the user's token claims, and (2) contextual ownership validation confirming "
        "that the authenticated user's ID matches the resource's owner or active assignment (e.g., a courier can only access deliveries assigned to their ID)."
    )

    add_sub_heading(doc, "C. Input Validation and Injection Sanitization")
    add_para(doc,
        "All incoming payloads are strictly validated against schema models before reaching controller logic. To defend against NoSQL injection exploits "
        "(where attackers inject MongoDB query operators such as {'$gt': ''} into request bodies), the application utilizes express-mongo-sanitize to "
        "strip dollar-sign ($) and dot (.) characters from user inputs automatically."
    )

    add_sub_heading(doc, "D. Secure API Communication")
    add_para(doc,
        "All network traffic is encrypted using Transport Layer Security (TLS 1.3 / HTTPS). Insecure HTTP requests are automatically redirected with "
        "HTTP 301. HTTP Strict Transport Security (HSTS) headers enforce HTTPS compliance on consuming clients, while Helmet middleware injects protective "
        "headers including X-Frame-Options (preventing clickjacking) and X-Content-Type-Options: nosniff (preventing MIME confusion attacks)."
    )

    add_sub_heading(doc, "E. Sensitive Data Protection")
    add_para(doc,
        "Sensitive customer attributes—including credit card numbers, CVVs, and raw payment nonces—are never stored in the application database; "
        "payment processing is delegated to PCI-DSS compliant third-party gateways. Customer phone numbers and addresses are masked in API responses "
        "served to couriers and restaurants once an order reaches terminal status."
    )

    add_sub_heading(doc, "F. Secure Error Messages and Information Masking")
    add_para(doc,
        "The centralized error handler guarantees that internal database error objects (such as MongoDB connection strings, schema collection names, or "
        "runtime stack traces) are entirely stripped in production responses. Clients receive only abstract, sanitized error descriptions and unique "
        "correlation identifiers for tracking, eliminating intelligence leakage."
    )

    add_image_figure(doc, "fig4_error_handling_flow.png", "Fig. 5. Centralized Error Normalization, Security Filtering, and Audit Pipeline.")

    add_sub_heading(doc, "G. Adaptive Rate Limiting")
    add_para(doc,
        "To safeguard the API against volumetric brute-force attacks and resource exhaustion, express-rate-limit enforces sliding-window quotas. "
        "Public authentication endpoints are restricted to 5 attempts per 15-minute window per IP, while general resource endpoints permit up to 100 "
        "requests per minute. Excess calls receive HTTP 429 Too Many Requests along with standard Retry-After headers."
    )

    add_sub_heading(doc, "H. Structured Logging and Monitoring")
    add_para(doc,
        "The Winston logging framework records application events into structured JSON format. Logs capture request HTTP method, endpoint URI, response status, "
        "execution latency, and authenticated user ID. Sensitive parameters (passwords, tokens) are intercepted and redacted by custom log sanitizers. "
        "High-severity 5xx exceptions trigger alerts to operational dashboards."
    )

    add_sub_heading(doc, "I. API Reliability and Fault Tolerance")
    add_para(doc,
        "System reliability is reinforced through defensive design patterns. Idempotency keys are supported on POST /api/orders to prevent duplicate "
        "order submissions during client network dropouts. Database operations utilize connection pooling and automated reconnection retry logic to survive "
        "transient network blips gracefully."
    )

    add_sub_heading(doc, "J. Database Backup and Disaster Recovery")
    add_para(doc,
        "MongoDB is configured in a high-availability Replica Set architecture featuring primary-secondary node replication with automated failover. "
        "Automated point-in-time snapshots and daily mongodump archives are exported to isolated, encrypted cloud object storage, ensuring low Recovery "
        "Time Objectives (RTO) and Recovery Point Objectives (RPO)."
    )

    add_sub_heading(doc, "K. Security Risk and Mitigation Analysis")
    add_para(doc, "A comprehensive risk matrix identifying potential threats, operational impacts, and proposed engineering mitigations is presented in Table VIII:")

    headers_tr = ["Security / Reliability Risk", "Potential Operational Impact", "Proposed Engineering Mitigation"]
    rows_tr = [
        ["Unauthorized Endpoint Access", "Data breach; leakage of customer PII and delivery addresses.", "Mandatory JWT verification; role-based guards on all private routes."],
        ["Invalid / Hostile Input", "Controller crashes; database corruption; NoSQL query injection.", "Multi-tier schema validation (express-validator); express-mongo-sanitize."],
        ["Token Misuse & Forgery", "Identity spoofing; unauthorized account manipulation.", "HMAC-SHA256 signatures; short token expiry (60m); secret rotation policy."],
        ["Excessive Volumetric Requests", "Denial of service; application server thread exhaustion; downtime.", "IP-based sliding window rate limiting (express-rate-limit) with 429 status."],
        ["Sensitive Information Leakage", "Attackers gain internal architectural blueprints and file paths.", "Centralized error handler strips stack traces and internal metadata in prod."],
        ["Database Connectivity Drops", "Unhandled promise rejections; service-wide HTTP 500 crashes.", "Mongoose connection pooling; exponential retry logic; 500 error catching."],
        ["API Regression Defects", "Deployed mobile client breakages; customer checkout failures.", "Automated Postman regression test suites integrated into CI/CD pipelines."],
        ["Data Loss & Inconsistency", "Permanent loss of order transaction history and merchant earnings.", "MongoDB Replica Sets with automated failover; daily encrypted snapshots."]
    ]
    build_academic_table(doc, headers_tr, rows_tr, caption="TABLE VIII. SECURITY RISKS, OPERATIONAL IMPACTS, AND MITIGATION MATRIX")

    # ==========================================
    # SECTION IX: TECHNICAL ANALYSIS
    # ==========================================
    add_sec_heading(doc, "IX. TECHNICAL ANALYSIS")
    
    add_para(doc,
        "This section evaluates the operational mechanics, architectural trade-offs, scalability dimensions, and performance characteristics of the "
        "proposed food delivery web service. In accordance with academic rigor, all evaluations represent proposed design capabilities rather than "
        "empirically measured deployment statistics."
    )

    add_sub_heading(doc, "A. Working Mechanics of the Proposed Solution")
    add_para(doc,
        "The proposed solution operates as an integrated pipeline. Incoming client requests traverse gateway rate-limiters, TLS termination, and CORS filters. "
        "Authentication middleware decodes the JWT token and binds user credentials to the Express request context. The validation layer scrutinizes the body, "
        "params, and query strings. Validated data enters domain controllers, which execute business logic and database queries using Mongoose models. "
        "If any step encounters a failure, execution halts and delegates to the central error middleware via next(error), which serializes a uniform JSON "
        "error response. Successful transactions yield standardized success payloads."
    )

    add_sub_heading(doc, "B. Advantages of the Architecture")
    add_bullet(doc, "Uniform JSON responses allow consuming mobile and web applications to implement deterministic parsing and centralized error rendering.", bold_prefix="Predictable Client Contracts: ")
    add_bullet(doc, "Consolidating error translation into a single middleware eliminates redundant try-catch error response formatting across dozens of controllers.", bold_prefix="Centralized Maintenance: ")
    add_bullet(doc, "Schema-based request filters halt malformed data at the network boundary, safeguarding controllers and database models from illegal states.", bold_prefix="Proactive Boundary Defense: ")
    add_bullet(doc, "Stateless JWT tokens enable frictionless horizontal scaling of Node.js worker processes behind reverse proxies without shared session memory.", bold_prefix="Horizontal Scalability: ")
    add_bullet(doc, "Automated Postman test collections provide verifiable regression safety nets, enabling rapid feature iterations without contract breakage.", bold_prefix="Quality Assurance Agility: ")

    add_sub_heading(doc, "C. Architectural Limitations")
    add_bullet(doc, "Stateless JWT tokens cannot be revoked instantly prior to expiration unless an explicit distributed token-denylist (e.g., Redis) is maintained.", bold_prefix="Token Revocation Latency: ")
    add_bullet(doc, "While MongoDB offers high write throughput, multi-document ACID transactions across distributed shards incur higher latency than traditional RDBMS.", bold_prefix="Distributed Transaction Overhead: ")
    add_bullet(doc, "Single-threaded event-loop execution requires careful avoidance of CPU-intensive algorithms (e.g., complex route optimization) on the main thread.", bold_prefix="Single-Threaded CPU Bottlenecks: ")

    add_sub_heading(doc, "D. Scalability Dimensions")
    add_para(doc,
        "Scalability is addressed along two primary vectors: application tier and data tier. The Node.js application tier achieves horizontal scalability "
        "by deploying stateless worker instances across containers (Docker) coordinated behind an Nginx reverse proxy or cloud load balancer. The database "
        "tier scales via MongoDB sharding, distributing collections across shard keys (such as restaurantId or geographic cluster) to balance write throughput."
    )

    add_sub_heading(doc, "E. Software Reliability Evaluation")
    add_para(doc,
        "Software reliability is elevated by systematically eliminating unhandled exception pathways. By intercepting database drops, schema mismatches, "
        "and illegal state jumps before they terminate the Node.js runtime process, Mean Time Between Failures (MTBF) is maximized, and graceful degradation "
        "is guaranteed."
    )

    add_sub_heading(doc, "F. Code Maintainability and Modularity")
    add_para(doc,
        "The architecture enforces strict separation of concerns following the Controller-Service-Repository pattern. Routes define endpoint URIs, validators "
        "enforce contracts, services execute domain logic, and ODM models handle persistence. This modularity reduces cognitive load for developers and simplifies "
        "unit and integration test creation."
    )

    add_sub_heading(doc, "G. Performance Analysis and Proposed Metrics")
    add_para(doc,
        "To establish a verifiable performance evaluation baseline for future empirical implementations, Table IX details proposed key performance indicators "
        "(KPIs) and their intended target envelopes under standard operational loads:"
    )

    headers_te = ["Evaluation Dimension", "Architectural Mechanism", "Proposed Target Envelope", "Verification Tool"]
    rows_te = [
        ["API Latency (Read Operations)", "Indexed MongoDB queries, lean projections, connection pooling.", "p95 <= 150 ms (Proposed Target)", "Postman / JMeter"],
        ["API Latency (Write / Orders)", "Atomic document creation, lightweight payload validation.", "p95 <= 250 ms (Proposed Target)", "Postman / JMeter"],
        ["Availability / Uptime", "Process supervisor (PM2), container auto-restart, health endpoints.", "99.9% Availability (Proposed Target)", "Uptime Robot / Prometheus"],
        ["Error Sanitization Rate", "Global 4-parameter Express error handler, Winston logger.", "100% Sanitization (Zero Stack Leakage)", "Postman Negative Assertions"],
        ["Authentication Overhead", "In-memory cryptographic JWT signature verification.", "Overhead <= 5 ms per request", "Postman Latency Profiler"],
        ["Test Assertion Coverage", "Modular Postman collections across all 15 endpoints.", "100% Contract Coverage (Proposed Target)", "Postman Collection Runner"]
    ]
    build_academic_table(doc, headers_te, rows_te, caption="TABLE IX. TECHNICAL EVALUATION AND PROPOSED PERFORMANCE ENVELOPES")

    print("Section VIII & IX generated successfully!")

print("build_section_security_tech module ready.")
