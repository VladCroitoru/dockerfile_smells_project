FROM garland/butterfly
RUN apt-get update -y && apt-get install -y curl vim git && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN curl -o /usr/bin/docker https://get.docker.com/builds/Linux/x86_64/docker-1.10.3;chmod +x /usr/bin/docker
RUN curl -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.3.5/bin/linux/amd64/kubectl;chmod +x /usr/bin/kubectl
RUN curl -o /usr/bin/helmc https://storage.googleapis.com/helm-classic/helmc-latest-linux-amd64;chmod +x /usr/bin/helmc
ADD bash_aliases /root/.bash_aliases
