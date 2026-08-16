import tkinter as tk
from tkinter import ttk, messagebox


# ============================================================
# AI CAREER RECOMMENDATION SYSTEM
# Enhanced UI + More Skills + More Interests + 20 Careers
# No external libraries required
# ============================================================

CAREERS = {
    "AI / ML Engineer": {
        "skills": ["Python", "Mathematics", "Statistics", "Problem Solving", "Analytical Thinking"],
        "subjects": ["Computer Science", "Mathematics", "Physics"],
        "interests": ["Artificial Intelligence", "Machine Learning", "Robotics", "Technology", "Research"]
    },
    "Data Scientist": {
        "skills": ["Python", "Mathematics", "Statistics", "Data Analysis", "Analytical Thinking"],
        "subjects": ["Computer Science", "Mathematics", "Statistics"],
        "interests": ["Data Science", "Artificial Intelligence", "Data", "Research", "Technology"]
    },
    "Data Analyst": {
        "skills": ["Python", "Statistics", "Data Analysis", "Communication", "Analytical Thinking"],
        "subjects": ["Mathematics", "Statistics", "Computer Science"],
        "interests": ["Data", "Data Science", "Technology", "Business"]
    },
    "Software Developer": {
        "skills": ["Python", "Programming", "Problem Solving", "Logical Thinking", "Debugging"],
        "subjects": ["Computer Science", "Mathematics"],
        "interests": ["Programming", "Technology", "Software Development"]
    },
    "Software Engineer": {
        "skills": ["Programming", "Problem Solving", "Logical Thinking", "Algorithms", "Debugging"],
        "subjects": ["Computer Science", "Mathematics"],
        "interests": ["Programming", "Technology", "Software Development"]
    },
    "Web Developer": {
        "skills": ["Programming", "HTML/CSS", "JavaScript", "Creativity", "Design"],
        "subjects": ["Computer Science"],
        "interests": ["Web Development", "Programming", "Technology", "Creativity"]
    },
    "Frontend Developer": {
        "skills": ["HTML/CSS", "JavaScript", "Creativity", "Design", "Communication"],
        "subjects": ["Computer Science"],
        "interests": ["Web Development", "Design", "Creativity", "Technology"]
    },
    "Backend Developer": {
        "skills": ["Programming", "Python", "Databases", "Problem Solving", "APIs"],
        "subjects": ["Computer Science", "Mathematics"],
        "interests": ["Programming", "Software Development", "Technology", "Cloud Computing"]
    },
    "Cybersecurity Analyst": {
        "skills": ["Programming", "Networking", "Problem Solving", "Analytical Thinking", "Cybersecurity"],
        "subjects": ["Computer Science", "Mathematics"],
        "interests": ["Cybersecurity", "Networking", "Technology", "Ethical Hacking"]
    },
    "Cybersecurity Engineer": {
        "skills": ["Programming", "Networking", "Cybersecurity", "Problem Solving", "Linux"],
        "subjects": ["Computer Science", "Mathematics"],
        "interests": ["Cybersecurity", "Ethical Hacking", "Networking", "Technology"]
    },
    "Cloud Engineer": {
        "skills": ["Programming", "Networking", "Linux", "Problem Solving", "Cloud Computing"],
        "subjects": ["Computer Science", "Mathematics"],
        "interests": ["Cloud Computing", "Technology", "Networking", "Software Development"]
    },
    "DevOps Engineer": {
        "skills": ["Programming", "Linux", "Cloud Computing", "Problem Solving", "Git"],
        "subjects": ["Computer Science"],
        "interests": ["Cloud Computing", "Software Development", "Technology", "Automation"]
    },
    "Robotics Engineer": {
        "skills": ["Python", "C/C++", "Mathematics", "Electronics", "Problem Solving"],
        "subjects": ["Computer Science", "Mathematics", "Physics", "Electronics"],
        "interests": ["Robotics", "Artificial Intelligence", "Technology", "Automation"]
    },
    "Computer Vision Engineer": {
        "skills": ["Python", "Mathematics", "Statistics", "Problem Solving", "Data Analysis"],
        "subjects": ["Computer Science", "Mathematics", "Physics"],
        "interests": ["Computer Vision", "Artificial Intelligence", "Robotics", "Research"]
    },
    "NLP Engineer": {
        "skills": ["Python", "Mathematics", "Statistics", "Programming", "Communication"],
        "subjects": ["Computer Science", "Mathematics"],
        "interests": ["Natural Language Processing", "Artificial Intelligence", "Research", "Technology"]
    },
    "UI/UX Designer": {
        "skills": ["Creativity", "Design", "Communication", "HTML/CSS", "Problem Solving"],
        "subjects": ["Computer Science"],
        "interests": ["UI/UX Design", "Design", "Creativity", "Technology"]
    },
    "Game Developer": {
        "skills": ["Programming", "C/C++", "Creativity", "Problem Solving", "Design"],
        "subjects": ["Computer Science", "Mathematics", "Physics"],
        "interests": ["Game Development", "Programming", "Creativity", "Technology"]
    },
    "IoT Engineer": {
        "skills": ["Programming", "Networking", "Electronics", "Python", "Problem Solving"],
        "subjects": ["Computer Science", "Physics", "Electronics", "Mathematics"],
        "interests": ["Internet of Things", "Robotics", "Technology", "Automation"]
    },
    "Blockchain Developer": {
        "skills": ["Programming", "Python", "Problem Solving", "Cryptography", "Databases"],
        "subjects": ["Computer Science", "Mathematics"],
        "interests": ["Blockchain", "Programming", "Technology", "Cybersecurity"]
    },
    "Database Administrator": {
        "skills": ["Databases", "SQL", "Problem Solving", "Analytical Thinking", "Networking"],
        "subjects": ["Computer Science", "Mathematics"],
        "interests": ["Data", "Databases", "Technology", "Cloud Computing"]
    }
}


