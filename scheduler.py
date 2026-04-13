from datetime import datetime, timedelta

def calculate_days_left(exam_date):
    today = datetime.now().date()
    exam = datetime.strptime(exam_date, "%Y-%m-%d").date()
    return max(1, (exam - today).days)

def generate_schedule(subjects, hours_per_day):
    schedule = []
    current_day = datetime.now().date()

    # Add days_left
    for sub in subjects:
        sub["days_left"] = calculate_days_left(sub["exam_date"])

    # Sort by priority (nearest exam first)
    subjects.sort(key=lambda x: x["days_left"])

    for sub in subjects:
        units = sub["units"]
        days = sub["days_left"]
        unit_counter = 1

        for i in range(days):
            tasks = []
            hours_used = 0

            while hours_used < hours_per_day and unit_counter <= units:
                tasks.append(f"{sub['name']} - Unit {unit_counter}")
                unit_counter += 1
                hours_used += 1

            schedule.append({
                "date": current_day.strftime("%Y-%m-%d"),
                "tasks": tasks
            })

            current_day += timedelta(days=1)

        # Add revision day
        schedule.append({
            "date": current_day.strftime("%Y-%m-%d"),
            "tasks": [f"{sub['name']} - Revision"]
        })

        current_day += timedelta(days=1)

    return schedule