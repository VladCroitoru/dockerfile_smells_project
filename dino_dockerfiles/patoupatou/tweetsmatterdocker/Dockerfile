FROM frolvlad/alpine-python3:latest
MAINTAINER Gabriel G. <gabrielpolloguilbert@gmail.com>

ENV RELEASE_VERSION=0.3

WORKDIR /tweetsmatter

ADD https://github.com/opendwellers/TweetsMatter/archive/${RELEASE_VERSION}.tar.gz . 

RUN pip install tweepy simplejson urllib3

RUN tar xvfz ${RELEASE_VERSION}.tar.gz && \
        rm ${RELEASE_VERSION}.tar.gz && \
        mv -v TweetsMatter-${RELEASE_VERSION} tweetsmatter

VOLUME tweetsmatter/config

ENTRYPOINT ["python3", "tweetsmatter/App.py", "tweetsmatter/config"]
