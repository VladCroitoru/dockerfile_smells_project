FROM clojure:alpine
MAINTAINER olhtbr@gmail.com

RUN apk update && \
    apk add git jq wget unzip curl openssh-client && \
    git config --global user.email "git@localhost" && \
    git config --global user.name "git" && \
    mkdir -p /opt/resource/git && \
    wget https://github.com/concourse/git-resource/archive/master.zip -O /opt/resource/git/git-resource.zip && \
    unzip /opt/resource/git/git-resource.zip -d /opt/resource/git && \
    mv /opt/resource/git/git-resource-master/assets/* /opt/resource/git && \
    mv /opt/resource/git/git-resource-master/scripts/install_git_lfs.sh /opt/resource/git && \
    rm -r /opt/resource/git/git-resource.zip /opt/resource/git/git-resource-master && \
    bash /opt/resource/git/install_git_lfs.sh

ADD check in out /opt/resource/

ENV MAVEN_REPO /root/.m2/repository
