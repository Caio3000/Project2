from Project2_Flask import app, forms, main_functions
from flask import request, render_template
from Project2_Flask.forms import generateDataFromAPI
import requests, json

api_key_dict = main_functions.read_from_file("Project2_Flask/JSON_Files/api_keys.json")
api_key = api_key_dict["my_ny_key"]

@app.route('/', methods=['GET', 'POST'])
def search():
    my_form = forms.NewsForm(request.form)

    if request.method == 'POST':
        first_name = request.form["first_name"]
        date = request.form["date"]
        list_name = request.form["list_name"]

        # Couldn't figure out how to run this from forms :/ sorry
        url = "https://api.nytimes.com/svc/books/v3/lists/" + date + "/" + list_name + ".json?api-key="
        final_url = url + api_key
        response_ = requests.get(final_url).json()
        main_functions.save_to_file(response_, "Project2_Flask/JSON_Files/response.json")
        data = main_functions.read_from_file("Project2_Flask/JSON_Files/response.json")

        book1 = data['results']['books'][0]['title']
        book2 = data['results']['books'][1]['title']
        book3 = data['results']['books'][2]['title']
        book4 = data['results']['books'][3]['title']
        book5 = data['results']['books'][4]['title']

        response = [first_name, book1, book2, book3, book4, book5]

        return render_template('results.html', response=response, form=my_form)
    return render_template('search.html', form=my_form)


