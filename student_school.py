class Student:
    def __init__(self, score, preferred_schools):
        self.score = score
        self.preferred_school = preferred_schools
        self.school = None

    def set_school(self, school):
        self.school = school



class School:
    def __init__(self, school_id, seats):
        self.school_id = school_id
        self.seats = seats
        self.students = []

    def add_pupil(self, student):
        if self.seats > 0:
            self.students.append(student)
            student.set_school(self)
            self.seats -= 1
            return True
        else:
            return False


def allocate_schools(school_seats_array, student_scores_array, student_school_preferrence_array):
    schools = {index: School(index, seats) for index, seats in enumerate(school_seats_array)}
    students = []

    for score, preferred_schools in zip(student_scores_array, student_school_preferrence_array):
        studnets.append(Student(score, preference_schools))

    for student in sorted(students, key=lambda x: x.score, reverse = True):
        for school_id in studnet.preferred_schools:
            if schools[school_id].add_pupil(student):
                break

    unfilled = sum([school.seats for school in schools.value()])
    unassigned = len([studnet for student in students if not student.school])

