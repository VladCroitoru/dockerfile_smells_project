FROM python:2
MAINTAINER Jon Bullen

RUN apt-get update && apt-get install -y \
        libssl-dev \
        libusb-1.0-0 \
        python-dev \
        swig \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install --upgrade pip

ADD requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
RUN pip --no-cache-dir install https://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-0.24.0.tar.gz
#RUN pip --no-cache-dir install firetv[firetv-server]
RUN pip install git+git://github.com/sytone/python-firetv.git

# Default listening port.
EXPOSE 5556

# The configuration yaml for persistance.
VOLUME /config

ENTRYPOINT ["firetv-server"]

# By default show help. 
CMD ["--help"]

# docker build -t docker-firetv .
# docker run -it --rm --name python-firetv -p 5556:5556 sytone/python-firetv
# docker run -d --restart=always -v E:/myconfigpath:/config --name python-firetv -p 5556:5556 sytone/python-firetv

# docker run -it --rm -v C:/config:/config --name python-firetv -p 5556:5556 sytone/python-firetv2 -v --config /config/house.yaml
# docker run -d --restart=always -v E:/myconfigpath:/config --name python-firetv -p 5556:5556 sytone/python-firetv -v --config /config/house.yaml
