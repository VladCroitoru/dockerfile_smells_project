FROM python:2.7

RUN mkdir /app

COPY shareme /app

EXPOSE 5000

WORKDIR /app

RUN pip install -r requirements.txt

CMD python share-folder-http.py
