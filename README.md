
1. Jupyter Notebook: for exploratory data analysis and for comparing different models for performance
2. The rest of the files are part of the flask app - some of the main ones listed here with description:
    a. app.py - links the back-end python code with the front end (html and css) so what you see on the website gets it info from the database
    
    
    b. myModel.py - actually handles the database and creates the model to be imported as a pickle file into app.py
    
    
    c. index.html - contains the layout for the web app, the code for the web page style, and a little bit of javascript for the guage feature on the web app
    
    
    d. 100_sample.csv - I wanted to create features on the app that would make it so people who don't necessarily want to type anything into the textbox, or just want to test drive the app, and see how the model evaluate texts from a sample of 100 that I compiled. 
    
    
    e. getSampleText.py - creates lists (arrays) out of the 100 sample csv file, and splits it up by categories.
    
    
    f. abusive_language_data.csv - the database that this model is based on
    
