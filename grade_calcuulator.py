def ask_int(prompt, min_value=1):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value < min_value:
                print("Enter a number greater than or equal to", min_value)
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def ask_float(prompt, min_value=0.0, max_value=100.0):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value < min_value or value > max_value:
                print("Enter a value between", min_value, "and", max_value)
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def grade_from_score(score):
    if score >= 90:
        return "A"
    if score >= 85:
        return "B+"
    if score >= 80:
        return "B"
    if score >= 75:
        return "C+"
    if score >= 70:
        return "C"
    if score >= 65:
        return "D+"
    if score >= 60:
        return "D"
    return "F"


def collect_subjects():
    count = ask_int("How many subjects? ", min_value=1)
    subjects = []
    for idx in range(1, count + 1):
        print("\nSubject", idx)
        name = input("Name: ").strip()
        if not name:
            name = "Subject " + str(idx)
        marks = ask_float("Marks (0-100): ")
        subjects.append([name, marks])
    return subjects


def calculate_average(subjects):
    total = 0.0
    for sub in subjects:
        total += sub[1]
    return total / len(subjects)


def print_report(student_name, subjects, final_score):
    grade = grade_from_score(final_score)
    status = "PASS" if final_score >= 35 else "FAIL"

    print("\n" + "=" * 60)
    print(f"REPORT CARD: {student_name}")
    print("=" * 60)
    print(f"{'Subject':20} {'Marks':>8}")
    print("-" * 60)
    for sub in subjects:
        print(f"{sub[0]:20} {sub[1]:>8.2f}")
    print("-" * 60)
    print(f"{'Final Score':20} {final_score:>8.2f}")
    print(f"{'Letter Grade':20} {grade:>8}")
    print(f"{'Result':20} {status:>8}")
    print("=" * 60)


def main():
    print("Simple Grade Calculator\n")

    while True:
        student_name = input("Student name: ").strip() or "Student"
        subjects = collect_subjects()
        final_score = calculate_average(subjects)
        print_report(student_name, subjects, final_score)

        again = input("\nCalculate for another student? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
