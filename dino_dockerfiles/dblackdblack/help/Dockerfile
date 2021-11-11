FROM ubuntu:bionic

ENV KUBECTL_VERSION=1.12.7 \
    KUBECTL_DATE=2019-03-27 \
    KUBECTL_SHA256=fbfa5c8c43a25ae6595c3060364ceb53b02cab2fa4750f840830e523531553e6

RUN apt-get update && apt-get -y install \
    netcat-openbsd curl wget mtr-tiny iputils-ping bind9-host \
    iproute2 net-tools vim tmux ssh lsof screen dtach dnsutils \
    lynx psmisc strace apt-transport-https postgresql-client \
    software-properties-common gnupg jq tcpdump httpie \
    python-pip python3-pip build-essential \
    gcc g++ make locales traceroute groff \
  && apt-get clean \
  && ln -sf /bin/bash /bin/sh

RUN add-apt-repository ppa:git-core/ppa \
  && apt-get update \
  && apt-get -y install git \
  && apt-get clean \
  && export KUBECTL_URL=https://amazon-eks.s3-us-west-2.amazonaws.com/${KUBECTL_VERSION}/${KUBECTL_DATE}/bin/linux/amd64/kubectl \
  && wget -O /usr/local/bin/kubectl ${KUBECTL_URL} \
  && echo "${KUBECTL_SHA256} /usr/local/bin/kubectl" | sha256sum --check \
  && chmod +x /usr/local/bin/kubectl

ENV PYTHON_PACKAGES="boto boto3 ipython redis"

RUN pip install $PYTHON_PACKAGES \
  && pip3 install $PYTHON_PACKAGES \
  && pip3 install awscli

ADD ["https://hey-release.s3.us-east-2.amazonaws.com/hey_linux_amd64", "/usr/local/bin/hey"]
RUN chmod +x /usr/local/bin/hey

CMD ["bash", "-xec", "exec sleep infinity"]
