FROM python:3.7-slim

MAINTAINER James Boyce <mail@its-jam.es> 

COPY resources/state-data.json resources/state-data.json
COPY resources/nsw.json resources/nsw.json
COPY *.py .
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt \
 && python3 -m pytest *.py

ENTRYPOINT ["python3", "post_covid_stats.py"]