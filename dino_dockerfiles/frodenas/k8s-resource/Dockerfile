FROM concourse/buildroot:base

ARG kubernetes_version=1.15.5

ADD https://storage.googleapis.com/kubernetes-release/release/v${kubernetes_version}/bin/linux/amd64/kubectl /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*
