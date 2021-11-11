FROM python:2.7.16-slim-stretch

ENV iraf /iraf/iraf/
ENV IRAFARCH linux64
ENV TERM xterm
RUN  apt-get update \
        && apt -y install gcc make flex git \
        && apt -y install libcurl4-openssl-dev libexpat-dev libreadline-dev \
        && apt-get autoclean \
        && rm -rf /var/lib/apt/lists/*

RUN  mkdir -p $iraf \
        && cd /iraf \
        && git clone https://github.com/iraf-community/iraf.git \
        && cd $iraf \
        && git checkout 567961f \
        && ./install < /dev/null \
        && make linux64 \
        && make sysgen

RUN apt-get update \
        && apt-get -y install libx11-dev libcfitsio-bin wget x11-apps libtk8.6 \
        python3 python3-pip openssh-client wcstools libxml2 vim libssl1.0.2 zip \
        && apt-get autoclean \
        && rm -rf /var/lib/apt/lists/*

RUN pip install setuptools==44.1.1
RUN pip install numpy==1.16.6 astropy==2.0.16 pyraf==2.1.15 matplotlib==2.2.4 xhtml2pdf==0.2.4 pathlib2==2.3.5 requests==2.22.0 pytest==3.6.4 stsci.tools==3.6.0 && rm -rf ~/.cache/pip

RUN pip3 install ocs_ingester>=2.2.5 kombu && rm -rf ~/.cache/pip

RUN wget http://ds9.si.edu/download/debian9/ds9.debian9.8.2.1.tar.gz \
        && tar -xzvf ds9.debian9.8.2.1.tar.gz -C /usr/local/bin \
        && rm -rf ds9.debian9.8.2.1.tar.gz

RUN mkdir -p /home/archive/iraf && /usr/sbin/groupadd -g 10000 "domainusers" \
        && /usr/sbin/useradd -g 10000 -d /home/archive -M -N -u 10087 archive \
        && chown -R archive:domainusers /home/archive \
        && mkdir -p /archive/engineering \
        && chown -R archive:domainusers /archive/engineering

USER archive

WORKDIR /home/archive/iraf

RUN mkiraf --term=xgterm -i

USER root

COPY . /usr/src/floyds_pipeline

WORKDIR /usr/src/floyds_pipeline

RUN python setup.py install

USER archive

WORKDIR /home/archive

ENV DISPLAY host.docker.internal:0
