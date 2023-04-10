class Student:
    def __init__(self,student_name,student_cohort):
        self.name = student_name
        self.cohort = student_cohort
        # self.language = favourite_language

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self,language):
        if language == "Python":
            return "I love Python"