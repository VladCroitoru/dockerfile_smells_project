FROM jenkins:alpine

USER root

RUN addgroup -g 233 docker \
 && apk add --no-cache \
      docker \
      py2-pip \
      python \
      shadow \
 && pip install --no-cache-dir \
      awscli \
 && usermod -a -G docker jenkins \
 && docker --version \
 && git --version \
 && aws --version

USER jenkins

RUN git config --global credential.helper '!aws codecommit credential-helper $@' \
 && git config --global credential.UseHttpPath true \
 && mv ~/.gitconfig /usr/share/jenkins/ref
