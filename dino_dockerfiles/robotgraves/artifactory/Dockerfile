FROM robotgraves/virtualpython
MAINTAINER apaul@transparent.com

RUN apt-get install -y bzip2 \
    zlib1g-dev libopenjpeg-dev libjpeg-dev \
    libcurl4-openssl-dev libssl-dev

ADD requirements-cpython.txt /opt/requirements-cpython.txt

RUN opt/v/bin/pip install -U -r /opt/requirements-cpython.txt && \
    rm /opt/requirements-cpython.txt

# change this add based on project #
ADD scripts /opt/scripts
EXPOSE 8000
WORKDIR /opt

CMD ["/opt/v/bin/python", "/opt/scripts/artifact_cleanup.py"]