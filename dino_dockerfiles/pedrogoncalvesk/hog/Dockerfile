FROM python:2.7

COPY requirements.txt /hog/requirements.txt

WORKDIR /hog

RUN pip install -U pip setuptools

RUN pip install -r requirements.txt

ADD . /hog

CMD ["python", "hog-iterator.py"]