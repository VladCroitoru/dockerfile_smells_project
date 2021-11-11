# each statement makes a new layer
# set base image (host OS)
FROM python:3
LABEL stage=builder

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -U pip && pip install -r requirements.txt

# copy the content of the local directory to the working directory
COPY . .

# create an Ipython profile to manage default imports
RUN ipython profile create template --ipython-dir /code/.ipython && \
    echo "c.InteractiveShellApp.exec_lines = \
    ['import jsonutils as js', \
    'from jsonutils.base import JSONObject, \
    JSONDict, \
    JSONList, \
    JSONStr, \
    JSONFloat, \
    JSONInt, \
    JSONNull, \
    JSONBool, \
    JSONUnknown', \
    'from jsonutils.exceptions import *', \
    'from jsonutils.query import I, SingleQuery, All, ExtractYear', \
    'from jsonutils.functions.parsers import parse_float, \
    parse_datetime, parse_bool, parse_json, url_validator, \
    parse_int, parse_timestamp', \
    'from jsonutils.functions.dummy import dummy_json', \
    'from jsonutils.functions.converters import dict_to_list', \
    'from jsonutils.functions.seekers import DefaultDict, DefaultList', \
    'from datetime import date, datetime', \
    'import pytz', \
    'import json', \
    'import re', \
    'import requests', \
    'test = JSONObject.open(\'jsonutils/tests/json-schema-test.json\')' \
    ]" >> /code/.ipython/profile_template/ipython_config.py

# set ipython environment variable
ENV IPYTHONDIR=/code/.ipython

RUN python -m unittest -v

# command to run on container start
CMD [ "ipython", "--profile=template" ] 
