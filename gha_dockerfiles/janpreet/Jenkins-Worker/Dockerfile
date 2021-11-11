FROM ubuntu
LABEL Maintainer="Janpreet Singh"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y && \
         apt-get full-upgrade

RUN apt-get install -y \
    git \
    wget \
    openssh-server \
    openjdk-8-jdk \
    maven

RUN /usr/bin/ssh-keygen -A

ADD ./sshd_config /etc/ssh/sshd_config

RUN useradd jenkins -m -s /bin/bash

RUN echo jenkins:jenkins | chpasswd

RUN echo "jenkins  ALL=(ALL)  ALL" >> etc/sudoers

RUN mkdir -p /var/run/sshd
RUN mkdir /home/jenkins/.m2

RUN chown -R jenkins:jenkins /home/jenkins/.m2/ 

ENV HELM_VERSION="v3.4.0"

RUN wget -q https://get.helm.sh/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm 
RUN chmod +x /usr/local/bin/helm 

RUN helm repo add janpreet https://janpreet.github.io/helm-charts/
RUN helm repo update

RUN wget -q https://dl.k8s.io/v1.16.15/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]