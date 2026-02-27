"""Utilities for generating project-based lesson ideas."""


def generate_lesson_idea(grade_level, subject, standard):
    """Return a short project-based learning activity with student voice and choice.

    Args:
        grade_level (str): The grade level for the learners (for example, "5th grade").
        subject (str): The subject area (for example, "science").
        standard (str): The learning standard to address.

    Returns:
        str: A concise lesson activity idea.
    """
    return (
        f"In {grade_level} {subject}, invite students to design a real-world mini project "
        f"that demonstrates mastery of {standard}. Start with a class brainstorm of local "
        "issues or interests, then let students choose their own project format (podcast, "
        "prototype, video, poster, or live demo) and audience. Conclude with reflection and "
        "peer feedback focused on how their choices helped them meet the standard."
    )
