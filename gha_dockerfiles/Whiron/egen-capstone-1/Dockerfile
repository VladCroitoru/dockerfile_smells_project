# syntax=docker/dockerfile:1
FROM python:3.7
COPY egen-project-1-327215-1294007c4e28.json egen-project-1-327215-1294007c4e28.json
COPY pub_docker.py pub_docker.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD [ "python3", "pub_docker.py"]
