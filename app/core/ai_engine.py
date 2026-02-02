def generate_tasks_from_note(content: str):
    if not content:
        return []

    topics = [line.strip() for line in content.split(".") if line.strip()]

    tasks = []
    for topic in topics[:5]:
        tasks.append(f"Study {topic}")

    return tasks
