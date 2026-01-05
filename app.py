from flask import Flask, request, jsonify, render_template
from supabase import create_client
from planner import generate_plan   

app = Flask(__name__)

url = "https://qbqujqjedtobttotkxef.supabase.co"
key = "sb_publishable_tEaHaYcl_RXOAtWTbhDzWQ_VDoRyBKl"

supabase = create_client(url, key)

# 🔹 Helper function: fetch subjects from Supabase
def get_subjects_from_db(user_id):
    response = supabase.table("subjects") \
        .select("*") \
        .eq("user_id", user_id) \
        .execute()
    return response.data

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/generate-plan", methods=["POST"])
def generate():
    data = request.json
    user_id = data["user_id"]
    total_time = data["total_time"]

    # 🔹 FETCH subjects from Supabase
    subjects = get_subjects_from_db(user_id)

    # 🔹 Convert DB data to planner format
    formatted_subjects = []
    for s in subjects:
        formatted_subjects.append({
            "name": s["name"],
            "priority": s["difficulty"]
        })

    plan = generate_plan(formatted_subjects, total_time)
    return jsonify(plan)

@app.route("/add-subject", methods=["POST"])
def add_subject():
    data = request.json

    supabase.table("subjects").insert({
        "user_id": data["user_id"],
        "name": data["name"],
        "difficulty": data["difficulty"],
        "exam_date": data["exam_date"]
    }).execute()

    return jsonify({"message": "Subject added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
