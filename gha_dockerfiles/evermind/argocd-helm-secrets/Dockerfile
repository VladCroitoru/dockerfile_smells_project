FROM argoproj/argocd:v2.1.3

ARG HELM_SECRETS_VERSION=v3.8.3
ARG SOPS_VERSION=v3.7.1

# Switch to root user to perform installation
USER root  
COPY helm-wrapper.sh /usr/local/bin/    
RUN apt-get update && \
    apt-get install -y \
    curl \
    nano \
    gpg
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    curl -o /usr/local/bin/sops -L https://github.com/mozilla/sops/releases/download/${SOPS_VERSION}/sops-${SOPS_VERSION}.linux && \
    chmod +x /usr/local/bin/sops 

RUN curl -o /usr/local/bin/kubectl -L "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl" && \ 
    chmod +x /usr/local/bin/kubectl

RUN cd /usr/local/bin && \
    mv helm helm.bin && \
    mv helm2 helm2.bin && \
    mv helm-wrapper.sh helm && \
    ln helm helm2 && \
    chmod +x helm helm2

# install plugin for argocd user
USER argocd
# set HELM_PLUGINS makes sure that plugin is found later on by helm
ENV HELM_PLUGINS="/home/argocd/.local/share/helm/plugins/"
RUN helm.bin plugin install https://github.com/jkroepke/helm-secrets --version ${HELM_SECRETS_VERSION}

