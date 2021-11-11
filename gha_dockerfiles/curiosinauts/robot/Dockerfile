ARG BASE_VERSION
FROM docker-registry.int.curiosityworks.org/7onetella/base:${BASE_VERSION}

ARG PLATFORMCTL_VERSION
ENV PLATFORMCTL_VERSION ${PLATFORMCTL_VERSION}

USER root

COPY --chown=coder:coder  robot_linux_amd64  /robot
COPY --chown=coder:coder  entrypoint.sh      /entrypoint.sh

RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x ./kubectl           && \
    mv ./kubectl /usr/local/bin

RUN mkdir -p /home/coder/.kube && chown coder:coder /home/coder/.kube
COPY --chown=coder:coder config /home/coder/.kube/config
RUN chown coder:coder /home/coder/.kube/config 

COPY --chown=coder:coder .ssh /home/coder/.ssh

RUN set -x; curl -L https://github.com/curiosinauts/platformctl/releases/download/v${PLATFORMCTL_VERSION}/platformctl_${PLATFORMCTL_VERSION}_Linux_x86_64.tar.gz | tar -xvz -C . && sudo mv platformctl /usr/local/bin

RUN  chmod +x /entrypoint.sh             && \
     chmod +x /robot                     && \
     chmod +x /usr/local/bin/platformctl

EXPOSE 22
EXPOSE 3000

USER 1000
ENV USER=coder
WORKDIR /home/coder
USER coder

CMD /entrypoint.sh