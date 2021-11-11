FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy

RUN python -m spacy download en
CMD python insults.py
