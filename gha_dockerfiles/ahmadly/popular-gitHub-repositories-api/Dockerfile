FROM python:slim-buster

EXPOSE 8000/tcp
WORKDIR /opt/src

COPY requirements.txt .
RUN pip3 install --no-cache-dir --compile --upgrade --force-reinstall --requirement requirements.txt && rm requirements.txt


COPY src/ .
CMD '/opt/src/main.py'
