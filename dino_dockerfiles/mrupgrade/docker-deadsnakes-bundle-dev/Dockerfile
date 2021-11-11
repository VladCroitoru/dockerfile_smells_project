FROM ubuntu:xenial

MAINTAINER MrUPGrade itsupgradetime@gmail.com

COPY ./get-pip.py /

RUN apt-get purge -y python.* && \
    echo "deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu xenial main" >> /etc/apt/sources.list && \
    echo "deb-src http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu xenial main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FF3997E83CD969B409FB24BC5BB92C09DB82666C && \
    apt-get update && \
    apt-get install -y build-essential libffi-dev libssl-dev sudo && \
    apt-get install -y  \
        python2.6 python2.6-dev \
        python2.7 python2.7-dev \
        python3.3 python3.3-dev \
        python3.4 python3.4-dev \
        python3.5 python3.5-dev \
        python3.6 python3.6-dev && \
    python2.6 /get-pip.py && \
    python2.7 /get-pip.py && \
    python3.3 /get-pip.py && \
    python3.4 /get-pip.py && \
    python3.5 /get-pip.py && \
    python3.6 /get-pip.py && \
    pip2.6 install --upgrade pip && \
    pip2.7 install --upgrade pip && \
    pip3.3 install --upgrade pip && \
    pip3.4 install --upgrade pip && \
    pip3.5 install --upgrade pip && \
    pip3.6 install --upgrade pip && \
    rm -f /get-pip.py && \
    rm -rf /var/lib/apt/lists/*

CMD ["python3.6"]