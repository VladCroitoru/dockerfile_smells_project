FROM cloutainer/k8s-jenkins-slave-base:v22

#
# INSTALL AND CONFIGURE
#
COPY docker-entrypoint-hook.sh /opt/docker-entrypoint-hook.sh
RUN chmod u+rx,g+rx,o+rx,a-w /opt/docker-entrypoint-hook.sh

#
# KUBERNETES CLI (kubectl)
#
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl

#
# DOCKER CLI
#
RUN curl -fsSL get.docker.com -o get-docker.sh && \
    sh get-docker.sh && \
    usermod -aG docker jenkins

#
# UTILS
#
COPY util-wait-for-http-200.sh /usr/local/bin/util-wait-for-http-200.sh
RUN chmod +x /usr/local/bin/util-wait-for-http-200.sh


#
# XML UTILS
#
COPY util-get-pom-xml-version.sh /usr/local/bin/util-get-pom-xml-version.sh
RUN apt-get -qqy update && apt-get -qqy --no-install-recommends install xmlstarlet rsync && \
    chmod +x /usr/local/bin/util-get-pom-xml-version.sh



USER root
