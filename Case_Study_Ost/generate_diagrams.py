import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set global styles
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def create_fig1():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Title box
    ax.text(50, 96, "Overall System Architecture: Food Delivery Web Services", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')

    # Color palette - academic clean
    c_client = '#EBF8FF'
    c_client_b = '#3182CE'
    c_gw = '#EDF2F7'
    c_gw_b = '#4A5568'
    c_api = '#F0FFF4'
    c_api_b = '#38A169'
    c_sec = '#FEFCBF'
    c_sec_b = '#D69E2E'
    c_db = '#FAF5FF'
    c_db_b = '#805AD5'
    c_test = '#FFF5F5'
    c_test_b = '#E53E3E'

    # 1. Clients Block (Top Left)
    box_client = patches.FancyBboxPatch((4, 72), 38, 18, boxstyle="round,pad=1", fc=c_client, ec=c_client_b, lw=1.5)
    ax.add_patch(box_client)
    ax.text(23, 87, "Client Presentation Layer", ha='center', va='center', fontsize=10, fontweight='bold', color='#2B6CB0')
    ax.text(23, 81, "• Customer Mobile App & Web Portal\n• Restaurant Management Dashboard\n• Delivery Personnel Mobile App\n• System Administrator Portal", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Postman Testing Client (Top Right)
    box_test = patches.FancyBboxPatch((58, 72), 38, 18, boxstyle="round,pad=1", fc=c_test, ec=c_test_b, lw=1.5, ls='--')
    ax.add_patch(box_test)
    ax.text(77, 87, "API Testing & Automation Client", ha='center', va='center', fontsize=10, fontweight='bold', color='#C53030')
    ax.text(77, 81, "• Postman Collection Runner\n• Pre-request Auth & Environment Vars\n• Automated Test Assertion Scripts (pm.test)\n• Negative & Boundary Scenario Suites", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Arrows down to Gateway
    ax.annotate('', xy=(30, 64), xytext=(23, 72), arrowprops=dict(facecolor='#4A5568', edgecolor='#4A5568', width=1.5, headwidth=6))
    ax.text(24, 67, "HTTPS / JSON", fontsize=7.5, fontweight='bold', color='#4A5568')
    
    ax.annotate('', xy=(70, 64), xytext=(77, 72), arrowprops=dict(facecolor='#E53E3E', edgecolor='#E53E3E', width=1.5, headwidth=6))
    ax.text(74, 67, "REST Verification", fontsize=7.5, fontweight='bold', color='#C53030')

    # 2. API Gateway & Reverse Proxy
    box_gw = patches.FancyBboxPatch((20, 56), 60, 8, boxstyle="round,pad=0.8", fc=c_gw, ec=c_gw_b, lw=1.5)
    ax.add_patch(box_gw)
    ax.text(50, 60, "API Gateway / Reverse Proxy (HTTPS, TLS 1.3, Rate Limiting, CORS Headers)", 
            ha='center', va='center', fontsize=9, fontweight='bold', color='#2D3748')

    # Arrow down to Backend
    ax.annotate('', xy=(50, 48), xytext=(50, 56), arrowprops=dict(facecolor='#4A5568', edgecolor='#4A5568', width=1.5, headwidth=6))

    # 3. Node.js & Express.js Backend Application Layer
    box_backend = patches.FancyBboxPatch((4, 18), 92, 30, boxstyle="round,pad=1.2", fc=c_api, ec=c_api_b, lw=1.5)
    ax.add_patch(box_backend)
    ax.text(50, 45, "Node.js & Express.js Application Server (REST API Backend)", 
            ha='center', va='center', fontsize=10, fontweight='bold', color='#22543D')

    # Sub-modules inside backend
    sub_modules = [
        ("Authentication & RBAC", "Token Verification\nRole Guards (Customer,\nRestaurant, Delivery, Admin)", 6, 21, 20, 20, c_sec, c_sec_b),
        ("Input Validation Layer", "Schema Validation\nType & Boundary Checks\nSanitization & Stripping", 28, 21, 20, 20, '#EDF2F7', '#718096'),
        ("Business Controllers", "Auth, Restaurant, Menu,\nCart, Order Lifecycle,\nDelivery Tracking Logic", 50, 21, 22, 20, '#EBF8FF', '#3182CE'),
        ("Error & Log Handler", "Central Error Catching\nStandard JSON Normalizer\nWinston Audit Logger", 74, 21, 20, 20, '#FFF5F5', '#E53E3E')
    ]

    for title, desc, x, y, w, h, bg, border in sub_modules:
        sb = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", fc=bg, ec=border, lw=1)
        ax.add_patch(sb)
        ax.text(x + w/2, y + h - 3.5, title, ha='center', va='center', fontsize=8, fontweight='bold', color='#1A202C')
        ax.text(x + w/2, y + 6.5, desc, ha='center', va='center', fontsize=7, color='#2D3748')

    # Arrows between sub-modules
    ax.annotate('', xy=(28, 31), xytext=(26, 31), arrowprops=dict(facecolor='#4A5568', edgecolor='#4A5568', width=1, headwidth=4))
    ax.annotate('', xy=(50, 31), xytext=(48, 31), arrowprops=dict(facecolor='#4A5568', edgecolor='#4A5568', width=1, headwidth=4))
    ax.annotate('', xy=(74, 31), xytext=(72, 31), arrowprops=dict(facecolor='#4A5568', edgecolor='#4A5568', width=1, headwidth=4))

    # Arrow down to Database
    ax.annotate('', xy=(50, 10), xytext=(50, 18), arrowprops=dict(facecolor='#805AD5', edgecolor='#805AD5', width=1.5, headwidth=6))
    ax.text(52, 14, "Mongoose ODM / TCP", fontsize=7.5, fontweight='bold', color='#6B46C1')

    # 4. Database Layer (MongoDB)
    box_db = patches.FancyBboxPatch((15, 1), 70, 9, boxstyle="round,pad=0.8", fc=c_db, ec=c_db_b, lw=1.5)
    ax.add_patch(box_db)
    ax.text(50, 6.5, "MongoDB Document Database", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#553C9A')
    ax.text(50, 3, "Collections: users  |  restaurants  |  menuItems  |  carts  |  orders  |  deliveries", 
            ha='center', va='center', fontsize=8, color='#4A5568')

    plt.tight_layout()
    plt.savefig('fig1_system_architecture.png', dpi=300)
    plt.close()
    print("Fig 1 generated successfully!")

def create_fig2():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "API Request/Response Validation and Processing Flow", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')

    steps = [
        ("1. HTTP Request", "Client / Postman sends\nMethod, Headers, Body", 3, 40, 14, 24, '#EBF8FF', '#3182CE'),
        ("2. Rate Limiting", "Check IP/Token request\nfrequency window", 19, 40, 14, 24, '#EDF2F7', '#4A5568'),
        ("3. Auth & RBAC", "Validate Token & verify\nendpoint permissions", 35, 40, 14, 24, '#FEFCBF', '#D69E2E'),
        ("4. Request Validation", "Validate schema, types,\nrequired attributes", 51, 40, 14, 24, '#EDF2F7', '#4A5568'),
        ("5. Controller Logic", "Execute business rules\n& DB transactions", 67, 40, 14, 24, '#F0FFF4', '#38A169'),
        ("6. Response Format", "Construct structured\nSuccess JSON", 83, 40, 14, 24, '#EBF8FF', '#3182CE'),
    ]

    for title, desc, x, y, w, h, bg, border in steps:
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", fc=bg, ec=border, lw=1.2)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - 5, title, ha='center', va='center', fontsize=8, fontweight='bold', color='#1A202C')
        ax.text(x + w/2, y + 8, desc, ha='center', va='center', fontsize=7, color='#2D3748')

    # Main pipeline arrows
    for i in range(len(steps)-1):
        x_from = steps[i][2] + steps[i][4]
        x_to = steps[i+1][2]
        ax.annotate('', xy=(x_to, 52), xytext=(x_from, 52), arrowprops=dict(facecolor='#2B6CB0', edgecolor='#2B6CB0', width=1.2, headwidth=4))

    # Error Catching Layer below
    err_box = patches.FancyBboxPatch((15, 8), 70, 18, boxstyle="round,pad=0.8", fc='#FFF5F5', ec='#E53E3E', lw=1.5)
    ax.add_patch(err_box)
    ax.text(50, 21, "Centralized Error Handling Middleware (next(err))", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#C53030')
    ax.text(50, 13, "• Normalizes Error Codes (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests, 500 Server Error)\n• Sanitizes internal stack traces and database details\n• Formats standardized JSON response: { success: false, error: { code, message, timestamp } }", 
            ha='center', va='center', fontsize=7.5, color='#4A5568')

    # Error arrows pointing down from steps to error box
    error_points = [
        (26, "429 Limit Exceeded"),
        (42, "401/403 Auth Fail"),
        (58, "400 Invalid Input"),
        (74, "404/500 Logic/DB Error")
    ]
    for x, lbl in error_points:
        ax.annotate('', xy=(x, 26), xytext=(x, 40), arrowprops=dict(facecolor='#E53E3E', edgecolor='#E53E3E', width=1, headwidth=4, ls='--'))
        ax.text(x, 33, lbl, ha='center', va='center', fontsize=6.5, color='#C53030', backgroundcolor='white')

    # Success return arrow
    ax.annotate('', xy=(90, 78), xytext=(90, 64), arrowprops=dict(facecolor='#38A169', edgecolor='#38A169', width=1.2, headwidth=4))
    success_box = patches.FancyBboxPatch((78, 78), 20, 12, boxstyle="round,pad=0.5", fc='#F0FFF4', ec='#38A169', lw=1.2)
    ax.add_patch(success_box)
    ax.text(88, 86, "200 OK / 201 Created", ha='center', va='center', fontsize=8, fontweight='bold', color='#22543D')
    ax.text(88, 81, "Valid JSON payload", ha='center', va='center', fontsize=7, color='#2D3748')

    plt.tight_layout()
    plt.savefig('fig2_request_response_flow.png', dpi=300)
    plt.close()
    print("Fig 2 generated successfully!")

def create_fig3():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "Order Lifecycle and State Machine Flowchart", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')

    states = [
        ("CART_BUILDING", "Customer adds / modifies items\nPOST /api/cart/items", 3, 60, 14, 22, '#EDF2F7', '#4A5568'),
        ("ORDER_PLACED", "Checkout validated & created\nPOST /api/orders (201)", 19, 60, 14, 22, '#EBF8FF', '#3182CE'),
        ("CONFIRMED", "Restaurant reviews & accepts\nPATCH /api/orders/:id", 35, 60, 14, 22, '#FEFCBF', '#D69E2E'),
        ("PREPARING", "Kitchen prepares food items\nStatus: 'PREPARING'", 51, 60, 14, 22, '#FEFCBF', '#D69E2E'),
        ("OUT_FOR_DELIVERY", "Rider assigned & picked up\nPATCH /api/deliveries/:id", 67, 60, 15, 22, '#FAF5FF', '#805AD5'),
        ("DELIVERED", "Order handed over to customer\nStatus: 'DELIVERED'", 84, 60, 14, 22, '#F0FFF4', '#38A169'),
    ]

    for title, desc, x, y, w, h, bg, border in states:
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", fc=bg, ec=border, lw=1.2)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - 5, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1A202C')
        ax.text(x + w/2, y + 7, desc, ha='center', va='center', fontsize=6.5, color='#2D3748')

    for i in range(len(states)-1):
        x_from = states[i][2] + states[i][4]
        x_to = states[i+1][2]
        ax.annotate('', xy=(x_to, 71), xytext=(x_from, 71), arrowprops=dict(facecolor='#2B6CB0', edgecolor='#2B6CB0', width=1.2, headwidth=4))

    # Cancelled / Rejected branch below
    cancel_box = patches.FancyBboxPatch((27, 16), 18, 20, boxstyle="round,pad=0.5", fc='#FFF5F5', ec='#E53E3E', lw=1.2)
    ax.add_patch(cancel_box)
    ax.text(36, 31, "CANCELLED / REJECTED", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#C53030')
    ax.text(36, 22, "• Customer cancellation\n• Restaurant item stockout\n• Delivery partner unavailable", 
            ha='center', va='center', fontsize=6.5, color='#2D3748')

    # Arrows to cancelled
    ax.annotate('', xy=(31, 36), xytext=(26, 60), arrowprops=dict(facecolor='#E53E3E', edgecolor='#E53E3E', width=1, headwidth=4, ls='--'))
    ax.text(25, 47, "User Cancel", fontsize=6.5, color='#C53030')

    ax.annotate('', xy=(39, 36), xytext=(42, 60), arrowprops=dict(facecolor='#E53E3E', edgecolor='#E53E3E', width=1, headwidth=4, ls='--'))
    ax.text(42, 47, "Reject", fontsize=6.5, color='#C53030')

    # Guard rules note
    note_box = patches.FancyBboxPatch((55, 16), 40, 20, boxstyle="round,pad=0.5", fc='#EDF2F7', ec='#718096', lw=1)
    ax.add_patch(note_box)
    ax.text(75, 31, "State Transition Integrity Guard", ha='center', va='center', fontsize=8, fontweight='bold', color='#2D3748')
    ax.text(75, 22, "• Strict validation prevents invalid state jumps (e.g. CART directly to DELIVERED)\n• PATCH requests verify actor permissions (only restaurant can accept, only rider can deliver)\n• Incompatible transitions trigger HTTP 422 Unprocessable Entity", 
            ha='center', va='center', fontsize=6.5, color='#4A5568')

    plt.tight_layout()
    plt.savefig('fig3_order_processing_flow.png', dpi=300)
    plt.close()
    print("Fig 3 generated successfully!")

def create_fig4():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Centralized Error-Handling and Normalization Flow", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')

    # Error sources on Left
    sources = [
        ("Input Validation Error", "Missing fields, bad types, negative numbers", 3, 73, 24, 14, '#FFF5F5', '#E53E3E'),
        ("Authentication & RBAC Error", "Missing token, expired JWT, forbidden role", 3, 53, 24, 14, '#FEFCBF', '#D69E2E'),
        ("Business Domain Error", "Resource missing, invalid order state, empty cart", 3, 33, 24, 14, '#FAF5FF', '#805AD5'),
        ("Database / System Exception", "Mongo CastError, connection failure, 500 crash", 3, 13, 24, 14, '#EDF2F7', '#4A5568'),
    ]

    for title, desc, x, y, w, h, bg, border in sources:
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", fc=bg, ec=border, lw=1)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - 4, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1A202C')
        ax.text(x + w/2, y + 4, desc, ha='center', va='center', fontsize=6.5, color='#4A5568')
        ax.annotate('', xy=(34, 50), xytext=(x + w, y + h/2), arrowprops=dict(facecolor='#E53E3E', edgecolor='#E53E3E', width=1, headwidth=4))

    # Central Handler in Center
    ch_box = patches.FancyBboxPatch((34, 25), 32, 50, boxstyle="round,pad=0.8", fc='#FFF5F5', ec='#C53030', lw=2)
    ax.add_patch(ch_box)
    ax.text(50, 70, "Central Error Middleware\napp.use((err, req, res, next))", 
            ha='center', va='center', fontsize=9, fontweight='bold', color='#C53030')
    ax.text(50, 48, "1. Identify Error Class / Name\n2. Assign HTTP Status (400, 401, 403, 404, 422, 500)\n3. Sanitize Stack Traces & DB Internals\n4. Write Audit Log to Winston / Console\n5. Produce Standard Error Object", 
            ha='center', va='center', fontsize=7.5, color='#2D3748')

    # Output paths on Right
    ax.annotate('', xy=(72, 65), xytext=(66, 60), arrowprops=dict(facecolor='#3182CE', edgecolor='#3182CE', width=1.2, headwidth=4))
    ax.annotate('', xy=(72, 35), xytext=(66, 40), arrowprops=dict(facecolor='#4A5568', edgecolor='#4A5568', width=1.2, headwidth=4))

    # Standard JSON Response (Right Top)
    resp_box = patches.FancyBboxPatch((72, 52), 25, 32, boxstyle="round,pad=0.5", fc='#EBF8FF', ec='#3182CE', lw=1.2)
    ax.add_patch(resp_box)
    ax.text(84.5, 78, "Client JSON Response", ha='center', va='center', fontsize=8, fontweight='bold', color='#2B6CB0')
    ax.text(84.5, 64, "{\n  \"success\": false,\n  \"error\": {\n    \"code\": \"INVALID_INPUT\",\n    \"message\": \"Detailed msg\",\n    \"timestamp\": \"ISO...\"\n  }\n}", 
            ha='center', va='center', fontsize=6.5, family='monospace', color='#1A202C')

    # Internal Audit Log (Right Bottom)
    log_box = patches.FancyBboxPatch((72, 16), 25, 28, boxstyle="round,pad=0.5", fc='#EDF2F7', ec='#4A5568', lw=1.2)
    ax.add_patch(log_box)
    ax.text(84.5, 38, "Internal Audit Logger", ha='center', va='center', fontsize=8, fontweight='bold', color='#2D3748')
    ax.text(84.5, 27, "• Full error stack trace\n• Request IP, Method, URI\n• User ID & Timestamp\n• Never exposed to client", 
            ha='center', va='center', fontsize=6.5, color='#4A5568')

    plt.tight_layout()
    plt.savefig('fig4_error_handling_flow.png', dpi=300)
    plt.close()
    print("Fig 4 generated successfully!")

def create_fig5():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "API Testing Strategy and Postman Automation Workflow", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')

    phases = [
        ("Phase 1: Test Design", "• Contract Definition\n• Equivalence Partitioning\n• Boundary Value Analysis\n• Security & RBAC Scenarios", 3, 45, 17, 34, '#EDF2F7', '#4A5568'),
        ("Phase 2: Postman Setup", "• Environment Variables\n• Base URL & Tokens\n• Pre-request Scripts\n• Dynamic payload setup", 22, 45, 17, 34, '#FEFCBF', '#D69E2E'),
        ("Phase 3: Execution", "• Postman Collection Runner\n• Positive & Negative Suites\n• Boundary Value Checks\n• Automated Script Triggers", 41, 45, 17, 34, '#EBF8FF', '#3182CE'),
        ("Phase 4: Validation", "• HTTP Status Assertions\n• JSON Schema Validation\n• Response Time Thresholds\n• Error Code Verification", 60, 45, 17, 34, '#F0FFF4', '#38A169'),
        ("Phase 5: Reporting", "• Test Pass/Fail Logging\n• Defect Identification\n• Regression Suite Update\n• Reliability Evaluation", 79, 45, 18, 34, '#FFF5F5', '#E53E3E'),
    ]

    for title, desc, x, y, w, h, bg, border in phases:
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", fc=bg, ec=border, lw=1.2)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - 5, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1A202C')
        ax.text(x + w/2, y + 12, desc, ha='center', va='center', fontsize=6.5, color='#2D3748')

    for i in range(len(phases)-1):
        x_from = phases[i][2] + phases[i][4]
        x_to = phases[i+1][2]
        ax.annotate('', xy=(x_to, 62), xytext=(x_from, 62), arrowprops=dict(facecolor='#3182CE', edgecolor='#3182CE', width=1.2, headwidth=4))

    # Bottom Feedback loop
    feed_box = patches.FancyBboxPatch((15, 8), 70, 22, boxstyle="round,pad=0.6", fc='#FAF5FF', ec='#805AD5', lw=1.2)
    ax.add_patch(feed_box)
    ax.text(50, 24, "Continuous Regression & Reliability Feedback Loop", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#553C9A')
    ax.text(50, 14, "Automated Postman collections executed on every API modification to prevent regression defects.\nVerifies that boundary checks, authentication guards, and centralized error formats remain consistently enforced.", 
            ha='center', va='center', fontsize=7, color='#4A5568')

    ax.annotate('', xy=(11, 45), xytext=(20, 26), arrowprops=dict(facecolor='#805AD5', edgecolor='#805AD5', width=1, headwidth=4, ls='--'))
    ax.annotate('', xy=(80, 26), xytext=(88, 45), arrowprops=dict(facecolor='#805AD5', edgecolor='#805AD5', width=1, headwidth=4, ls='--'))

    plt.tight_layout()
    plt.savefig('fig5_api_testing_workflow.png', dpi=300)
    plt.close()
    print("Fig 5 generated successfully!")

create_fig1()
create_fig2()
create_fig3()
create_fig4()
create_fig5()
