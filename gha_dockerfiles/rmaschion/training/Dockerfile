FROM python:3.9
# MAINTAINER python_student

RUN mkdir training_project/
COPY requirements.txt training_project/
COPY setup.py training_project/setup.py
RUN cd training_project

RUN pip3 install --upgrade pip
RUN pip3 install -e .
RUN pip3 install -r training_project/requirements.txt

WORKDIR training_project/app

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
