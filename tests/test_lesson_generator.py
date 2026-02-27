import unittest

from lesson_generator import generate_lesson_idea


class LessonGeneratorTests(unittest.TestCase):
    def test_generates_with_standard(self):
        idea = generate_lesson_idea("3", "math", "CCSS.MATH.CONTENT.3.OA.A.1")
        self.assertIn("K-5", idea.title)
        self.assertIn("Align to standard", idea.standards_alignment)
        self.assertIn("CCSS.MATH.CONTENT.3.OA.A.1", idea.standards_alignment)

    def test_generates_without_standard(self):
        idea = generate_lesson_idea("10", "science")
        self.assertIn("9-12", idea.title)
        self.assertIn("grade-level subject standards", idea.standards_alignment)

    def test_rejects_unknown_subject(self):
        with self.assertRaises(ValueError):
            generate_lesson_idea("7", "art")


if __name__ == "__main__":
    unittest.main()
