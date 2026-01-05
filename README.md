# 🎓 Smart Study Planner (EduTech)

A cloud-backed **personalized study plan generator** that dynamically adapts schedules based on subject difficulty, exam urgency, available time, and user performance.

Built as a **hackathon-ready EduTech project** using Flask and Supabase.

---

## 🚀 Problem Statement
Students often struggle with fixed timetables that don’t adapt to:
- Changing availability
- Upcoming exams
- Missed or completed tasks

This project solves that by acting like a **virtual study mentor** that automatically adjusts study plans.

---

## ✨ Features
- 🔐 User authentication (Supabase Auth)
- 📚 Add subjects with difficulty & exam date
- ⏰ Input available daily study time
- 🧠 Priority-based study plan generation
- 🔄 Adaptive planning (missed tasks increase priority)
- ☁️ Cloud storage with Supabase
- 👤 User-specific data isolation

---

## 🧠 How It Works (Logic Overview)
Each subject is assigned a **priority score** based on:
- Difficulty level
- Exam proximity
- Previous missed tasks

The system then:
1. Sorts subjects by priority
2. Allocates available study time
3. Generates a personalized plan
4. Stores progress for future adaptation

---

## 🛠️ Tech Stack
| Layer | Technology |
|-----|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Database | Supabase (PostgreSQL) |
| Auth | Supabase Authentication |
| Logic | Rule-based adaptive engine |

---

## 📁 Project Structure
# smart-study-planner
