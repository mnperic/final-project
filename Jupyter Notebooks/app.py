# 1. import dependencies
import numpy as np
import pandas as pd
import io
import os
import csv 
from flask import Flask, request, send_file

@app.route('/')
def index():
 
    return render_template("index.html")


