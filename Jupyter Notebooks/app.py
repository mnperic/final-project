# 1. import dependencies
import numpy as np
import pandas as pd
import io
import os
import csv 
from flask import Flask, request, send_file

app = Flask(__name__)
@app.route("/")


