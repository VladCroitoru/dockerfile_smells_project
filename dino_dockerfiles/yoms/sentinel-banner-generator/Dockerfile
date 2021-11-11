FROM debian:stretch
RUN apt-get update && apt-get install -y python3 python3-pip python3-gdal python3-pil unzip && rm -rf /var/lib/apt/lists/*
RUN mkdir /app
RUN mkdir /app/data
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

ADD sbg.py /app/sbg.py
ADD banner_generator.py /app/banner_generator.py
ADD sentinel_downloader.py /app/sentinel_downloader.py
ADD data/S2A_OPER.kml.zip /app/data/S2A_OPER.kml.zip
RUN cd /app/data && unzip S2A_OPER.kml.zip

WORKDIR /app/
ENTRYPOINT ["python3", "/app/sbg.py"]

