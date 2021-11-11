FROM debian:stretch-slim

RUN apt-get update \
     && apt-get install -y \
                        wget \
                        gnupg \
     && wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add - \
     && wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/jessie.list \
     && apt-get update \
      && apt-get install -y \
                         python-pip \
                         mopidy \
    && pip install mopidy-moped \
    && apt-get purge --auto-remove -y \
        wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.cache

COPY start.sh /start.sh

RUN chmod a+x /start.sh

ENTRYPOINT [ "/start.sh" ]
