# This file was generated from the README.md in the GitHub repository.
FROM erlang:19.2

RUN apt-get update \
    && apt-get install -y inotify-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /workdir
COPY files/watcherl.sh /usr/local/bin/watcherl.sh
RUN chmod +x /usr/local/bin/watcherl.sh
CMD ["watcherl.sh"]
COPY files/dot_erlang /root/.erlang