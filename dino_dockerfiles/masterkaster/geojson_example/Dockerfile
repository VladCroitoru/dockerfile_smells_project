FROM python:2.7

RUN pip install -U girder_worker_utils

COPY script.py /script.py

ENTRYPOINT ["python", "/script.py"]
