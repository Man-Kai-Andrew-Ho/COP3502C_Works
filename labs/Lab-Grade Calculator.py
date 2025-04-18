import os
import matplotlib.pyplot as plt

# --- Load students.txt ---
def load_students(filepath):
    students = {}
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            student_id = line[:3]
            student_name = line[3:]
            students[student_name] = student_id
    return students

# --- Load assignments.txt ---
def load_assignments(filepath):
    assignments = {}
    with open(filepath, 'r') as file:
        lines = file.readlines()
        index = 0
        while index < len(lines):
            name = lines[index].strip()
            assignment_id = lines[index + 1].strip()
            points = int(lines[index + 2].strip())
            assignments[name] = (assignment_id, points)
            index += 3
    return assignments

# --- Load a single submission file ---
def load_submission_file(filepath):
    submissions = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split('|')
            student_id = parts[0]
            assignment_id = parts[1]
            percent = float(parts[2])
            submissions.append((student_id, assignment_id, percent))
    return submissions

# --- Load all submissions in folder ---
def get_all_submissions(directory):
    all_submissions = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        submissions = load_submission_file(path)
        for submission in submissions:
            all_submissions.append(submission)
    return all_submissions

# --- Option 1: Student grade ---
def student_grade(student_name, students, assignments, submissions):
    if student_name not in students:
        print("Student not found")
        return

    student_id = students[student_name]
    total_earned = 0

    for assignment_name in assignments:
        assignment_id, points = assignments[assignment_name]
        for submission in submissions:
            sid, aid, percent = submission
            if sid == student_id and aid == assignment_id:
                earned = (percent / 100) * points
                total_earned += earned

    final_percent = (total_earned / 1000) * 100
    print(f"{round(final_percent)}%")

# --- Option 2: Assignment statistics ---
def assignment_stats(assignment_name, assignments, submissions):
    if assignment_name not in assignments:
        print("Assignment not found")
        return

    assignment_id, points = assignments[assignment_name]
    scores = []

    for submission in submissions:
        student_id, aid, percent = submission
        if aid == assignment_id:
            score = (percent / 100) * points
            scores.append(score)

    if len(scores) == 0:
        print("No submissions found")
        return

    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)

    print(f"Min: {round((min_score / points) * 100)}%")
    print(f"Avg: {round((avg_score / points) * 100)}%")
    print(f"Max: {round((max_score / points) * 100)}%")

# --- Option 3: Assignment graph ---
def assignment_graph(assignment_name, assignments, submissions):
    if assignment_name not in assignments:
        print("Assignment not found")
        return

    assignment_id, points = assignments[assignment_name]
    scores = []

    for submission in submissions:
        student_id, aid, percent = submission
        if aid == assignment_id:
            score = (percent / 100) * points
            percent_score = (score / points) * 100
            scores.append(percent_score)

    if len(scores) == 0:
        print("No data to graph.")
        return

    plt.hist(scores, bins = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
    plt.title(assignment_name)
    plt.xlabel("Score (%)")
    plt.ylabel("Number of Students")
    plt.show()

# --- Main program ---
def main():
    students = load_students('file')
    assignments = load_assignments('file')
    submissions = get_all_submissions('file')

    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")

    choice = input("Enter your selection: ")

    if choice == '1':
        name = input("What is the student's name: ")
        student_grade(name, students, assignments, submissions)
    elif choice == '2':
        name = input("What is the assignment name: ")
        assignment_stats(name, assignments, submissions)
    elif choice == '3':
        name = input("What is the assignment name: ")
        assignment_graph(name, assignments, submissions)
    else:
        print("Invalid option.")

# Run the program
if __name__ == "__main__":
    main()