SKILLS = [
    "Python", "Programming", "C/C++", "JavaScript", "HTML/CSS",
    "Mathematics", "Statistics", "Data Analysis", "Problem Solving",
    "Logical Thinking", "Analytical Thinking", "Creativity", "Design",
    "Communication", "Networking", "Databases", "SQL", "Linux",
    "Cloud Computing", "Electronics", "Algorithms", "Debugging",
    "APIs", "Git", "Cybersecurity", "Cryptography"
]

SUBJECTS = [
    "Computer Science", "Mathematics", "Statistics", "Physics",
    "Electronics"
]

INTERESTS = [
    "Artificial Intelligence", "Machine Learning", "Data Science", "Data",
    "Programming", "Software Development", "Web Development",
    "Cybersecurity", "Ethical Hacking", "Cloud Computing", "Networking",
    "Robotics", "Automation", "Computer Vision",
    "Natural Language Processing", "UI/UX Design", "Game Development",
    "Internet of Things", "Blockchain", "Databases", "Technology",
    "Creativity", "Research", "Business"
]


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("AI Career Recommendation System")
root.geometry("1100x760")
root.minsize(900, 650)
root.configure(bg="#0f172a")


# ============================================================
# STYLES
# ============================================================

style = ttk.Style()
try:
    style.theme_use("clam")
except tk.TclError:
    pass

style.configure(
    "TCheckbutton",
    background="#172033",
    foreground="#e5e7eb",
    font=("Segoe UI", 10)
)

style.map(
    "TCheckbutton",
    background=[("active", "#172033")],
    foreground=[("active", "#ffffff")]
)


# ============================================================
# VARIABLES
# ============================================================

skill_vars = {item: tk.BooleanVar(value=False) for item in SKILLS}
subject_vars = {item: tk.BooleanVar(value=False) for item in SUBJECTS}
interest_vars = {item: tk.BooleanVar(value=False) for item in INTERESTS}


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(root, bg="#111827", height=105)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="🎓",
    font=("Segoe UI Emoji", 30),
    bg="#111827",
    fg="#38bdf8"
).pack(side="left", padx=(35, 12))

title_box = tk.Frame(header, bg="#111827")
title_box.pack(side="left", pady=18)

tk.Label(
    title_box,
    text="AI Career Recommendation System",
    font=("Segoe UI", 24, "bold"),
    bg="#111827",
    fg="#f8fafc"
).pack(anchor="w")

tk.Label(
    title_box,
    text="Discover careers that match your skills, subjects and interests",
    font=("Segoe UI", 11),
    bg="#111827",
    fg="#94a3b8"
).pack(anchor="w", pady=(3, 0))


# ============================================================
# SCROLLABLE CONTENT
# ============================================================

outer = tk.Frame(root, bg="#0f172a")
outer.pack(fill="both", expand=True)

canvas = tk.Canvas(
    outer,
    bg="#0f172a",
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    outer,
    orient="vertical",
    command=canvas.yview
)

content = tk.Frame(
    canvas,
    bg="#0f172a"
)

content_window = canvas.create_window(
    (0, 0),
    window=content,
    anchor="nw"
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))


