FROM docker:latest

RUN apk --update add bash curl wget ca-certificates git less openssl \
      openssh-client p7zip python py-lxml py-pip rsync sshpass \
      sudo git vim zip && \
    apk --update add --virtual build-dependencies python-dev \
      libffi-dev openssl-dev build-base && \
    pip install --upgrade pip && \
    pip install ansible && \
    pip install ansible-container[docker] && \
    apk add openjdk8 maven && \
    export JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk/
    
