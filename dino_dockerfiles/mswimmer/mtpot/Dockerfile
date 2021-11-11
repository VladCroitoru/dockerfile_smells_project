FROM python:2

RUN apt-get update && apt-get install busybox

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY *.py /

EXPOSE 23

CMD [ "python", "MTPot.py", "-v", "-o", "/mtpot.log", "/config.json" ]
