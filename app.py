from flask import Flask, render_template, url_for, request, jsonify, redirect
import requests
import pandas
from bs4 import BeautifulSoup
from textblob import TextBlob
import matplotlib.pyplot as plt
import urllib
import nltk
import spacy
import queue
from threading import Thread
from nltk.corpus import stopwords
from PIL import Image
from gingerit.gingerit import GingerIt
import googlemaps
from time import time
from grammer import *
from address import *
from nairaland import *
from confidence import *
from cac_check import *


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """
    GET Request
    """
    # Give message to user
    return redirect("https://documenter.getpostman.com/view/9310664/SW132eE3?version=latest")


@app.route('/', methods=['POST'])
def analyze():
    """
    POST Request
    """
    start_time = time()
    data = request.get_json(force=True)
    try:
        searchTerm = data['company']
        addressTerm = data['address']
        inviteTerm = data['invite']
    except KeyError:
        titl = "You have a KeyError. Please check your JSON input"
        return jsonify(errors=titl)

    jobres = []
    que = queue.Queue()
    threads_list = list()

    t = Thread(target=lambda q, arg1: q.put(nairasearch(arg1)), args=(que, searchTerm))
    t.start()
    threads_list.append(t)

    t2 = Thread(target=lambda q, arg1: q.put(scraper(arg1)), args=(que, searchTerm))
    t2.start()
    threads_list.append(t2)

    t3 = Thread(target=lambda q, arg1: q.put(verify_address(arg1)), args=(que, addressTerm))
    t3.start()
    threads_list.append(t3)

    t4 = Thread(target=lambda q, arg1: q.put(check(arg1)), args=(que, inviteTerm))
    t4.start()
    threads_list.append(t4)

    # Join all the threads
    for t in threads_list:
        t.join()

    # Check thread's return value
    while not que.empty():
        result = que.get()
        jobres.append(result)


    for i in range(len(jobres)):
        if isinstance(jobres[i], pandas.core.frame.DataFrame):
            dg = jobres[i]
        if isinstance(jobres[i], int) or isinstance(jobres[i], float):
            negative = jobres[i]
        if isinstance(jobres[i], bool):
            auth = jobres[i]
        if isinstance(jobres[i], list):
            correction = jobres[i]
            correction = correction[0]


    if dg.empty:
        cac = True
    else:
        cac = False

    report = confidence_interval(correction, auth, negative, cac)
    print('Time to solve: ', time() - start_time)
    return jsonify(confidence=report)

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


    jobres = []
    que = queue.Queue()
    threads_list = list()

    t = Thread(target=lambda q, arg1: q.put(nairasearch(arg1)), args=(que, searchTerm))
    t.start()
    threads_list.append(t)

    t2 = Thread(target=lambda q, arg1: q.put(scraper(arg1)), args=(que, searchTerm))
    t2.start()
    threads_list.append(t2)

    t3 = Thread(target=lambda q, arg1: q.put(verify_address(arg1)), args=(que, addressTerm))
    t3.start()
    threads_list.append(t3)

    t4 = Thread(target=lambda q, arg1: q.put(check(arg1)), args=(que, inviteTerm))
    t4.start()
    threads_list.append(t4)

    # Join all the threads
    for t in threads_list:
        t.join()

    # Check thread's return value
    while not que.empty():
        result = que.get()
        jobres.append(result)


    for i in range(len(jobres)):
        if isinstance(jobres[i], pandas.core.frame.DataFrame):
            dg = jobres[i]
        if isinstance(jobres[i], int) or isinstance(jobres[i], float):
            negative = jobres[i]
        if isinstance(jobres[i], bool):
            auth = jobres[i]
        if isinstance(jobres[i], list):
            correction = jobres[i]
            correction = correction[0]


    if dg.empty:
        cac = True
    else:
        cac = False

    report = confidence_interval(correction, auth, negative, cac)
    return jsonify(confidence=report)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
