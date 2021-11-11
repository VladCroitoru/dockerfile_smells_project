FROM python:3.7-slim

WORKDIR /DECATHLONTEST

ADD . /DECATHLONTEST

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "app.py"]