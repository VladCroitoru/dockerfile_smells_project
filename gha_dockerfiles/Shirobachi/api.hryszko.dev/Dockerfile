FROM python:3.7-alpine

ADD app/requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

