FROM python:3.8-slim

RUN mkdir /vampi 
#RUN apt-get update add bash nano gcc
RUN apt-get update
RUN apt-get -y install gcc

ENV vulnerable=1
ENV tokentimetolive=60

COPY . /vampi
WORKDIR /vampi

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
