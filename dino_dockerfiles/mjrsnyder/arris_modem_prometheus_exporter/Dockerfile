FROM python:3.6.4-slim-stretch

RUN mkdir /app

ADD requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD arris_exporter.py /app/arris_exporter.py

CMD /usr/local/bin/python /app/arris_exporter.py

