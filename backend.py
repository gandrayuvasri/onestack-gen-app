from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def init_db():
    conn = sqlite3.connect("C:/Users/shiva/data.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prompt TEXT,
        result TEXT,
        type TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

def generate_fake(prompt):
    prompt = prompt.lower()

    if "portfolio" in prompt:
        return "Portfolio Website:\n- Home\n- About Me\n- Projects\n- Skills\n- Contact Form\n- Resume Download"
    elif "ecommerce" in prompt or "shop" in prompt or "store" in prompt or "buy" in prompt:
        return "E-commerce Website:\n- Product Listing\n- Product Page\n- Cart\n- Checkout\n- Payment Gateway\n- Order Tracking"
    elif "blog" in prompt or "article" in prompt or "news" in prompt:
        return "Blog Website:\n- Homepage\n- Categories\n- Article Page\n- Comments Section\n- Search Bar\n- Newsletter"
    elif "landing" in prompt or "startup" in prompt or "saas" in prompt:
        return "Landing Page:\n- Hero Section\n- Features\n- Pricing\n- Testimonials\n- CTA Button\n- Footer"
    elif "restaurant" in prompt or "food" in prompt or "cafe" in prompt:
        return "Restaurant Website:\n- Menu Page\n- Online Ordering\n- Reservations\n- Gallery\n- Location Map"
    elif "dashboard" in prompt or "analytics" in prompt or "admin" in prompt:
        return "Dashboard:\n- Sidebar Navigation\n- Analytics Cards\n- Bar & Line Charts\n- User Table\n- Filters\n- Export Button"
    elif "sales" in prompt or "revenue" in prompt or "finance" in prompt:
        return "Sales Dashboard:\n- Revenue Chart\n- Top Products\n- Sales by Region\n- Monthly Targets\n- KPI Cards"
    elif "student" in prompt or "school" in prompt or "college" in prompt:
        return "Student Dashboard:\n- Attendance Tracker\n- Grades Table\n- Assignments\n- Timetable\n- Notifications"
    elif "hospital" in prompt or "doctor" in prompt or "patient" in prompt:
        return "Hospital Dashboard:\n- Patient Records\n- Appointment Scheduler\n- Doctor List\n- Bed Availability\n- Reports"
    elif "chat" in prompt or "message" in prompt or "social" in prompt:
        return "Chat App:\n- User Authentication\n- Chat Rooms\n- Direct Messages\n- Notifications\n- Online Status"
    elif "delivery" in prompt or "order" in prompt or "courier" in prompt:
        return "Delivery App:\n- Order Placement\n- Live Tracking\n- Driver Assignment\n- Payment\n- Order History"
    elif "fitness" in prompt or "gym" in prompt or "workout" in prompt:
        return "Fitness App:\n- Workout Plans\n- Progress Tracker\n- Calorie Counter\n- Exercise Library\n- Goals"
    elif "travel" in prompt or "hotel" in prompt or "booking" in prompt:
        return "Travel App:\n- Search & Filter\n- Hotel Booking\n- Flight Search\n- Itinerary Planner\n- Reviews"
    elif "todo" in prompt or "task" in prompt or "productivity" in prompt:
        return "Todo App:\n- Task List\n- Priority Levels\n- Due Dates\n- Categories\n- Progress Bar"
    elif "employee" in prompt or "hr" in prompt or "staff" in prompt:
        return "HR Tool:\n- Employee Directory\n- Leave Management\n- Payroll Tracker\n- Performance Reviews\n- Onboarding"
    elif "inventory" in prompt or "stock" in prompt or "warehouse" in prompt:
        return "Inventory Tool:\n- Stock List\n- Add/Remove Items\n- Low Stock Alerts\n- Supplier Management\n- Reports"
    elif "crm" in prompt or "customer" in prompt or "client" in prompt:
        return "CRM Tool:\n- Customer List\n- Deal Pipeline\n- Follow-up Reminders\n- Email Integration\n- Reports"
    elif "project" in prompt or "team" in prompt or "management" in prompt:
        return "Project Management Tool:\n- Task Board (Kanban)\n- Team Members\n- Deadlines\n- File Sharing\n- Progress Tracker"
    else:
        return "General App:\n- User Authentication\n- Home Screen\n- Settings\n- Profile Page\n- Notifications"

@app.route("/generate", methods=["POST", "OPTIONS"])
def generate():
    if request.method == "OPTIONS":
        response = jsonify({})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        return response

    data = request.json
    prompt = data.get("prompt", "")
    result = generate_fake(prompt)

    conn = sqlite3.connect("C:/Users/shiva/data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (prompt, result, type) VALUES (?, ?, ?)", (prompt, result, "website"))
    conn.commit()
    conn.close()

    response = jsonify({"result": result})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/get", methods=["GET"])
def get_projects():
    conn = sqlite3.connect("C:/Users/shiva/data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True, port=5000)