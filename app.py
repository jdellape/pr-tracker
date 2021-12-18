from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    #Get existing records to display to user
    pr_logs = None
    with open('personal_records.json', 'r') as f:
        pr_logs = json.load(f)
        print(pr_logs)
    return render_template('index.html', pr_logs=pr_logs)

@app.route('/submit', methods=['POST'])
def my_form_post():
    #Get the input submitted by user
    input_lift_type = request.form['lift_type']
    input_weight = request.form['weight']
    input_reps = request.form['reps']
    input_date = request.form['date']
    if request.method == 'POST':
        #Update json file
        with open('personal_records.json', 'r+') as jf:
            pr_dict = {'lift':input_lift_type,'weight':input_weight, 'reps':input_reps, 'date':input_date}
            file_data = json.load(jf)
            file_data.append(pr_dict)
            jf.seek(0)
            json.dump(file_data, jf, indent=2)
        #Update records to show to the user
        with open('personal_records.json', 'r') as f:
            pr_logs = json.load(f)
    return render_template('index.html', pr_logs=pr_logs)


if __name__ == '__main__':
    app.debug = True
    app.run()