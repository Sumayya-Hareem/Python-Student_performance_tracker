class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        if not self.students:
            print("No students in the system.")
            return

        print("\nStudent Performance:")
        print("-" * 30)
        for student in self.students.values():
            avg_score = student.calculate_average()
            passing_status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Name: {student.name}")
            print(f"  Average Score: {avg_score:.2f}")
            print(f"  Status: {passing_status}")
            print("-" * 30)

def main():
    tracker = PerformanceTracker()

    while True:
        try:
            # Input student name
            name = input("Enter student name (or type 'done' to finish): ").strip()
            if name.lower() == "done":
                break

            # Input scores
            scores = []
            for subject in ["Math", "Science", "English"]:
                while True:
                    try:
                        score = int(input(f"Enter {subject} score for {name}: "))
                        if score < 0 or score > 100:
                            raise ValueError("Score must be between 0 and 100.")
                        scores.append(score)
                        break
                    except ValueError as e:
                        print(f"Invalid input: {e}. Please try again.")

            tracker.add_student(name, scores)

        except KeyboardInterrupt:
            print("\nExiting input process.")
            break

    tracker.display_student_performance()
    class_average = tracker.calculate_class_average()
    print(f"\nClass Average Score: {class_average:.2f}")

if __name__ == "__main__":
    main()