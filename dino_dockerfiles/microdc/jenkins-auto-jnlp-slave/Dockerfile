FROM openjdk:8-alpine

ENV AZURE_CLI_VERSION=2.0.67
ENV KUBECTL_VERSION=1.14.3

# those are allowed to be changed at build time`
ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

RUN apk --no-cache add curl dumb-init git openssh-client bash jq gettext

#Install Docker
RUN apk --no-cache add shadow su-exec docker
RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' > /etc/nsswitch.conf

#Install aws cli and azure cli
RUN apk --no-cache add su-exec docker groff python py-pip gettext procps xz jq && \
    apk --no-cache add --virtual=build gcc libffi-dev musl-dev openssl-dev python-dev python3-dev make linux-headers && \
    pip --no-cache-dir install -U pip && \
    pip --no-cache-dir install awscli s3cmd azure-cli==${AZURE_CLI_VERSION} yamllint && \
    apk del --purge build

#Install kubectl
RUN curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && chmod +x /usr/bin/kubectl

# Install shellcheck for validating shell scripts in CI pipelines
RUN curl -o /tmp/shellcheck.tar.xz https://shellcheck.storage.googleapis.com/shellcheck-v0.5.0.linux.x86_64.tar.xz && \
    cd /tmp && tar xJf shellcheck.tar.xz && cd shellcheck-* && \
    mv shellcheck /usr/local/bin && rm -r /tmp/shellcheck*

ENV JENKINS_HOME=/var/jenkins_home \
    JENKINS_USER=${user}

RUN  groupadd -g ${gid} ${group} && \
     useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user} && \
     sed -i '/^Host \*/a \ \ \ \ ServerAliveInterval 30' /etc/ssh/ssh_config && \
     sed -i '/^Host \*/a \ \ \ \ StrictHostKeyChecking no' /etc/ssh/ssh_config

# Jenkins home directory is a volume, so configuration and build history
# can be persisted and survive image upgrades
VOLUME $JENKINS_HOME

COPY jenkins-slave /usr/local/bin/jenkins-slave
RUN chmod +x /usr/local/bin/jenkins-slave

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/usr/local/bin/jenkins-slave"]
