FROM python
RUN pip install influxdb
RUN git clone https://github.com/barrycarey/Cyberpower-UPS-Stats-For-InfluxDB.git
RUN mv Cyberpower-UPS-Stats-For-InfluxDB/CyberpowerUpsStats.py /
RUN rm -rf Cyberpower-UPS-Stats-For-InfluxDB
VOLUME /data/
WORKDIR /data/
CMD ["python", "/CyberpowerUpsStats.py"]
