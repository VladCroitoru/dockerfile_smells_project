FROM dceoy/oanda-cli:latest

ADD https://github.com/dceoy/oanda-cli/archive/master.tar.gz /tmp/oanda-cli.tar.gz
ADD . /tmp/fract

RUN set -e \
      && pip install -U --no-cache-dir /tmp/oanda-cli.tar.gz /tmp/fract \
      && rm -rf /tmp/oanda-cli.tar.gz /tmp/fract

ENTRYPOINT ["/usr/local/bin/fract"]
