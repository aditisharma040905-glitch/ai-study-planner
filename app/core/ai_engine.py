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
