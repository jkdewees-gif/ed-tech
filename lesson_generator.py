"""Project-based lesson idea generator."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LessonIdea:
    title: str
    driving_question: str
    project: str
    deliverable: str
    assessment_focus: str
    standards_alignment: str


GRADE_BANDS = {
    "elementary": ("K-5", "hands-on exploration and simple collaboration"),
    "middle": ("6-8", "guided inquiry and teamwork"),
    "high": ("9-12", "independent research and authentic problem-solving"),
}

SUBJECT_PROJECTS = {
    "science": {
        "title": "Community Science Solutions",
        "question": "How can we use science to improve something in our local community?",
        "project": "Investigate a local environmental or health issue, collect data, and design a science-based solution.",
        "deliverable": "Prototype or model with a data-backed presentation to classmates or community stakeholders.",
        "assessment": "Scientific reasoning, quality of data collection, and clarity of explanation.",
    },
    "math": {
        "title": "Math for Real-World Decisions",
        "question": "How can math help people make smarter decisions?",
        "project": "Analyze a real-life data set (budget, transportation, or school issue) and create mathematical models to compare solutions.",
        "deliverable": "Visual report or slide deck with graphs, calculations, and recommendation.",
        "assessment": "Accuracy of calculations, depth of analysis, and justification of conclusions.",
    },
    "ela": {
        "title": "Stories that Inspire Change",
        "question": "How can writing and media influence people to improve their community?",
        "project": "Research a community topic and craft a persuasive multimedia campaign using narrative and evidence.",
        "deliverable": "Podcast, digital magazine, or public service announcement plus written argument.",
        "assessment": "Use of evidence, organization, audience awareness, and communication effectiveness.",
    },
    "social studies": {
        "title": "Civic Action Lab",
        "question": "How can we apply lessons from history and civics to solve current issues?",
        "project": "Investigate a local civic challenge, examine historical parallels, and propose a policy or action plan.",
        "deliverable": "Public policy brief and classroom town-hall presentation.",
        "assessment": "Historical thinking, civic reasoning, and quality of proposed actions.",
    },
}


def _infer_grade_band(grade: str) -> tuple[str, str]:
    normalized = grade.strip().lower()
    if normalized in {"k", "kindergarten"}:
        return GRADE_BANDS["elementary"]

    digits = "".join(ch for ch in normalized if ch.isdigit())
    if digits:
        level = int(digits)
        if level <= 5:
            return GRADE_BANDS["elementary"]
        if level <= 8:
            return GRADE_BANDS["middle"]
        return GRADE_BANDS["high"]

    if "elementary" in normalized:
        return GRADE_BANDS["elementary"]
    if "middle" in normalized:
        return GRADE_BANDS["middle"]
    return GRADE_BANDS["high"]


def generate_lesson_idea(grade: str, subject: str, standard: str | None = None) -> LessonIdea:
    """Generate a project-based lesson idea for the requested grade and subject.

    Args:
        grade: Grade level (for example "3", "7th", "high school").
        subject: Subject name (supported: science, math, ela, social studies).
        standard: Optional content standard code or statement.
    """

    if not grade or not grade.strip():
        raise ValueError("grade is required")
    if not subject or not subject.strip():
        raise ValueError("subject is required")

    normalized_subject = subject.strip().lower()
    if normalized_subject not in SUBJECT_PROJECTS:
        supported = ", ".join(sorted(SUBJECT_PROJECTS))
        raise ValueError(f"Unsupported subject '{subject}'. Supported subjects: {supported}")

    grade_band, learning_style = _infer_grade_band(grade)
    template = SUBJECT_PROJECTS[normalized_subject]

    standards_alignment = (
        f"Align to standard: {standard.strip()} with explicit success criteria and evidence checkpoints."
        if standard and standard.strip()
        else "Use grade-level subject standards for inquiry, communication, and application."
    )

    return LessonIdea(
        title=f"{template['title']} ({grade_band})",
        driving_question=template["question"],
        project=(
            f"For grade {grade}, students engage in {learning_style}. "
            f"{template['project']}"
        ),
        deliverable=template["deliverable"],
        assessment_focus=template["assessment"],
        standards_alignment=standards_alignment,
    )


if __name__ == "__main__":
    example = generate_lesson_idea("7", "science", "MS-ESS3-3")
    print(example)
