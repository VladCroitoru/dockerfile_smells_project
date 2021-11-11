FROM debian
MAINTAINER sirEgghead

RUN apt-get update \
  && apt-get -q -y install \
    git \
    openssl \
    python-dev \
    python-openssl \
    python-pyasn1 \
    python-twisted \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd -d /kippo -s /bin/bash -m kippo -g sudo
RUN git clone -q --depth 1 https://github.com/desaster/kippo.git /kippo-app
RUN mv /kippo-app/kippo.cfg.dist /kippo-app/kippo.cfg
RUN chown kippo /kippo-app -R
RUN /kippo-app/utils/passdb.py /kippo-app/data/pass.db add pass
RUN /kippo-app/utils/passdb.py /kippo-app/data/pass.db add password
RUN /kippo-app/utils/passdb.py /kippo-app/data/pass.db add 123
RUN /kippo-app/utils/passdb.py /kippo-app/data/pass.db add root

EXPOSE 2222
USER kippo
WORKDIR /kippo-app
CMD ["twistd", "--nodaemon", "-y", "kippo.tac", "--pidfile=kippo.pid"]
