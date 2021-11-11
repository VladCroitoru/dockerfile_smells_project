FROM python:2.7

RUN apt-get update && apt-get install -qq -y --no-install-recommends \
  unzip \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# runner goodness
ADD https://github.com/dweinstein/analysis-runner/archive/v3.0.0.zip /tmp/runner.zip
RUN unzip -j /tmp/runner.zip -d /opt/runner && \
    rm -f /tmp/runner.zip

ENV PYTHON /usr/local/bin/python2.7
ENV TOOL ${PYTHON} ./androbugs.py
ENV CONTENT_TYPE application/json

WORKDIR /opt/androbugs

ADD . /opt/androbugs

ENTRYPOINT ["/opt/runner/runner.sh", "${TOOL}"]
