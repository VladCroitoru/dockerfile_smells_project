FROM python:3.6.4-slim-stretch

RUN mkdir /app

ADD requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD arris_events.py /app/arris_events.py

CMD /usr/local/bin/python /app/arris_events.py

