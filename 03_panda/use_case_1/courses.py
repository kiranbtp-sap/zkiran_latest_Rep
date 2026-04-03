from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Course catalog dictionary
course_catalog = {
    "UI5": {"trainer": "Anubhav", "hours": 40, "price": 380},
    "CPI": {"trainer": "Anurag", "hours": 35, "price": 400},
    "AOH": {"trainer": "Anubhav", "hours": 40, "price": 400},
    "CDS": {"trainer": "Ananya", "hours": 50, "price": 480},
    "BTP": {"trainer": "Saurabh", "hours": 30, "price": 580},
    "SAC": {"trainer": "Rohan", "hours": 45, "price": 300},
    "CAPM": {"trainer": "Sonia", "hours": 60, "price": 900},
    "RAP": {"trainer": "Anubhav", "hours": 40, "price": 850}
}

selected_courses = []

print(Fore.GREEN + "Welcome to the Course Catalog!")
print(Fore.CYAN + f"Available Courses: {', '.join(course_catalog.keys())}")
print(Fore.CYAN + "Type course codes one at a time. Type 'EXIT' to finish.\n")

while True:
    course = input("\nEnter the course code (or 'EXIT' to finish): ").strip().upper()
    if course == 'EXIT':
        break
    elif course in course_catalog:
        if course in selected_courses:
            print(Fore.YELLOW + f"⚠️ Course '{course}' already selected.")
        else:
            selected_courses.append(course)
            print(Fore.GREEN + f"✅ Added {course} to your selection.")
    else:
        print(Fore.RED + f"❌ Course '{course}' not found. Please try again.")

# Display the selected courses and their details and total cost
print("\nYou have selected the following courses:")
total_amount = 0

for idx, course in enumerate(selected_courses, start=1):
    details = course_catalog[course]
    print(f"{idx}. {course} - Trainer: {details['trainer']}, Hours: {details['hours']}, Price: ${details['price']}")
    total_amount += details['price']

print(f"\nTotal amount for selected courses: ${total_amount}")
