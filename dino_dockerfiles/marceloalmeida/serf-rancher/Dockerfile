FROM alpine:edge
MAINTAINER Marcelo Almeida <marcelo.almeida@jumia.com>

ENV \
  UNZIP="python -c \"import zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall(sys.argv[1] if len(sys.argv) == 2 else '.')\""

RUN \
  apk --update add curl python jq bash && \
  curl -s https://releases.hashicorp.com/serf/0.8.0/serf_0.8.0_linux_amd64.zip | sh -c "$UNZIP /usr/local/bin/" && \
  chmod a+x /usr/local/bin/serf && \
  apk --purge del python

ADD etc /etc
ADD start_serf_agent.sh /root/

CMD sh /root/start_serf_agent.sh
