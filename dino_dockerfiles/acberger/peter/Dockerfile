FROM alpine:latest
MAINTAINER Johannes Hofmeister <docker@spam.cessor.de>

# To Build:
# docker build -t cessor/peter -f Dockerfile .

# To Run:
# docker run --name peter -d -p 5000:5000 --link mongodb:mongodb cessor/peter

RUN echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk add --no-cache mongodb
VOLUME /data/db


RUN apk add --update bash curl g++ python python-dev py-pip && \
    rm -rf /var/cache/apk/*

RUN pip install pip --upgrade
RUN pip install setuptools --upgrade
RUN pip install tornado
RUN pip install motor

ADD ./src /var/peter

# Generate Cookie Secret Key
RUN python -c "import random,string; print 'cookie_secret=\'%s\'' % ''.join([random.choice(string.letters+string.digits) for _ in range(32)])" >> /var/peter/config/docker.cfg

# Generate Admin Password
RUN python -c "import random,string; print ''.join([random.choice(string.letters+string.digits) for _ in range(12)])" > /var/peter/.key

# Write this down.
RUN echo Your Password for /admin/login is: $(cat /var/peter/.key)

ENV PETER_ENV=docker
CMD { mongod &  python /var/peter/serve-fast.py ; }
