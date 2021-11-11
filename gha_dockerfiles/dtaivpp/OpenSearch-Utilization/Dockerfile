FROM python:3
LABEL MAINTAINER="David Tippett"

ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /code
ADD .env .env
COPY ./github-collector .

CMD python /code/runner.py
