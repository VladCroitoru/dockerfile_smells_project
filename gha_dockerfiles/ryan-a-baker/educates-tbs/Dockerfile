FROM quay.io/eduk8s/base-environment:master

USER root
RUN curl -L -o /usr/local/bin/kp https://github.com/vmware-tanzu/kpack-cli/releases/download/v0.3.1/kp-linux-0.3.1 && \
  chmod 755 /usr/local/bin/kp
RUN curl -sSL "https://github.com/buildpacks/pack/releases/download/v0.20.0/pack-v0.20.0-linux.tgz" | sudo tar -C /usr/local/bin/ --no-same-owner -xzv pack
USER 1001