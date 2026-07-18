from class_test import Survey
def test_survey():
    question="what's your age"
    age_survey=Survey(question)
    ans=['18','16','14']
    for an in ans:
        age_survey.add_answer(an)
    assert ans == age_survey.answers