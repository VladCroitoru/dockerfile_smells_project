FROM java:8-jre

ENV SAUCE_VERSION 4.5.3

ENV SAUCE_USERNAME ""
ENV SAUCE_ACCESS_KEY ""

WORKDIR /usr/local/sauce-connect

RUN wget https://saucelabs.com/downloads/sc-$SAUCE_VERSION-linux.tar.gz -O - | tar -xz

WORKDIR /usr/local/sauce-connect/sc-$SAUCE_VERSION-linux

EXPOSE 4445
EXPOSE 8032

ENV PATH /usr/local/sauce-connect/sc-$SAUCE_VERSION-linux/bin:$PATH

ENTRYPOINT ["sc"]
