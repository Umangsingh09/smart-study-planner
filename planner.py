def generate_plan(subjects, total_minutes):
    sorted_subjects = sorted(subjects, key=lambda x: x["priority"], reverse=True)
    plan = []
    remaining = total_minutes

    for sub in sorted_subjects:
        if remaining <= 0:
            break

        allocated = min(60, remaining)
        plan.append({
            "subject": sub["name"],
            "time": allocated
        })
        remaining -= allocated

    return plan

if __name__ == "__main__":
    # Sample data to test the function
    sample_subjects = [
        {"name": "Mathematics", "priority": 9},
        {"name": "Physics", "priority": 8},
        {"name": "History", "priority": 5}
    ]
    # Run the planner with 130 minutes
    result = generate_plan(sample_subjects, 130)
    print(result)
