base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }
level = "semi senior"
if level not in base_salaries.keys():
    print("not in")
print(base_salaries.keys())