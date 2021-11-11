FROM sameersbn/gitlab-ci-runner:latest
MAINTAINER sameer@damagehead.com

RUN apt-get update && \
    apt-get install -y ca-certificates-java java-common java-wrappers \
    openjdk-7-jdk openjdk-7-jre maven \
    git lftp p7zip-full && \
    rm -rf /var/lib/apt/lists/* # 20140918

ADD assets/ /app/
RUN chmod 755 /app/setup/install
RUN /app/setup/install
