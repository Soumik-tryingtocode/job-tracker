import json
from datetime import datetime

FILENAME = 'data.json'

def load_data():
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILENAME, 'w') as f:
        json.dump(data, f, indent=4)
def add_application():
    company = input("Company name: ")
    position = input("Position: ")
    status = input("Status (Applied/Interviewing/Offer/Rejected): ")
    notes = input("Notes: ")
    date_applied = datetime.now().strftime('%Y-%m-%d')

    new_app = {
        'company': company,
        'position': position,
        'status': status,
        'notes': notes,
        'date_applied': date_applied
    }

    data = load_data()
    data.append(new_app)
    save_data(data)
    print("✅ Application added successfully!")

def view_applications():
    data = load_data()
    if not data:
        print("No applications found.")
        return

    for idx, app in enumerate(data):
        print(f"\n[{idx}] {app['company']} - {app['position']}")
        print(f"   Status: {app['status']}")
        print(f"   Notes: {app['notes']}")
        print(f"   Date Applied: {app['date_applied']}")

def update_status():
    data = load_data()
    view_applications()
    idx = int(input("Enter the index of the application to update: "))
    if idx < 0 or idx >= len(data):
        print("❌ Invalid index.")
        return

    new_status = input("Enter new status: ")
    data[idx]['status'] = new_status
    save_data(data)
    print("✅ Status updated!")

def delete_application():
    data = load_data()
    view_applications()
    idx = int(input("Enter the index of the application to delete: "))
    if idx < 0 or idx >= len(data):
        print("❌ Invalid index.")
        return

    del data[idx]
    save_data(data)
    print("🗑️ Application deleted.")

def menu():
    while True:
        print("\n===== Internship/Job Tracker =====")
        print("1. Add new application")
        print("2. View all applications")
        print("3. Update application status")
        print("4. Delete an application")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_application()
        elif choice == '2':
            view_applications()
        elif choice == '3':
            update_status()
        elif choice == '4':
            delete_application()
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
