FROM maven
RUN curl -fsSL https://download.docker.com/linux/static/stable/x86_64/docker-17.12.0-ce.tgz -o /tmp/docker.tgz && tar --strip-components=1 -xvzf /tmp/docker.tgz -C /usr/local/bin && rm /tmp/docker.tgz
WORKDIR /srv
CMD /bin/bash
