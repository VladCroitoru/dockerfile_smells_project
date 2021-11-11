
FROM minfeng/geo-env:latest
LABEL creator Min Feng

ADD . /opt/lib
RUN cd /opt/lib && python3 setup.py install
RUN rm -rf /opt/lib
