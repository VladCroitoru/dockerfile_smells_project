FROM python:2

RUN \
 apt-get update &&\
 DEBIAN_FRONTEND=noninteractive apt-get install -yq wireless-tools aircrack-ng tcpdump tshark &&\
 apt-get clean &&\
 rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /application/iSniff-GPS
ENV PYTHONPATH /application/iSniff-GPS/iSniff_GPS

COPY color.py iSniff_import.py manage.py requirements.txt run.sh /application/iSniff-GPS/
COPY iSniff_GPS /application/iSniff-GPS/iSniff_GPS
RUN pip install -U -r requirements.txt

RUN echo "yes" | ./manage.py syncdb
CMD ["./manage.py","runserver","0.0.0.0:80"]
