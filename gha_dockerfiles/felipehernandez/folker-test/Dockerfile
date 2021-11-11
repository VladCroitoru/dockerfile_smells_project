FROM python:3.9-slim

WORKDIR /

COPY folker folker
COPY ./folker.py folker.py
COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /

ENTRYPOINT ["python", "folker.py"]