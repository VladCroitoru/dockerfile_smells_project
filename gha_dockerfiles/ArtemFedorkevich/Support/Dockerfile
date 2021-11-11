FROM python:3.9.7
RUN mkdir -p /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
