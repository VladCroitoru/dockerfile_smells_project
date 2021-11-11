FROM ubuntu:18.04
ENV TZ=America/Denver
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y ca-certificates apt-transport-https gnupg2 curl software-properties-common && \
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list && \
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable" && \
    apt-get update -y && \
    apt-get install -y kubectl awscli gettext docker-ce docker-ce-cli containerd.io
WORKDIR /app
COPY entrypoint.sh .
RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]