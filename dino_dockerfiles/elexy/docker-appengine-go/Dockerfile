FROM google/golang
MAINTAINER Alex Knol <alexknol@gmail.com>

ENV GAE_VER 1.9.23
ENV GAE_ZIP go_appengine_sdk_linux_amd64-$GAE_VER.zip

RUN apt-get update && \
    apt-get install --yes \
        unzip \
	python

ADD https://storage.googleapis.com/appengine-sdks/featured/$GAE_ZIP .
RUN unzip -q $GAE_ZIP -d /usr/local
RUN rm $GAE_ZIP

ENV PATH $PATH:/usr/local/go_appengine/
