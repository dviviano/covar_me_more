# this file contains all controller functions that are called on the different
# routes in cvapp

import string, os
from flask import render_template, flash
from datamodels import *

if os.environ.get('PRESENTATION') != None:
    with open(os.environ.get('PRESENTATION')) as f:
        rmdhtml = f.read().decode('utf-8')

def show_homepage():
    return render_template('index.html')

def show_allocation_form():
    tickers = ['AB','ABC']
    return render_template('allocate.html',
                           tickers=tickers)

def show_allocated_portfolio(form):
    time_horizon = form['horizon']
    tickers = form['ticker_selection'].split(',')
    return render_template('index.html')
