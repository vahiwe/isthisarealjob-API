from flask import Flask, render_template, url_for, request, jsonify, redirect
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import matplotlib.pyplot as plt
import urllib
import nltk
import spacy
# import en_core_web_sm
from nltk.corpus import stopwords
from PIL import Image
from gingerit.gingerit import GingerIt
import googlemaps
from grammer import *
from address import *
from nairaland import *
from confidence import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """
    GET Request
    """
    # Give message to user
    return redirect("https://documenter.getpostman.com/view/9310664/SW11VxQY?version=latest")


@app.route('/', methods=['POST'])
def analyze():
    """
    POST Request
    """
    data = request.get_json(force=True)
    try:
        searchTerm = data['company']
        addressTerm = data['address']
        inviteTerm = data['invite']
        # data = [data]
    except KeyError:
        titl = "You have a KeyError. Please check your JSON input"
        return jsonify(errors=titl)


    board = 29
    try:
        j = 0
        while j < 20:
            if j == 0:
                nextItem = False
            else:
                nextItem = True
            commentsCurrent = search_item(searchTerm, nextItem, j,  board)
            add_to_word_list(commentsCurrent)
            j += 1
    except:
        titlee = "Search failed"
        comm = "Try again"
        return jsonify(errors=titlee)


    polarity = 0
    positive = 0
    negative = 0
    neutral = 0


    previous = []

    for tweet in WordList:
        if tweet in previous:
            continue
        previous.append(tweet)
        analysis = TextBlob(tweet)
        """evaluating polarity of comments"""
        polarity += analysis.sentiment.polarity

        if (analysis.sentiment.polarity == 0):
            neutral += 1
        elif (analysis.sentiment.polarity < 0.00):
            negative += 1
        elif (analysis.sentiment.polarity > 0.0):
            positive += 1

    noOfSearchTerms = positive + negative + neutral

    positive = percentage(positive, noOfSearchTerms)
    negative = percentage(negative, noOfSearchTerms)
    neutral = percentage(neutral, noOfSearchTerms)

    titl = "How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " comments from " + "on nairaland"

    if (negative> 30):
        comm = "There is a high percentage of negative comments about this Company online in regards to jobs"
    elif(negative>20):
        comm = "There are some negative comments about this Company in regards to jobs" 
    elif (negative<20):
        comm = "There is a low percentage of negative comments about this Company online in regards to jobs"


    addr = verify_address(addressTerm)
    if addr == "The Company address is valid":
        cont = "This address looks legit"
        auth = True
    else:
        cont = "This address might be bogus"
        auth = False


    inv = check(inviteTerm)
    correction = inv
    if inv == 0:
        contt = "There are no errors in this invitation"
    else:
        contt = "You have errors in this invitation"

    report = confidence_interval(correction, auth, negative)

    return jsonify(report=report)

@app.route('/form', methods=['POST'])
def analyze_form():
    """
    POST Request
    """
    try:
        searchTerm = request.form['company']
        addressTerm = request.form['address']
        inviteTerm = request.form['invite']
        # data = [data]
    except KeyError:
        titl = "You have a KeyError. Please check your Form input"
        return jsonify(errors=titl)


    board = 29
    try:
        j = 0
        while j < 20:
            if j == 0:
                nextItem = False
            else:
                nextItem = True
            commentsCurrent = search_item(searchTerm, nextItem, j,  board)
            add_to_word_list(commentsCurrent)
            j += 1
    except:
        titlee = "Search failed"
        comm = "Try again"
        return jsonify(errors=titlee)


    polarity = 0
    positive = 0
    negative = 0
    neutral = 0


    previous = []

    for tweet in WordList:
        if tweet in previous:
            continue
        previous.append(tweet)
        analysis = TextBlob(tweet)
        """evaluating polarity of comments"""
        polarity += analysis.sentiment.polarity

        if (analysis.sentiment.polarity == 0):
            neutral += 1
        elif (analysis.sentiment.polarity < 0.00):
            negative += 1
        elif (analysis.sentiment.polarity > 0.0):
            positive += 1

    noOfSearchTerms = positive + negative + neutral

    positive = percentage(positive, noOfSearchTerms)
    negative = percentage(negative, noOfSearchTerms)
    neutral = percentage(neutral, noOfSearchTerms)

    titl = "How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " comments from " + "on nairaland"

    if (negative> 30):
        comm = "There is a high percentage of negative comments about this Company online in regards to jobs"
    elif(negative>20):
        comm = "There are some negative comments about this Company in regards to jobs" 
    elif (negative<20):
        comm = "There is a low percentage of negative comments about this Company online in regards to jobs"


    addr = verify_address(addressTerm)
    if addr == "The Company address is valid":
        cont = "This address looks legit"
        auth = True
    else:
        cont = "This address might be bogus"
        auth = False


    inv = check(inviteTerm)
    correction = inv
    if inv == 0:
        contt = "There are no errors in this invitation"
    else:
        contt = "You have errors in this invitation"

    report = confidence_interval(correction, auth, negative)

    return jsonify(report=report)

if __name__ == '__main__':
    app.run(port=5000, debug=True)