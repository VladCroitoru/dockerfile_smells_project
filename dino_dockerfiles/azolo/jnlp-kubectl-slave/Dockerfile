FROM jenkins/jnlp-slave:alpine

USER root

RUN apk --no-cache add bash curl

RUN wget "https://storage.googleapis.com/kubernetes-release/release/$(wget -qO- https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin/kubectl

RUN wget -O- "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh" | bash \
    && chmod +x ./kustomize \
    && mv ./kustomize /usr/local/bin/kustomize

RUN git lfs install

USER jenkins
