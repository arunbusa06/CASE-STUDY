from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor
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

def generate_section_sdg_challenges(doc):
    print("Generating Section X (SDG Mapping), XI (Challenges), XII (Conclusion), References, and Appendix...")

    # ==========================================
    # SECTION X: SDG MAPPING AND JUSTIFICATION
    # ==========================================
    add_sec_heading(doc, "X. SDG MAPPING AND JUSTIFICATION")
    
    add_para(doc,
        "The United Nations Sustainable Development Goals (SDGs) establish a global blueprint for peace, prosperity, and sustainable development. "
        "The engineering of robust software systems directly influences societal modernization and infrastructural resilience. This case study "
        "explicitly aligns with Sustainable Development Goal 9: Industry, Innovation, and Infrastructure."
    )

    add_sub_heading(doc, "A. Alignment with SDG 9 (Industry, Innovation, and Infrastructure)")
    add_para(doc,
        "SDG 9 mandates the construction of resilient infrastructure, the promotion of inclusive and sustainable industrialization, and the fostering "
        "of innovation. In contemporary digital economies, physical infrastructure (such as supply chains, transit networks, and merchant commerce) is "
        "inextricably coupled to digital web service infrastructure. REST APIs represent the foundational utility pipes of this digital ecosystem."
    )

    add_bullet(doc, "The proposed architecture establishes dependable, standards-compliant web service communication that powers hyperlocal digital commerce and logistics networks.", bold_prefix="Digital Infrastructure: ")
    add_bullet(doc, "By enforcing rigorous API validation and systematic error handling, the system eliminates sudden service crashes, guaranteeing uninterrupted web service availability for local merchants and consumers.", bold_prefix="Reliable Web Services: ")
    add_bullet(doc, "Deploying automated testing harnesses (Postman) and stateless modern runtimes (Node.js/Express) demonstrates software engineering innovation, shifting quality verification left in the development lifecycle.", bold_prefix="Software Engineering Innovation: ")
    add_bullet(doc, "Defensive error mediation, graceful degradation, and uniform status code reporting ensure that software services remain operational and recover predictably under extreme operational workloads.", bold_prefix="API Reliability & Fault Tolerance: ")
    add_bullet(doc, "The cloud-neutral, containerizable architecture scales horizontally to accommodate expanding urban populations and burgeoning merchant participation without architectural redesign.", bold_prefix="Scalable Digital Architecture: ")
    add_bullet(doc, "Cryptographic token verification, role-based guards, and automated input sanitization protect citizens' personal and financial data, building trust in digital public services.", bold_prefix="Secure Digital Services: ")

    add_sub_heading(doc, "B. SDG 9 Technical Mapping Matrix")
    add_para(doc, "Table X maps specific technical components of the proposed food delivery API to core SDG 9 targets:")

    headers_tsdg = ["SDG 9 Target / Aspect", "Case Study Technical Contribution & Architectural Implementation"]
    rows_tsdg = [
        ["Target 9.1: Quality, reliable, sustainable, and resilient infrastructure", "Implementation of standardized REST API contracts, connection pooling, and centralized error handling guaranteeing high-availability digital ordering infrastructure."],
        ["Target 9.3: Increase access of small-scale enterprises to financial services & markets", "Providing an open, standardized API platform allowing small and medium restaurant merchants to connect seamlessly to broader urban consumer markets."],
        ["Target 9.4: Upgrade infrastructure and retrofit industries to make them sustainable", "Modernizing legacy manual dispatch and ordering mechanisms through automated, cloud-neutral Node.js web services and containerized microservice architectures."],
        ["Target 9.b: Support domestic technology development, research, and innovation", "Leveraging open-source web technologies (Node.js, Express, MongoDB) and open standards (REST, JSON, JWT) to cultivate accessible software innovation."],
        ["Digital Public Trust & Data Protection", "Embedding OWASP API security hardening, input sanitization, and credential encryption to protect consumer privacy and promote inclusive digital commerce."]
    ]
    build_academic_table(doc, headers_tsdg, rows_tsdg, caption="TABLE X. SDG 9 TECHNICAL ALIGNMENT AND MAPPING MATRIX")

    # ==========================================
    # SECTION XI: CHALLENGES AND RECOMMENDATIONS
    # ==========================================
    add_sec_heading(doc, "XI. CHALLENGES AND RECOMMENDATIONS")
    
    add_para(doc,
        "The conceptualization, design, and validation of enterprise-grade food delivery web services present multifaceted software engineering "
        "challenges across architectural, operational, and testing dimensions."
    )

    add_sub_heading(doc, "A. Technical Challenges")
    add_bullet(doc, "Coordinating atomic updates across shopping carts, payment verifications, and restaurant order queues in a distributed NoSQL database requires sophisticated compensation logic or two-phase commit patterns.", bold_prefix="Distributed State Synchronization: ")
    add_bullet(doc, "Calculating dynamic delivery ETAs, routing waypoints, and rider proximity queries under high concurrency introduces computational complexity on the Node.js event-loop.", bold_prefix="Real-Time Geospatial Computation: ")

    add_sub_heading(doc, "B. API Testing Challenges")
    add_bullet(doc, "Testing temporal order progression (e.g., waiting for kitchen preparation before courier pickup) requires stateful chaining across multiple asynchronous Postman requests.", bold_prefix="Stateful Workflow Orchestration: ")
    add_bullet(doc, "Accurately mocking external dependencies (such as bank payment gateways and SMS notification providers) without incurring operational costs or false positives during CI regression runs.", bold_prefix="Third-Party Service Mocking: ")

    add_sub_heading(doc, "C. Security and Error-Handling Challenges")
    add_bullet(doc, "Balancing the delivery of informative error messages for client-side debugging against the strict imperative to prevent internal schema and stack-trace leakage in public environments.", bold_prefix="Information Disclosure vs. Usability: ")
    add_bullet(doc, "Preventing stolen JWT tokens from being reused prior to expiration in the absence of heavy distributed session stores.", bold_prefix="Stateless Token Revocation: ")

    add_sub_heading(doc, "D. Recommendations for Engineering Implementation")
    add_bullet(doc, "Strictly mandate schema validation at the HTTP routing boundary before any request context touches controller code.", bold_prefix="1) Enforce Fail-Fast Validation: ")
    add_bullet(doc, "Adopt an immutable JSON response envelope across the entire organization, ensuring identical key structures for success and failure states.", bold_prefix="2) Standardize Response Envelopes: ")
    add_bullet(doc, "Embed automated Postman collections into continuous deployment pipelines, gating production releases on 100% test pass rates.", bold_prefix="3) Shift Quality Verification Left: ")
    add_bullet(doc, "Deploy multi-tier rate limiting to isolate public endpoints from denial-of-service surges and brute-force credential stuffing.", bold_prefix="4) Implement Defensive Rate Limiting: ")
    add_bullet(doc, "Enforce strict separation between internal log repositories (storing complete stack traces) and client-facing error payloads (storing sanitized strings).", bold_prefix="5) Isolate Internal Diagnostics: ")

    add_sub_heading(doc, "E. Roadmap for Future Improvements")
    add_para(doc, "Future iterations of the proposed food delivery web service architecture can incorporate several advanced technologies:")
    add_bullet(doc, "Integrate Swagger / OpenAPI 3.0 specifications to generate machine-readable contracts, interactive developer documentation, and automated client SDKs.", bold_prefix="OpenAPI Specification: ")
    add_bullet(doc, "Incorporate automated API security scanning tools (such as OWASP ZAP) into the CI/CD pipeline to detect injection and header vulnerabilities dynamically.", bold_prefix="Automated Security Scanning: ")
    add_bullet(doc, "Introduce Redis in-memory caching for frequently queried restaurant catalogs and menu items to reduce database query pressure during lunch/dinner surges.", bold_prefix="Distributed Redis Caching: ")
    add_bullet(doc, "Deploy Prometheus and Grafana telemetry dashboards to visualize real-time HTTP error rates, p99 latencies, and route throughput.", bold_prefix="Telemetry & Observability Dashboards: ")
    add_bullet(doc, "Transition to Semantic API Versioning (e.g., /api/v1, /api/v2) to support backward-compatible evolution without breaking deployed mobile client apps.", bold_prefix="Structured API Versioning: ")

    # ==========================================
    # SECTION XII: CONCLUSION
    # ==========================================
    add_sec_heading(doc, "XII. CONCLUSION")
    
    add_para(doc,
        "This case study presented a comprehensive, academically grounded software engineering architecture and quality assurance strategy for an on-demand "
        "food delivery web service. Operating within a cloud-neutral technology stack comprising Node.js, Express.js, and MongoDB, the study addressed the "
        "critical necessity of establishing dependable REST API interfaces connecting customers, restaurant partners, delivery couriers, and administrators."
    )

    add_para(doc,
        "By systematically analyzing fourteen distinct failure modes—spanning malformed input types, broken authentication states, unauthorized horizontal "
        "privilege escalations, database connection drops, and sensitive error disclosure—the study established that software reliability is fundamentally "
        "governed by API boundary discipline and error-handling resilience. The proposed solution demonstrated how schema-based request validation, "
        "stateless JWT authentication, declarative role guards, centralized error-handling middleware, and standardized JSON response envelopes collectively "
        "prevent catastrophic runtime crashes and protect system availability."
    )

    add_para(doc,
        "Furthermore, the deployment of Postman as an automated testing harness established a repeatable methodology for positive acceptance, negative exception "
        "probing, boundary value analysis, and CI/CD regression verification. Mapping the proposed architecture to UN Sustainable Development Goal 9 (SDG 9: "
        "Industry, Innovation, and Infrastructure) demonstrated that rigorous web service engineering forms the indispensable foundation of modern digital "
        "infrastructure and inclusive commercial innovation. Ultimately, this case study underscores that high software reliability is achieved not through "
        "accidental runtime stability, but through deliberate architectural design, defensive error handling, and exhaustive API verification."
    )

    # ==========================================
    # REFERENCES (AUTHENTIC IEEE FORMAT)
    # ==========================================
    add_sec_heading(doc, "REFERENCES")
    
    refs = [
        "[1] R. Fielding and J. Reschke, Eds., \"HTTP Semantics,\" RFC 9110, Internet Engineering Task Force (IETF), Jun. 2022, doi: 10.17487/RFC9110.",
        "[2] M. Jones, J. Bradley, and N. Sakimura, \"JSON Web Token (JWT),\" RFC 7519, Internet Engineering Task Force (IETF), May 2015, doi: 10.17487/RFC7519.",
        "[3] Postman Inc., \"Postman API Platform Documentation: Automated API Testing and Test Scripts,\" Postman Docs, 2026. [Online]. Available: https://learning.postman.com/docs/writing-scripts/test-scripts/",
        "[4] OWASP Foundation, \"OWASP API Security Top 10: 2023,\" Open Worldwide Application Security Project, Jun. 2023. [Online]. Available: https://owasp.org/www-project-api-security/",
        "[5] Express.js Project, \"Express.js Documentation: Error Handling in Express Applications,\" OpenJS Foundation, 2026. [Online]. Available: https://expressjs.com/en/guide/error-handling.html",
        "[6] Node.js Foundation, \"Node.js v20 LTS Runtime Documentation: Asynchronous Flow and Process Management,\" OpenJS Foundation, 2026. [Online]. Available: https://nodejs.org/docs/latest-v20.x/api/",
        "[7] MongoDB Inc., \"MongoDB Manual: Document Data Modeling, Indexing, and Replica Sets,\" MongoDB Docs, 2026. [Online]. Available: https://www.mongodb.com/docs/manual/",
        "[8] United Nations, \"Sustainable Development Goal 9: Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation,\" UN Department of Economic and Social Affairs, 2026. [Online]. Available: https://sdgs.un.org/goals/goal9"
    ]
    for r in refs:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(r)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8)

    # ==========================================
    # APPENDIX
    # ==========================================
    add_sec_heading(doc, "APPENDIX")

    add_sub_heading(doc, "Appendix A — System Architecture Diagram Reference")
    add_para(doc, "Refer to Fig. 1 in Section V for the complete architectural topology illustrating client tiers, API gateway, Node.js controllers, MongoDB collections, and the Postman automation harness.")

    add_sub_heading(doc, "Appendix B — Complete API Endpoint Reference Matrix")
    add_para(doc, "Refer to Table III in Section VI for the authoritative reference matrix defining all fifteen core endpoints, HTTP methods, access roles, and operational scopes.")

    add_sub_heading(doc, "Appendix C — Postman Test Automation Script Examples")
    add_para(doc, "The following representative JavaScript test script demonstrates automated status assertion, schema validation, and token extraction within Postman:")
    
    script_code = (
        "// Postman Test Script: Assert HTTP 200 OK & Validate JWT Response Contract\n"
        "pm.test(\"Status code is 200 OK\", function () {\n"
        "    pm.response.to.have.status(200);\n"
        "});\n\n"
        "pm.test(\"Response conforms to Standard JSON Envelope\", function () {\n"
        "    var jsonData = pm.response.json();\n"
        "    pm.expect(jsonData).to.have.property('success', true);\n"
        "    pm.expect(jsonData).to.have.property('data');\n"
        "    pm.expect(jsonData.data).to.have.property('token');\n"
        "    pm.expect(jsonData.data.user).to.have.property('role');\n"
        "    \n"
        "    // Dynamically persist JWT to Postman Environment for downstream tests\n"
        "    pm.environment.set(\"jwt_token\", jsonData.data.token);\n"
        "});\n\n"
        "pm.test(\"Response time within acceptable SLA threshold\", function () {\n"
        "    pm.expect(pm.response.responseTime).to.be.below(300);\n"
        "});"
    )
    add_code_snippet(doc, script_code)

    add_sub_heading(doc, "Appendix D — Standard Request and Response Payloads")
    add_para(doc, "The following JSON payloads represent the standardized success and error contracts enforced across all endpoints:")

    add_sub_sub_heading(doc, "1) Representative Successful Order Creation Response (HTTP 201 Created):")
    json_succ = (
        "{\n"
        "  \"success\": true,\n"
        "  \"data\": {\n"
        "    \"orderId\": \"ORD1001\",\n"
        "    \"customerId\": \"6501f177bcf86cd799439011\",\n"
        "    \"restaurantId\": \"6501f177bcf86cd799439022\",\n"
        "    \"items\": [\n"
        "      { \"menuItemId\": \"6501f177bcf86cd799439033\", \"name\": \"Margherita Pizza\", \"quantity\": 2, \"price\": 14.99 }\n"
        "    ],\n"
        "    \"totalAmount\": 29.98,\n"
        "    \"status\": \"PENDING\",\n"
        "    \"createdAt\": \"2026-09-27T10:15:30.000Z\"\n"
        "  }\n"
        "}"
    )
    add_code_snippet(doc, json_succ)

    add_sub_sub_heading(doc, "2) Representative Validation Failure Response (HTTP 400 Bad Request):")
    json_err_val = (
        "{\n"
        "  \"success\": false,\n"
        "  \"error\": {\n"
        "    \"code\": \"INVALID_REQUEST\",\n"
        "    \"message\": \"The request data is invalid.\",\n"
        "    \"timestamp\": \"2026-09-27T10:16:02.124Z\",\n"
        "    \"details\": [\n"
        "      { \"field\": \"quantity\", \"message\": \"Quantity must be a positive integer strictly between 1 and 50.\" },\n"
        "      { \"field\": \"deliveryAddressId\", \"message\": \"deliveryAddressId is required and must be a valid ObjectID.\" }\n"
        "    ]\n"
        "  }\n"
        "}"
    )
    add_code_snippet(doc, json_err_val)

    add_sub_sub_heading(doc, "3) Representative Authentication Failure Response (HTTP 401 Unauthorized):")
    json_err_auth = (
        "{\n"
        "  \"success\": false,\n"
        "  \"error\": {\n"
        "    \"code\": \"UNAUTHORIZED\",\n"
        "    \"message\": \"Authentication is required.\",\n"
        "    \"timestamp\": \"2026-09-27T10:16:45.542Z\"\n"
        "  }\n"
        "}"
    )
    add_code_snippet(doc, json_err_auth)

    add_sub_sub_heading(doc, "4) Representative Forbidden Access Response (HTTP 403 Forbidden):")
    json_err_forbid = (
        "{\n"
        "  \"success\": false,\n"
        "  \"error\": {\n"
        "    \"code\": \"FORBIDDEN\",\n"
        "    \"message\": \"Access denied. Caller lacks role permission for this endpoint.\",\n"
        "    \"timestamp\": \"2026-09-27T10:17:10.891Z\"\n"
        "  }\n"
        "}"
    )
    add_code_snippet(doc, json_err_forbid)

    add_sub_sub_heading(doc, "5) Representative Resource Not Found Response (HTTP 404 Not Found):")
    json_err_404 = (
        "{\n"
        "  \"success\": false,\n"
        "  \"error\": {\n"
        "    \"code\": \"ORDER_NOT_FOUND\",\n"
        "    \"message\": \"The requested order was not found.\",\n"
        "    \"timestamp\": \"2026-09-27T10:17:35.312Z\"\n"
        "  }\n"
        "}"
    )
    add_code_snippet(doc, json_err_404)

    add_sub_sub_heading(doc, "6) Representative Internal Server Error Response (HTTP 500 Internal Server Error):")
    json_err_500 = (
        "{\n"
        "  \"success\": false,\n"
        "  \"error\": {\n"
        "    \"code\": \"INTERNAL_SERVER_ERROR\",\n"
        "    \"message\": \"An unexpected error occurred. Please contact system support.\",\n"
        "    \"timestamp\": \"2026-09-27T10:18:00.001Z\",\n"
        "    \"correlationId\": \"err-92f7b4c2-9e23\"\n"
        "  }\n"
        "}"
    )
    add_code_snippet(doc, json_err_500)

    add_sub_heading(doc, "Appendix E — Centralized Error-Handling Middleware Implementation")
    add_para(doc, "The following production-ready Node.js/Express middleware implements centralized error normalization and secure logging:")

    middleware_code = (
        "// Centralized Error-Handling Middleware (errorHandler.js)\n"
        "const logger = require('./logger');\n\n"
        "const errorHandler = (err, req, res, next) => {\n"
        "  // Extract error attributes or establish defensive defaults\n"
        "  let statusCode = err.statusCode || 500;\n"
        "  let errorCode = err.code || 'INTERNAL_SERVER_ERROR';\n"
        "  let message = err.message || 'An unexpected error occurred.';\n\n"
        "  // Handle Mongoose CastError (Malformed ObjectID)\n"
        "  if (err.name === 'CastError') {\n"
        "    statusCode = 400;\n"
        "    errorCode = 'INVALID_ID_FORMAT';\n"
        "    message = `Invalid format for resource identifier: ${err.value}`;\n"
        "  }\n\n"
        "  // Handle Mongoose Duplicate Key Error (Unique index collision)\n"
        "  if (err.code === 11000) {\n"
        "    statusCode = 409;\n"
        "    errorCode = 'DUPLICATE_KEY_ERROR';\n"
        "    message = 'A record with that unique field already exists.';\n"
        "  }\n\n"
        "  // Log detailed diagnostic trace internally (never sent to client)\n"
        "  logger.error({\n"
        "    message: err.message,\n"
        "    stack: err.stack,\n"
        "    method: req.method,\n"
        "    path: req.originalUrl,\n"
        "    ip: req.ip,\n"
        "    timestamp: new Date().toISOString()\n"
        "  });\n\n"
        "  // Return uniform, sanitized JSON envelope to client\n"
        "  res.status(statusCode).json({\n"
        "    success: false,\n"
        "    error: {\n"
        "      code: errorCode,\n"
        "      message: message,\n"
        "      timestamp: new Date().toISOString(),\n"
        "      ...(err.details && { details: err.details })\n"
        "    }\n"
        "  });\n"
        "};\n\n"
        "module.exports = errorHandler;"
    )
    add_code_snippet(doc, middleware_code)

    add_sub_heading(doc, "Appendix F — Professional Postman Verification Placeholders")
    add_para(doc, "In accordance with academic integrity guidelines, experimental results and visual artifacts are maintained as formal design verification placeholders:")

    placeholders = [
        "[Insert Screenshot: Postman Collection Organization and Environment Variables Setup]",
        "[Insert Screenshot: Successful Login API and Dynamic JWT Bearer Token Capture]",
        "[Insert Screenshot: Invalid Request / HTTP 400 Bad Request Response with Validation Details]",
        "[Insert Screenshot: Unauthorized Request / HTTP 401 Response on Missing Token]",
        "[Insert Screenshot: Forbidden Request / HTTP 403 Response on Role Privilege Violation]",
        "[Insert Screenshot: Resource Not Found / HTTP 404 Response on Invalid Entity Query]",
        "[Insert Screenshot: Postman Test Runner Summary: 100% Passed Assertions Across Master Test Suite]"
    ]
    for ph in placeholders:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(ph)
        run.bold = True
        run.font.name = "Consolas"
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor.from_string("4A5568")

    print("Section X, XI, XII, References, and Appendix generated successfully!")

print("build_section_sdg_challenges module ready.")
