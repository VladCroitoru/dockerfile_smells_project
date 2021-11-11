FROM garland/butterfly
RUN apt-get update -y && apt-get install -y curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN curl -o /usr/bin/docker https://get.docker.com/builds/Linux/x86_64/docker-1.9.1;chmod +x /usr/bin/docker
RUN curl -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.2.0/bin/linux/amd64/kubectl;chmod +x /usr/bin/kubectl
