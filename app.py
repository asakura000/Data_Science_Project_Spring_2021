import flask 
import os
import pickle
import pandas as pd
import getSampleText
from random import choice as c
import random


test_string = 'test_string_here'
app = flask.Flask(__name__, template_folder='templates')

path_to_vectorizer = 'models/vectorizer_me.pkl'
path_to_text_classifier = 'models/text-classifier_me.pkl'
#path_to_image_classifier = 'models/image-classifier.pkl'

# get the list of 100 text strings from another .py file
list_of_sample_texts = getSampleText.samples

# load the pickle files
with open(path_to_vectorizer, 'rb') as f:
    vectorizer = pickle.load(f)

with open(path_to_text_classifier, 'rb') as f:
    model = pickle.load(f)
 

@app.route('/', methods=['GET', 'POST'])
def main():

    miscellaneous = getSampleText.miscellaneous_list
    race = getSampleText.race_list
    gender = getSampleText.gender_list
    other_groups = getSampleText.other_groups_list
    politics = getSampleText.politics_list
    immigration = getSampleText.immigration_list

    global dropdownMenu 

    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))

    if flask.request.method == 'POST':

        # Option 1: user chooses to enter their own text

        if flask.request.form.get('user_input_text'):

            # Get the input from the user.
            user_input_text = flask.request.form['user_input_text']
        
            # Turn the text into numbers using our vectorizer
            X = vectorizer.transform([user_input_text])
            
            # Make a prediction 
            predictions = model.predict(X)
            
            # Get the first and only value of the prediction.
            prediction = predictions[0]

            # Get the predicted probabs
            predicted_probas = model.predict_proba(X)

            # Get the value of the first, and only, predicted proba.
            predicted_proba = predicted_probas[0]

            # The first element in the predicted probabs is % abusive 
            percent_abusive = predicted_proba[0]

            # The second elemnt in predicted probas is % not abusive
            percent_notAbusive = predicted_proba[1]

            return flask.render_template('index.html',
                input_text=user_input_text,
                result=prediction,
                percent_abusive=round(percent_abusive, 4),
                percent_notAbusive=round(percent_notAbusive, 4))

        # Option 2: user chooses a randomly selected text

        elif flask.request.form.get('random'):
            # randomly choose 1 text from a static list of 100
            random_text = c(list_of_sample_texts)

            X = vectorizer.transform([random_text])
            predictions = model.predict(X)
            prediction = predictions[0]
            predicted_probas = model.predict_proba(X)
            predicted_proba = predicted_probas[0]
            percent_abusive = predicted_proba[0]
            percent_notAbusive = predicted_proba[1]

            return flask.render_template('index.html', 
                random_text=random_text,
                result=prediction,
                percent_abusive=round(percent_abusive, 4),
                percent_notAbusive=round(percent_notAbusive, 4))

        # Option 3: Generate dropdown menu
        elif flask.request.form.get('mixed'):
           
           dropdownMenu = random.sample(list_of_sample_texts, 10)
           return flask.render_template('index.html', 
                dropdownMenu=dropdownMenu)

        elif flask.request.form.get('misc'):

            dropdownMenu = miscellaneous
            return flask.render_template('index.html', 
                dropdownMenu=dropdownMenu)

        elif flask.request.form.get('race'):

            dropdownMenu = race
            return flask.render_template('index.html', 
                dropdownMenu=dropdownMenu)

        elif flask.request.form.get('gender'):

            dropdownMenu = gender
            return flask.render_template('index.html', 
                dropdownMenu=dropdownMenu)

        elif flask.request.form.get('immigration'):

            dropdownMenu = immigration
            return flask.render_template('index.html', 
                dropdownMenu=dropdownMenu)

        elif flask.request.form.get('other'):

            dropdownMenu = other_groups
            return flask.render_template('index.html', 
                dropdownMenu=dropdownMenu)

        elif flask.request.form.get('politics'):

            dropdownMenu = politics
            return flask.render_template('index.html', 
                dropdownMenu=dropdownMenu)

        # evaluate the selected text from the dropdown menu
        elif flask.request.form.get('evaluate'):
 
            dropdownMenu = dropdownMenu

            # gets the current value from the dropdown menu
                
            selected = flask.request.form.get('dropdownMenu')

            # converts the current value from dropdown menu into a string
            selected_text = str(selected)

            # predict classification 
            X = vectorizer.transform([selected_text])
            predictions = model.predict(X)
            prediction = predictions[0]
            predicted_probas = model.predict_proba(X)
            predicted_proba = predicted_probas[0]
            percent_abusive = predicted_proba[0]
            percent_notAbusive = predicted_proba[1]

            return flask.render_template('index.html',
                result=prediction,
                percent_abusive=round(percent_abusive, 4),
                percent_notAbusive=round(percent_notAbusive, 4),
                selected_text=selected_text,
                dropdownMenu=dropdownMenu)

# won't need this              
@app.route('/randomlyChoose/', methods=['GET', "POST"])
def randomlyChoose():
    return flask.render_template('randomlyChoose.html')

# won't need this   
@app.route('/dropdown/', methods=['GET', 'POST'])
def dropdown():
    return flask.render_template('dropdown.html')
        
# won't need this   
@app.route('/input_values/', methods=['GET', 'POST'])
def input_values():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('input_values.html'))

    if flask.request.method == 'POST':
        # Get the input from the user.
        var_one = flask.request.form['input_variable_one']
        var_two = flask.request.form['another-input-variable']
        var_three = flask.request.form['third-input-variable']

        list_of_inputs = [var_one, var_two, var_three]

        return(flask.render_template('input_values.html', 
            returned_var_one=var_one,
            returned_var_two=var_two,
            returned_var_three=var_three,
            returned_list=list_of_inputs))

    return(flask.render_template('input_values.html'))

# won't need this   
@app.route('/images/')
def images():
    return flask.render_template('images.html')

# won't need this   
@app.route('/bootstrap/')
def bootstrap():
    return flask.render_template('bootstrap.html')

# won't need this   
@app.route('/classify_image/', methods=['GET', 'POST'])
def classify_image():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('classify_image.html'))

    if flask.request.method == 'POST':
        # Get file object from user input.
        file = flask.request.files['file']

        if file:
            # Read the image using skimage
            img = io.imread(file)

            # Resize the image to match the input the model will accept
            img = transform.resize(img, (28, 28))

            # Flatten the pixels from 28x28 to 784x0
            img = img.flatten()

            # Get prediction of image from classifier
            predictions = image_classifier.predict([img])

            # Get the value of the prediction
            prediction = predictions[0]

            return flask.render_template('classify_image.html', prediction=str(prediction))

    return(flask.render_template('classify_image.html'))

if __name__ == '__main__':
    app.run(debug=True)