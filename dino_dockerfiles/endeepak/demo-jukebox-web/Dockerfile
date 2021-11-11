FROM python:2.7.13-alpine

COPY app /opt/demo-jukebox-web

RUN pip install -r /opt/demo-jukebox-web/requirements.txt

EXPOSE 5001
EXPOSE 8001

ENTRYPOINT ["python", "/opt/demo-jukebox-web/server.py"]