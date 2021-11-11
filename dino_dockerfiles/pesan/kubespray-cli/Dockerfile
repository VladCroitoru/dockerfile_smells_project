FROM alpine:3.7

RUN apk add --no-cache \
  openssh \
  git \
  py-pip \
  build-base \
  python-dev \
  libffi-dev \
  openssl-dev \
  ansible \
  && pip2 install --upgrade pip \
  && pip2 install kubespray==0.5.2

CMD ["sh"]
