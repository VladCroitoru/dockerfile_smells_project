FROM openjdk:8-jdk-alpine

ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

ENV TZ Asia/Taipei
ENV HOME /home/jenkins

# If you bind mount a volume from the host or a data container, 
# ensure you use the same uid
RUN addgroup -g ${gid} ${group} \
    && adduser -h "$HOME" -u ${uid} -G ${group} -G ping -s /bin/bash -D ${user}

# install docker
RUN apk add --no-cache \
    ca-certificates \
    curl \
    bash \
    openssl

ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 1.12.3
ENV DOCKER_SHA256 626601deb41d9706ac98da23f673af6c0d4631c4d194a677a9a1a07d7219fa0f

RUN set -x \
	&& curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz \
	&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
	&& tar -xzvf docker.tgz \
	&& mv docker/* /usr/local/bin/ \
	&& rmdir docker \
	&& rm docker.tgz \
	&& docker -v

# set up jenkins slave
ARG VERSION=2.62
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

# set up sbt
RUN curl -Ls https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt > /usr/local/bin/sbt && \
    chmod 755 /usr/local/bin/sbt
RUN apk add --no-cache \
    git

# download kubectl
ARG KUBERNETES_VERSION=1.4.6
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl && \
    chmod 755 /usr/local/bin/kubectl
#RUN ln -s /usr/local/bin/hyperkube /usr/local/bin/kubectl

RUN mkdir -p /opt && chmod a+w /opt

USER jenkins
RUN mkdir /home/jenkins/.jenkins
VOLUME /home/jenkins/.jenkins
WORKDIR /home/jenkins
COPY jenkins-slave /usr/local/bin/jenkins-slave

RUN mkdir -p sbt-init && cd sbt-init \
  && sbt -v -211 -sbt-create about \
  && cd .. \
  && rm -rf sbt-init \
  && tar -cvf /opt/sbt-caches.tar.gz .ivy2 .sbt \
  && rm -rf .ivy2 .sbt

COPY entrypoint.sh /home/jenkins/entrypoint.sh
ENTRYPOINT ["/home/jenkins/entrypoint.sh"]
