FROM debian:latest
RUN apt update && apt -y install curl python3-pip git && pip3 install yamllint
ADD https://github.com/garethr/kubeval/releases/download/0.7.1/kubeval-linux-amd64.tar.gz /kubeval-linux-amd64.tar.gz
RUN tar -C /usr/local/bin -xf /kubeval-linux-amd64.tar.gz && rm /kubeval-linux-amd64.tar.gz
ADD https://github.com/garethr/kubetest/releases/download/0.1.1/kubetest-linux-amd64.tar.gz /kubetest-linux-amd64.tar.gz
RUN tar -C /usr/local/bin -xf /kubetest-linux-amd64.tar.gz

RUN set -x; cd "$(mktemp -d)" && \
    curl -fsSLO https://github.com/FairwindsOps/pluto/releases/download/v2.2.0/pluto_2.2.0_linux_amd64.tar.gz && \
    tar zxvf pluto_2.2.0_linux_amd64.tar.gz && \
    mv pluto /usr/local/bin/pluto
