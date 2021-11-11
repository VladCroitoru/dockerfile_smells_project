FROM debian:stretch
RUN apt-get update && apt-get install -y python3 python3-pip python3-gdal python3-pil unzip && rm -rf /var/lib/apt/lists/*
RUN mkdir /app
RUN mkdir /app/data
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

ADD wtmse.py /app/wtmse.py
ADD generator /app/generator
ADD utils /app/utils

EXPOSE 5000

RUN cd /app/generator/sentinel2/utils/data/ && unzip S2A_OPER.kml.zip

WORKDIR /app/
ENTRYPOINT ["python3", "/app/wtmse.py"]

