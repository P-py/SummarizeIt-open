from flask import Flask, render_template, request, flash
from flask.wrappers import Response
import wikipedia
import requests #delete
import json #delete

app = Flask(__name__)

#PLEASE CHANGE THIS PART IF YOU WANT TO RUN YOUR CODE IN A PRODUCTION SERVER OR DEPLOY IT
with open('./key.0') as file:
    app.secret_key = file.read()
################################


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        language = request.form['language']
        objective = request.form['objective']


        language_codes = ['fr', 'en', 'pt', 'de', 'nl', 'it']
        for code in language_codes:
            if language == code:
                wikipedia.set_lang(code)

        #Legacy way
        """ if language == "fr":
            wikipedia.set_lang('fr')
        elif language == "en":
            wikipedia.set_lang('en')
        elif language == "pt-br":
            wikipedia.set_lang('pt')
        elif language == "de":
            wikipedia.set_lang('de')
        elif language == "nl":
            wikipedia.set_lang('nl')
        elif language == "it":
            wikipedia.set_lang('it') """

        
        try:
            page = wikipedia.page(str(objective))
            title = page.title
            link = page.url
            summary = wikipedia.summary(str(objective))
            return render_template('result.html', title=title, url=link, summary=summary)
        except:
            flash("Couldn't find any wikipedia info-sources with that specific name. Please verify if the name matches any existing page or check the grammar.", category="error")
            return render_template('index.html')

    return render_template('index.html')

@app.route("/about")
def about_page():
    return render_template('about.html')