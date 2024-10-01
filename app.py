import flask as Flask, render_template, request, redirect
from helper import get_predictions

app = Flask(__name__)

data = dict()
positive = 0
negative = 0

@app.route("/")
def index():

    data['positive'] = positive
    data['negative'] = negative
    data['total'] = positive+negative

    return render_template('index.html', data=data)

@app.route("/", methods = ['post'])
def my_post():

    city_development_index = request.form['city_development_index']
    relevent_experience = request.form['relevent_experience']
    education_level = request.form['education_level']
    total_experience = request.form['total_experience']
    last_new_job_gap = request.form['last_new_job_gap']

    prediction = get_predictions(city_development_index, relevent_experience, education_level, total_experience, last_new_job_gap)

    if prediction == 1:
        global positive
        positive+=1 #looking for a job change
    else:
        global negative
        negative+=1 #not looking for a job change 

    return redirect(request.url)


if __name__ =="__main__":
    app.run()
