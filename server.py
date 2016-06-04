# -*- coding: utf-8 -*-
from flask import Flask, render_template
    # redirect, request, flash, session

from jinja2 import StrictUndefined

import random

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Raises an error if you use an undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined

################################################################################


@app.route('/')
def display_homepage():

    return render_template('home.html')


@app.route('/comments')
def open_comment_generator():

    comment = BERNIE_COMMENTS[random.randrange(1, 16)]

    return render_template('comments.html', comment=comment)


@app.route('/new-comment')
def generate_new_comment():

    return BERNIE_COMMENTS[random.randrange(1, 16)]


################################################################################
BERNIE_COMMENTS = {
    1: "Hillary is a corporate shill!",
    2: "Another biased Bernie article from the lamestream media #overit #unfollowing",
    3: "What people fail to realize is that Bernie has INDEPENDENTS on his side, about 75 percent of the electorate.",
    4: "Why are people criticizing Bernie's positions on racial justice? Don't they know Bernie marched with MLK???",
    5: "Debbie Wasserman Schultz has rigged the democratic primary from the beginning #ourdemocracyisajoke",
    6: "Yes Bernie is trailing in the primary, but it's okay because he's starting a POLITICAL REVOLUTION.",
    7: "Of course Bernie should stay in the race, there's still a .00001 percent chance he could win!",
    8: "The rights of women, minorities, and immigrants are on the line this election, but voting my conscience matters more #writinginbernie",
    9: "Bernie has shattered all records for small campaign donations because he is for THE PEOPLE. Proud to say I just sent him the $27 I was gonna use to buy weed this month!",
    10: "Bernie voted against a war 15 years ago. That's all the foreign policy experience I need in my future president!",
    11: "Hillary only voted with Bernie 98 percent of the time while they were in Congress together. I won't cast my vote for a neocon witch! #writinginbernie",
    12: "Vote for a man who spent his entire political career representing a state that is 75 percent forest #imwithhim",
    13: "I'm voting for Bernie since he's the candidate I want to get an artisanally-crafted, microbrewed beer with.",
    14: "You say you're making a valid criticism of Bernie's policy proposals, but really we all know you're in the pocket of big banks.",
    15: "Bernie is the only candidate that can defeat Trump, according to all the highly unreliable polls I consulted #thefactsspeakforthemselves"
    }

################################################################################
if __name__ == "__main__":

    app.run()
