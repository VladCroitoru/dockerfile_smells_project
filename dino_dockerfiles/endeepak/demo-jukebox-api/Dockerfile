FROM python:2.7.13-alpine

COPY app /opt/demo-jukebox-api

RUN pip install -r /opt/demo-jukebox-api/requirements.txt

EXPOSE 5000
EXPOSE 8000

ENTRYPOINT ["python", "/opt/demo-jukebox-api/server.py"]