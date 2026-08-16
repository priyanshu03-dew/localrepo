import tkinter as tk
from tkinter import messagebox

CAREERS = {
    "AI / ML Engineer": (["Python", "Mathematics", "Problem Solving"], ["Artificial Intelligence", "Technology", "Robotics"]),
    "Data Scientist": (["Python", "Mathematics", "Statistics"], ["Artificial Intelligence", "Technology", "Data"]),
    "Data Analyst": (["Python", "Mathematics", "Statistics"], ["Data", "Technology"]),
    "Software Developer": (["Python", "Programming", "Problem Solving"], ["Technology", "Programming"]),
    "Software Engineer": (["Programming", "Python", "Problem Solving"], ["Technology", "Programming"]),
    "Web Developer": (["Programming", "Creativity", "Design"], ["Technology", "Programming", "Creativity"]),
    "Frontend Developer": (["Programming", "Creativity", "Design"], ["Technology", "Creativity"]),
    "Backend Developer": (["Programming", "Python", "Problem Solving"], ["Technology", "Programming"]),
    "Cybersecurity Analyst": (["Programming", "Networking", "Problem Solving"], ["Cybersecurity", "Technology"]),
    "Cybersecurity Engineer": (["Programming", "Networking", "Problem Solving"], ["Cybersecurity", "Technology"]),
    "Cloud Engineer": (["Programming", "Networking"], ["Cloud Computing", "Technology"]),
    "DevOps Engineer": (["Programming", "Networking", "Problem Solving"], ["Cloud Computing", "Technology"]),
    "Robotics Engineer": (["Python", "Mathematics", "Problem Solving"], ["Robotics", "Technology", "Artificial Intelligence"]),
    "Computer Vision Engineer": (["Python", "Mathematics", "Problem Solving"], ["Artificial Intelligence", "Robotics", "Technology"]),
    "NLP Engineer": (["Python", "Mathematics", "Programming"], ["Artificial Intelligence", "Technology"]),
    "UI/UX Designer": (["Creativity", "Design"], ["Creativity", "Technology"]),
    "Game Developer": (["Programming", "Creativity", "Problem Solving"], ["Technology", "Creativity", "Programming"]),
    "IoT Engineer": (["Programming", "Networking", "Problem Solving"], ["Technology", "Robotics"]),
    "Blockchain Developer": (["Programming", "Python", "Problem Solving"], ["Technology", "Programming"]),
    "Database Administrator": (["Programming", "Problem Solving"], ["Data", "Technology"])
}

root = tk.Tk()
root.title("AI Career Recommendation System")
root.geometry("850x700")
root.configure(bg="#202124")

skill_vars = {}
interest_vars = {}

skills = [
    "Python", "Programming", "Mathematics", "Statistics",
    "Networking", "Creativity", "Design", "Problem Solving"
]

interests = [
    "Artificial Intelligence", "Technology", "Data", "Cybersecurity",
    "Robotics", "Cloud Computing", "Programming", "Creativity"
]

def add_checkboxes(parent, items, variables, start_row):
    for i, item in enumerate(items):
        var = tk.BooleanVar(value=False)
        variables[item] = var
        tk.Checkbutton(
            parent, text=item, variable=var,
            font=("Arial", 11), bg="#303134", fg="white",
            selectcolor="#202124", activebackground="#303134",
            activeforeground="white"
        ).grid(row=start_row + i // 2, column=i % 2,
               sticky="w", padx=30, pady=4)

def recommend():
    selected_skills = [x for x, v in skill_vars.items() if v.get()]
    selected_interests = [x for x, v in interest_vars.items() if v.get()]

    if not selected_skills and not selected_interests:
        messagebox.showwarning("No Selection", "Select at least one skill or interest.")
        return

    results = []
    max_score = len(selected_skills) * 2 + len(selected_interests) * 3

    for career, (career_skills, career_interests) in CAREERS.items():
        score = 0
        score += sum(2 for x in selected_skills if x in career_skills)
        score += sum(3 for x in selected_interests if x in career_interests)
        results.append((career, score))

    results.sort(key=lambda x: x[1], reverse=True)

    result_window = tk.Toplevel(root)
    result_window.title("Career Recommendations")
    result_window.geometry("650x650")
    result_window.configure(bg="#202124")

    tk.Label(
        result_window, text="Your Career Recommendations",
        font=("Arial", 20, "bold"), bg="#202124", fg="white"
    ).pack(pady=20)

    for rank, (career, score) in enumerate(results, 1):
        percentage = round(score / max_score * 100) if max_score else 0

        row = tk.Frame(result_window, bg="#303134")
        row.pack(fill="x", padx=30, pady=4)

        tk.Label(
            row, text=f"{rank}. {career}",
            font=("Arial", 11, "bold"), bg="#303134", fg="white",
            anchor="w"
        ).pack(side="left", padx=12, pady=9)

        tk.Label(
            row, text=f"{percentage}% Match",
            font=("Arial", 11, "bold"), bg="#303134", fg="#00d084"
        ).pack(side="right", padx=12)

    tk.Button(
        result_window, text="Close", command=result_window.destroy,
        bg="#00a884", fg="white", font=("Arial", 11, "bold"),
        padx=30, pady=8
    ).pack(pady=20)

# Main UI
tk.Label(
    root, text="AI Career Recommendation System",
    font=("Arial", 24, "bold"), bg="#202124", fg="white"
).pack(pady=(25, 5))

tk.Label(
    root, text="Select your skills and interests",
    font=("Arial", 12), bg="#202124", fg="lightgray"
).pack(pady=(0, 15))

frame = tk.Frame(root, bg="#303134")
frame.pack(padx=40, pady=10, fill="both", expand=True)

tk.Label(
    frame, text="Your Skills", font=("Arial", 15, "bold"),
    bg="#303134", fg="white"
).grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=12)

add_checkboxes(frame, skills, skill_vars, 1)

tk.Label(
    frame, text="Your Interests", font=("Arial", 15, "bold"),
    bg="#303134", fg="white"
).grid(row=5, column=0, columnspan=2, sticky="w", padx=20, pady=12)

add_checkboxes(frame, interests, interest_vars, 6)

tk.Button(
    root, text="FIND MY BEST CAREER", command=recommend,
    font=("Arial", 13, "bold"), bg="#00a884", fg="white",
    padx=35, pady=10
).pack(pady=18)

root.mainloop()
