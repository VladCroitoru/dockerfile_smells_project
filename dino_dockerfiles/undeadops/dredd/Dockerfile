FROM python:2.7-alpine

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora

EXPOSE "5000"
CMD ["python", "app.py"]
