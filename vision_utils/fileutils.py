import csv
import json
import os
from os.path import *

def create_dir_if_not_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def check_if_exists(dir):
    return os.path.exists(dir)

def read_csv_file(csv_path):
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows=[]
        for row in csv_reader:
            rows.append(row)
        return rows


def read_file(image_path):
    text_file = open(image_path, "r")
    txt = text_file.readlines()
    text_file.close()
    return txt


def read_json_file(jsonfile):
    with open(jsonfile) as json_file:
        json_data = json.load(json_file)
        return json_data


def read_text_file(text_file):
    with open(text_file, 'r') as txt_file:
        content = txt_file.readlines();
        return content

def save_to_file(save_file, data):
    with open(save_file, mode='wt', encoding='utf-8') as myfile:
        myfile.write("\n".join(data))
    myfile.close()
