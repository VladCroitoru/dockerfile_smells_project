ARG JENKINS_VERSION=2.122

FROM jenkins/jenkins:${JENKINS_VERSION}-alpine
LABEL maintainer="Calvin Park <calvinspark@gmail.com>"

# Skip install wizard & give it 10 GB memory
# Override with command line arg if necessary
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false -Xmx10240m"

# Install usermod
USER root
RUN mkdir -p /etc/apk/ \
 && echo http://dl-2.alpinelinux.org/alpine/edge/community/ >> /etc/apk/repositories \
 && apk --no-cache add shadow

# Accept uid/gid as runtime parameters, then
# modify jenkins user and its home directory
COPY entrypoint.sh /
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