def resize_content(event):
    canvas.itemconfigure(content_window, width=event.width)


content.bind("<Configure>", update_scroll_region)
canvas.bind("<Configure>", resize_content)


def mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


canvas.bind_all("<MouseWheel>", mousewheel)


# ============================================================
# CARD CREATOR
# ============================================================

def create_card(parent, title, subtitle, items, variables, icon):
    card = tk.Frame(
        parent,
        bg="#172033",
        highlightbackground="#263449",
        highlightthickness=1
    )

    card.pack(
        fill="x",
        padx=35,
        pady=12
    )

    heading = tk.Frame(card, bg="#172033")
    heading.pack(fill="x", padx=22, pady=(18, 3))

    tk.Label(
        heading,
        text=f"{icon}  {title}",
        font=("Segoe UI", 16, "bold"),
        bg="#172033",
        fg="#f8fafc"
    ).pack(side="left")

    tk.Label(
        card,
        text=subtitle,
        font=("Segoe UI", 10),
        bg="#172033",
        fg="#94a3b8"
    ).pack(anchor="w", padx=25, pady=(0, 12))

    grid = tk.Frame(card, bg="#172033")
    grid.pack(fill="x", padx=22, pady=(0, 18))

    columns = 3 if len(items) > 8 else 2

    for i, item in enumerate(items):
        cb = ttk.Checkbutton(
            grid,
            text=item,
            variable=variables[item]
        )
        cb.grid(
            row=i // columns,
            column=i % columns,
            sticky="w",
            padx=10,
            pady=6
        )

    for c in range(columns):
        grid.columnconfigure(c, weight=1)

    return card


# ============================================================
# CARDS
# ============================================================

create_card(
    content,
    "Your Skills",
    "Select the skills you already have or enjoy using.",
    SKILLS,
    skill_vars,
    "💻"
)

create_card(
    content,
    "Your Subjects",
    "Choose the subjects you are comfortable with.",
    SUBJECTS,
    subject_vars,
    "📚"
)

create_card(
    content,
    "Your Interests",
    "Select the technology areas that interest you.",
    INTERESTS,
    interest_vars,
    "❤️"
)


# ============================================================
# BUTTONS
# ============================================================

button_frame = tk.Frame(content, bg="#0f172a")
button_frame.pack(fill="x", padx=35, pady=(10, 30))


def clear_all():
    for var in list(skill_vars.values()) + list(subject_vars.values()) + list(interest_vars.values()):
        var.set(False)


def recommend():
    selected_skills = [x for x, v in skill_vars.items() if v.get()]
    selected_subjects = [x for x, v in subject_vars.items() if v.get()]
    selected_interests = [x for x, v in interest_vars.items() if v.get()]

    if not selected_skills and not selected_subjects and not selected_interests:
        messagebox.showwarning(
            "No Selection",
            "Please select at least one skill, subject or interest."
        )
        return

    # Weighting:
    # Skills = 2 points
    # Subjects = 2 points
    # Interests = 3 points
    results = []

    max_score = (
        len(selected_skills) * 2
        + len(selected_subjects) * 2
        + len(selected_interests) * 3
    )

    for career, info in CAREERS.items():
        career_skills = info["skills"]
        career_subjects = info["subjects"]
        career_interests = info["interests"]

        matched_skills = [x for x in selected_skills if x in career_skills]
        matched_subjects = [x for x in selected_subjects if x in career_subjects]
        matched_interests = [x for x in selected_interests if x in career_interests]

        score = (
            len(matched_skills) * 2
            + len(matched_subjects) * 2
            + len(matched_interests) * 3
        )

        results.append(
            (
                career,
                score,
                matched_skills,
                matched_subjects,
                matched_interests
            )
        )

    results.sort(key=lambda x: x[1], reverse=True)

    show_results(
        results,
        max_score,
        selected_skills,
        selected_subjects,
        selected_interests
    )


