# Lesson Idea Generator

Simple project-based lesson idea generator that creates a lesson from:
- grade
- subject
- optional standard

## Usage

```python
from lesson_generator import generate_lesson_idea

idea = generate_lesson_idea("5", "math", "CCSS.MATH.CONTENT.5.MD.A.1")
print(idea)
```

Supported subjects:
- science
- math
- ela
- social studies
