# jessie
FROM jenkinsci/jenkins:latest

USER root
WORKDIR /root

RUN apt-get clean \
    && rm -rf \
        * \
        .bash_logout \
        .bashrc \
        .config \
        .profile \
        /root/.??* \
        /tmp/* \
        /var/lib/apt/lists/* \
        /var/tmp/* \

USER jenkins
WORKDIR /
