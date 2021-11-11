FROM ubuntu:latest

ENV USERNAME developer
ENV REMOTES /remotes
ENV MANIFEST_REPO ${REMOTES}/remote-00/manifest.git

RUN apt-get update \
 && apt-get install --yes \
        git repo \
        bash-completion man-db vim \
 && apt-get autoclean \
 && mkdir --mode=777 ${REMOTES} \
 && adduser --disabled-password --gecos '' ${USERNAME}

USER ${USERNAME}

RUN git config --global user.name Developer \
 && git config --global user.email developer@example.com \
 && git init --quiet --bare ${MANIFEST_REPO} \
 && git clone --quiet ${MANIFEST_REPO} /tmp/m \
 && echo "<?xml version='1.0' encoding='UTF-8'?><manifest>" >> /tmp/m/default.xml \
 && for r in $(seq --format='remote-%02g' 1 2); do \
      echo "  <remote  name='${r}' fetch='${REMOTES}/${r}' />" >> /tmp/m/default.xml; \
      for n in $(seq --format='project-%02g' 1 8); do \
        p=${REMOTES}/${r}/${n}.git; \
        git init --quiet --bare ${p}; \
        git clone --quiet ${p} /tmp/p; \
        git -C /tmp/p commit --quiet --allow-empty --allow-empty-message --message=''; \
        git -C /tmp/p push --quiet origin master; \
        rm --force --recursive /tmp/p; \
        echo "  <project remote='${r}' name='${n}' path='${r}.${n}' revision='refs/heads/master' />" >> /tmp/m/default.xml; \
      done \
    done \
 && echo "</manifest>" >> /tmp/m/default.xml \
 && git -C /tmp/m add default.xml \
 && git -C /tmp/m commit --quiet --message='Adding manifest' \
 && git -C /tmp/m push --quiet origin master \
 && rm --force --recursive /tmp/m

WORKDIR /home/${USERNAME}
