FROM google/python
MAINTAINER Matt Bailey <m@mdb.io>

# Data to backup
VOLUME /data

# Working directory
RUN mkdir -p /duplicity
WORKDIR /duplicity

# Add requirements
ADD requirements.txt /duplicity/requirements.txt

# Install librsync-dev
RUN apt-get -y install librsync-dev

# Install python requirements
RUN pip install --upgrade --requirement /duplicity/requirements.txt

# Get duplicity
ADD https://code.launchpad.net/duplicity/0.6-series/0.6.25/+download/duplicity-0.6.25.tar.gz /tmp/duplicity.tgz

# Extract
RUN tar -xzf /tmp/duplicity.tgz --strip-components 1 && ./setup.py install

# Runtime to perform backup
ENTRYPOINT ["/usr/local/bin/duplicity"]
CMD ["--full-if-older-than", "1M", "/data", "dpbx:///duplicity"]
