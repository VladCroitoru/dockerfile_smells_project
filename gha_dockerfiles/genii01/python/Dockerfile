FROM python:3.7.3-alpine

ENV APP_HOME /app
WORKDIR $APP-HOME

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py]
