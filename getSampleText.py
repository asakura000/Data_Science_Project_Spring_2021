# script to access sample of 100 texts from csv file

import pandas as pd
import numpy as np
from random import choice as c
import random

df = pd.read_csv('100_SAMPLES.csv')

# convert text column to a list of 100 strings
samples = df.text.tolist()

# choose 1 at random 
sampleOne = c(samples)

# choose 10 at random - for dropdown menu --- used for testing, not in actual app
sampleThree = random.sample(samples, 3)

# creating category-specific lists for the dropdown menu section of the app
miscellaneous = df['category'] == 'miscellaneous'
miscellaneous_list = df[miscellaneous].text.tolist()

race = df['category'] == 'race'
race_list = df[race].text.tolist()

politics = df['category'] == 'politics'
politics_list = df[politics].text.tolist()

immigration = df['category'] == 'immigration'
immigration_list = df[immigration].text.tolist()

other_groups = df['category'] == 'other groups'
other_groups_list = df[other_groups].text.tolist()

gender = df['category'] == 'gender'
gender_list = df[gender].text.tolist()
