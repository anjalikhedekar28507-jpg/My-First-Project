# Simple Recommendation System

courses = {
    "Python": ["Programming", "Coding", "Beginner"],
    "Java": ["Programming", "Coding", "OOP"],
    "Machine Learning": ["AI", "Python", "Data"],
    "Artificial Intelligence": ["AI", "Machine Learning", "Python"],
    "Web Development": ["HTML", "CSS", "JavaScript"],
    "Data Science": ["Python", "Data", "Machine Learning"]
}


def recommend(course):
    if course not in courses:
        print("Course not found!")
        return

    selected_features = set(courses[course])

    recommendations = []

    for name, features in courses.items():

        if name == course:
            continue

        common = selected_features.intersection(set(features))

        recommendations.append(
            (name, len(common))
        )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Courses:")
    print("--------------------")

    for name, score in recommendations[:3]:
        print(name)


print("================================")
print("   COURSE RECOMMENDATION SYSTEM")
print("================================")

print("\nAvailable Courses:")

for course in courses:
    print("-", course)

user_course = input("\nEnter course name: ")

recommend(user_course)