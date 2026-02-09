def generate_tasks_from_note(content: str):
    """
    Create simple study tasks from note content
    """
    if not content:
        return []

    sentences = [s.strip() for s in content.split(".") if s.strip()]

    tasks = []
    for s in sentences[:5]:
        tasks.append(f"Study: {s}")

    return tasks


def generate_qa_from_note(content: str):
    """
    Generate Q&A from note content
    """
    if not content:
        return []

    sentences = [s.strip() for s in content.split(".") if s.strip()]

    qa_list = []
    for s in sentences[:5]:
        first_word = s.split()[0] if s.split() else "Concept"

        qa_list.append({
            "question": f"What is {first_word}?",
            "answer": s
        })

    return qa_list


def answer_user_question(question: str):
    """
    Answer user questions in exam-style format
    """
    if not question:
        return "Please ask a valid academic question."

    q = question.lower()

    if "deadlock" in q:
        return (
            "Deadlock is a condition in operating systems where two or more "
            "processes wait indefinitely for resources held by each other, "
            "causing the system to stop execution until intervention occurs."
        )

    if "normalization" in q:
        return (
            "Normalization is the process of organizing database tables to "
            "reduce redundancy and improve data integrity by dividing data "
            "into smaller related tables."
        )

    return (
        "This is an AI-generated academic response. "
        "Future versions will integrate advanced language models "
        "for deeper conceptual explanations."
    )
from datetime import datetime, timedelta


def generate_study_schedule(tasks):
    """
    Create a simple smart study schedule from pending tasks
    """
    if not tasks:
        return ["No pending tasks. You are all caught up!"]

    today = datetime.now()
    schedule = []

    for i, task in enumerate(tasks):
        study_day = today + timedelta(days=i)
        schedule.append(
            f"{study_day.strftime('%d %b')}: Study '{task.title}'"
        )

    return schedule


def generate_priority_schedule(tasks):
    """
    Create priority-based study schedule using due dates.
    Earlier due date = higher priority.
    """
    if not tasks:
        return ["No pending tasks. You are all caught up!"]

    # Sort by due date (None goes last)
    tasks_sorted = sorted(
        tasks,
        key=lambda t: t.due_date if t.due_date else datetime.max
    )

    schedule = []

    for task in tasks_sorted:
        if task.due_date:
            day = task.due_date.strftime("%d %b")
            schedule.append(f"🔥 High Priority before {day}: {task.title}")
        else:
            schedule.append(f"📘 Study Soon: {task.title}")

    return schedule
def generate_exam_revision_plan(tasks):
    """
    Generate a smart revision plan before exams.
    Focus on incomplete and important tasks.
    """

    if not tasks:
        return ["You have no pending topics. Ready for the exam! 🎉"]

    revision_plan = []
    day = 1

    for task in tasks[:7]:  # limit to 7 topics for 1-week revision
        revision_plan.append(f"Day {day}: Revise {task.title}")
        day += 1

    revision_plan.append("Final Day: Practice previous year questions + mock test")

    return revision_plan
def generate_productivity_insight(total, completed):
    """
    Generate smart feedback based on study progress.
    """

    if total == 0:
        return "You haven't added any study tasks yet. Start planning today! 📚"

    percent = (completed / total) * 100

    if percent == 100:
        return "Excellent work! You are fully prepared for exams. 🏆"
    elif percent >= 70:
        return "Great progress! Revise remaining topics and you're ready. 💪"
    elif percent >= 40:
        return "Good start, but you need more consistency. Keep studying daily. 📖"
    else:
        return "You are falling behind. Create a strict study schedule now. ⚠️"
