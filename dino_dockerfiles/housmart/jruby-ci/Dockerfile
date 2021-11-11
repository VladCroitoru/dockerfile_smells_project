FROM jruby:9.1.7
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

ENV EMBULK_VERSION 0.8.15
RUN wget https://dl.bintray.com/embulk/maven/embulk-${EMBULK_VERSION}.jar -O /usr/local/bin/embulk
RUN chmod +x /usr/local/bin/embulk
ENV PATH /usr/local/bin/embulk:$PATH

RUN apt-get update -y && \
    apt-get install -y git python-dev && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    pip install awscli

