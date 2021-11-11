FROM gitlab/gitlab-runner
MAINTAINER Raymond Rutjes <raymond.rutjes@gmail.com>

RUN apt-get update && apt-get install -y \
    curl \
    lxc \
    && rm -rf /var/lib/apt/lists/*

# Install docker-compose
RUN curl -L https://github.com/docker/compose/releases/download/1.4.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

ADD register-and-run /
RUN chmod +x /register-and-run

ENTRYPOINT ["/register-and-run"]
