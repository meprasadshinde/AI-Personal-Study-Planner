from scheduler import generate_schedule
from utils import load_data

def main():
    subjects, hours_per_day = load_data()

    schedule = generate_schedule(subjects, hours_per_day)

    print("\n===== STUDY PLAN =====")
    for day in schedule:
        print(f"\nDate: {day['date']}")
        for task in day["tasks"]:
            print(f"  - {task}")

if __name__ == "__main__":
    main()