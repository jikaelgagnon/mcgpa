import pandas as pd

predictions = pd.read_csv("predictions.csv")
profs = pd.read_csv("prof_scores.csv")
results = pd.read_csv("results.csv")

def get_prediction(course, prof=""):
    predicted_mark_raw = predictions[predictions["Course"]==course]["predicted_avg"].values[0]
    try:
        prof_score = profs[profs["prof"]==prof]["diff_from_avg"]
    except:
        prof_score = 0
    return predicted_mark_raw + prof_score

def get_num_credits(course):
    return results[results["course"]==course]["credits"].mean()

def predict_gpa(current_gpa, current_credits, courses, profs):
    """
    courses is a list of course names
    profs is a list of prof names
    """
    predicted_marks = []
    credits = []
    
    for i in range(len(courses)):
        predicted_marks.append(get_prediction(courses[i], profs[i]))
        credits.append(get_num_credits(courses[i]))

    credits_mult_marks = sum([a * b for a, b in zip(predicted_marks, credits)])
    # print(credits_mult_marks)
    print(predicted_marks)
    return (current_credits * current_gpa + credits_mult_marks) / (sum(credits) + current_credits)

gpa = 4.0
current_credits = 55
current_courses = ['PHIL230', 'COMP330', 'COMP451','COMP302','MATH208']
profs = ['Howard, Christopher', 'Spinoso-Di Piano, Cesare', 'Ravanbakhsh, Siamak', 'Errington, Jacob', ' Lee, Kiwon']


# print(predict_gpa(gpa, current_credits, current_courses, profs))

