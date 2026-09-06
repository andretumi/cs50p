fda_table = [
    {"Fruits": "Apple", "Calories": 130},
    {"Fruits": "Avocado", "Calories": 50},
    {"Fruits": "Banana", "Calories": 110},
    {"Fruits": "Cantaloupe", "Calories": 50},
    {"Fruits": "Grapefruit", "Calories": 60},
    {"Fruits": "Grapes", "Calories": 90},
    {"Fruits": "Honeydew Melon", "Calories": 50},
    {"Fruits": "Kiwifruit", "Calories": 90},
    {"Fruits": "Lemon", "Calories": 15},
    {"Fruits": "Lime", "Calories": 20},
    {"Fruits": "Nectarine", "Calories": 60},
    {"Fruits": "Orange", "Calories": 80},
    {"Fruits": "Peach", "Calories": 60},
    {"Fruits": "Pear", "Calories": 100},
    {"Fruits": "Pineapple", "Calories": 50},
    {"Fruits": "Plums", "Calories": 70},
    {"Fruits": "Strawberries", "Calories": 50},
    {"Fruits": "Sweet Cherries", "Calories": 100},
    {"Fruits": "Tangerine", "Calories": 50},
    {"Fruits": "Watermelon", "Calories": 80}
]

user_request = input("Item: ")

for fruit_info in fda_table:
    if user_request.lower() == fruit_info["Fruits"].lower():
        print(f"Calories: {fruit_info['Calories']}")
        break
