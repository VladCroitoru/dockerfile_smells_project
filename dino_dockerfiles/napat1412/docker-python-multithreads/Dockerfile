FROM python:3.6.1-alpine

WORKDIR /usr/src/python

#RUN pip install --no-cache-dir schedule

COPY main.py ..
COPY example .

CMD [ "python", "-u", "../main.py" ]
