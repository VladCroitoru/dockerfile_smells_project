FROM python:alpine

COPY exporter.py /exporter.py

RUN pip install --no-cache-dir requests

CMD [ "python", "/exporter.py" ]
