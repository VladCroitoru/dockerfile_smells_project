FROM debian:9.3-slim

ENV \
  PATH=/usr/local/flutter/bin:$PATH

RUN apt-get -q update && apt-get install --no-install-recommends -y -q \
  ca-certificates \
  curl \
  git \
  unzip \
  && rm -rf /var/lib/apt/lists/* \
  ;

ARG \
  flutter="alpha"

RUN (cd /usr/local \
  && git clone --branch ${flutter} --depth 1 https://github.com/flutter/flutter.git \
  ) \
  && flutter doctor \
  && flutter config --no-analytics \
  ;

WORKDIR $HOME/

ENTRYPOINT ["flutter"]

CMD ["--version"]
