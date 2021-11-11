FROM debian:9

RUN apt-get update && apt-get install -y jq curl

RUN curl -L https://github.com/openshift/origin/releases/download/v3.6.0/openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz| \
    tar -zx && \
    mv openshift*/oc /usr/local/bin && \
    rm -rf openshift-origin-client-tools-*


ADD pipe-to-slack.sh /usr/local/bin/pipe-to-slack
RUN chmod 755 /usr/local/bin/pipe-to-slack

ADD stream-events.sh /usr/local/bin/stream-events
RUN chmod 755 /usr/local/bin/stream-events
