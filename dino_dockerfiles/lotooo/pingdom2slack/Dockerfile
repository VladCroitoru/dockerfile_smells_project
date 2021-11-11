FROM python:3.5

ENV FLASK_APP=pingdom2slack.py
ENV FLASK_DEBUG=0

RUN mkdir -p /app
WORKDIR /app

COPY . /app

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
