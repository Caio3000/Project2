from Project2_Flask import app, main_functions
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, RadioField, SelectField
import requests

api_key_dict = main_functions.read_from_file("Project2_Flask/JSON_Files/api_keys.json")
api_key = api_key_dict["my_ny_key"]

class NewsForm(FlaskForm):
    first_name = StringField("First Name")

    date = RadioField("Choose Date",
                      choices=[('', 'Current'),
                              ('2020-08-01', 'August'),
                              ('2020-09-01', 'September'),
                              ('2020-10-01', 'October'),
                              ('2020-11-01', 'November')])

    list_name = SelectField("List Name",
                         choices=[('hardcover-fiction', 'Hardcover Fiction'),
                                  ('hardcover-nonfiction', 'Hardcover Nonfiction')
                                  ])


def generateDataFromAPI():


    url = "https://api.nytimes.com/svc/books/v3/lists/" + date + "/" + list_name + ".json"
    final_url = url + api_key
    response = requests.get(final_url).json()
    main_functions.save_to_file(response, "Project2_Flask/JSON_Files/response.json")
    response_dict = main_functions.read_from_file("Project2_Flask/JSON_Files/response.json")

