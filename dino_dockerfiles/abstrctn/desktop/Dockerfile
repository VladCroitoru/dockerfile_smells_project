FROM ubuntu:xenial

RUN apt-get update && apt-get install -y git vim wget ruby-full build-essential patch zlib1g-dev curl libcurl3

# Install kubernetes-secret-env
ENV KUBERNETES_SECRET_ENV_VERSION=0.0.1
RUN \
  mkdir -p /etc/secret-volume && \
  cd /usr/local/bin && \
  wget -q https://github.com/newsdev/kubernetes-secret-env/releases/download/$KUBERNETES_SECRET_ENV_VERSION/kubernetes-secret-env && \
  chmod +x kubernetes-secret-env

RUN curl https://sdk.cloud.google.com | bash
RUN gcloud components install kubectl

# Gem setup
RUN gem install bundler

RUN rm -rf /root
WORKDIR /root

CMD [ "sleep", "infinity" ]
