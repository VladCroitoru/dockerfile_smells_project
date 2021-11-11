#FROM debian:latest
FROM marcelmaatkamp/gnuradio

# Update and override policy output
RUN apt-get update
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d

# Install base packages
RUN apt-get install -y python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev git wget
RUN pip install twisted && pip install txws && pip install pyephem && pip install pyserial && pip install service_identity && pip install x509

RUN git clone https://github.com/kpreid/shinysdr/ /tmp/shinysdr && cd /tmp/shinysdr && ./fetch-js-deps.sh && python setup.py build && python setup.py install

RUN mkdir /config
COPY config.py /config

EXPOSE 8080 8081

ENTRYPOINT ["shinysdr", "/config"]