def show_results(results, max_score, selected_skills, selected_subjects, selected_interests):
    result = tk.Toplevel(root)
    result.title("Your Career Recommendations")
    result.geometry("950x720")
    result.configure(bg="#0f172a")

    # Header
    top = tk.Frame(result, bg="#111827", height=95)
    top.pack(fill="x")
    top.pack_propagate(False)

    tk.Label(
        top,
        text="🎯  Your Career Recommendations",
        font=("Segoe UI", 22, "bold"),
        bg="#111827",
        fg="#f8fafc"
    ).pack(anchor="w", padx=30, pady=(18, 2))

    tk.Label(
        top,
        text="Based on your selected skills, subjects and interests",
        font=("Segoe UI", 10),
        bg="#111827",
        fg="#94a3b8"
    ).pack(anchor="w", padx=32)

    # Scroll area
    outer2 = tk.Frame(result, bg="#0f172a")
    outer2.pack(fill="both", expand=True)

    canvas2 = tk.Canvas(
        outer2,
        bg="#0f172a",
        highlightthickness=0
    )
    scroll2 = ttk.Scrollbar(
        outer2,
        orient="vertical",
        command=canvas2.yview
    )

    result_content = tk.Frame(canvas2, bg="#0f172a")
    result_window = canvas2.create_window(
        (0, 0),
        window=result_content,
        anchor="nw"
    )

    canvas2.configure(yscrollcommand=scroll2.set)
    canvas2.pack(side="left", fill="both", expand=True)
    scroll2.pack(side="right", fill="y")

    result_content.bind(
        "<Configure>",
        lambda e: canvas2.configure(scrollregion=canvas2.bbox("all"))
    )

    canvas2.bind(
        "<Configure>",
        lambda e: canvas2.itemconfigure(result_window, width=e.width)
    )

    # Top 10
    for rank, (career, score, ms, msub, mi) in enumerate(results[:10], 1):
        percentage = round((score / max_score) * 100) if max_score else 0

        card = tk.Frame(
            result_content,
            bg="#172033",
            highlightbackground="#263449",
            highlightthickness=1
        )
        card.pack(fill="x", padx=28, pady=6)

        row = tk.Frame(card, bg="#172033")
        row.pack(fill="x", padx=18, pady=(13, 4))

        tk.Label(
            row,
            text=f"{rank}.  {career}",
            font=("Segoe UI", 13, "bold"),
            bg="#172033",
            fg="#f8fafc"
        ).pack(side="left")

        tk.Label(
            row,
            text=f"{percentage}% MATCH",
            font=("Segoe UI", 10, "bold"),
            bg="#172033",
            fg="#34d399"
        ).pack(side="right")

        # Progress bar
        bar_bg = tk.Frame(card, bg="#263449", height=7)
        bar_bg.pack(fill="x", padx=20, pady=(2, 8))

        fill_width = max(1, percentage)
        bar_fill = tk.Frame(
            bar_bg,
            bg="#38bdf8",
            height=7
        )
        bar_fill.place(
            relwidth=fill_width / 100,
            relheight=1
        )

        matched = []
        if ms:
            matched.append("Skills: " + ", ".join(ms))
        if msub:
            matched.append("Subjects: " + ", ".join(msub))
        if mi:
            matched.append("Interests: " + ", ".join(mi))

        tk.Label(
            card,
            text="\n".join(matched) if matched else "No direct matches",
            font=("Segoe UI", 9),
            bg="#172033",
            fg="#94a3b8",
            justify="left",
            wraplength=800
        ).pack(anchor="w", padx=20, pady=(0, 14))

    # Bottom
    bottom = tk.Frame(result, bg="#111827")
    bottom.pack(fill="x")

    tk.Button(
        bottom,
        text="Close",
        command=result.destroy,
        font=("Segoe UI", 10, "bold"),
        bg="#334155",
        fg="white",
        activebackground="#475569",
        activeforeground="white",
        relief="flat",
        padx=30,
        pady=8
    ).pack(pady=12)


# Main buttons
tk.Button(
    button_frame,
    text="✨  FIND MY BEST CAREER",
    command=recommend,
    font=("Segoe UI", 12, "bold"),
    bg="#0ea5e9",
    fg="white",
    activebackground="#0284c7",
    activeforeground="white",
    relief="flat",
    padx=35,
    pady=12,
    cursor="hand2"
).pack(side="left", padx=(0, 12))

tk.Button(
    button_frame,
    text="↻  CLEAR ALL",
    command=clear_all,
    font=("Segoe UI", 11, "bold"),
    bg="#334155",
    fg="white",
    activebackground="#475569",
    activeforeground="white",
    relief="flat",
    padx=25,
    pady=12,
    cursor="hand2"
).pack(side="left")


# ============================================================
# FOOTER
# ============================================================

tk.Label(
    content,
    text="AI Career Recommendation System • Educational Project",
    font=("Segoe UI", 9),
    bg="#0f172a",
    fg="#64748b"
).pack(pady=(0, 25))


# ============================================================
# START
# ============================================================

root.mainloop()
