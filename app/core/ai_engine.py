def generate_tasks_from_note(content: str):
    if not content:
        return []

    topics = [line.strip() for line in content.split(".") if line.strip()]

    tasks = []
    for topic in topics[:5]:
        tasks.append(f"Study {topic}")

    return tasks

def generate_qa_from_note(content: str):
    """
    Generate questions & answers from note content
    """
    if not content:
        return []

    sentences = [s.strip() for s in content.split(".") if s.strip()]

    qa_list = []

    for s in sentences[:5]:
        qa_list.append({
            "question": f"What is {s.split()[0]}?",
            "answer": s
        })

    return qa_list
def answer_user_question(question: str):
    """
    Answer user questions (rule-based for now)
    """
    if not question:
        return "Please ask a valid question."

    q = question.lower()

    if "deadlock" in q:
        return (
            "Deadlock is a situation where two or more processes are waiting "
            "for each other to release resources, so none of them can proceed."
        )

    if "normalization" in q:
        return (
            "Normalization is the process of organizing data in a database "
            "to reduce redundancy and improve data integrity."
        )

    return (
        "This is an AI-generated response. "
        "In future, this will be powered by advanced language models."
    )
