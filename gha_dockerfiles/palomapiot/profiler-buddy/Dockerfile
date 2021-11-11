FROM python:3.7

LABEL maintainer="paloma.piot@udc.es"

RUN apt update && apt-get install -y python3 

COPY . /profiler

EXPOSE 5000

WORKDIR /profiler

RUN pip install -r requirements.txt

CMD python profiler.py