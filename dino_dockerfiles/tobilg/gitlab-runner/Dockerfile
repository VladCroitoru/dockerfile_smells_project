FROM gitlab/gitlab-runner
MAINTAINER tobilg <fb.tools.github@gmail.com>

RUN apt-get update && apt-get install -y \
    curl \
    lxc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install docker-compose 1.5.2 (latest supported version for CoreOS stable, uses Docker 1.8.3)
RUN curl -L https://github.com/docker/compose/releases/download/1.5.2/docker-compose-Linux-x86_64 > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

ADD register-and-run /
RUN chmod +x /register-and-run

ENTRYPOINT ["/register-and-run"]
