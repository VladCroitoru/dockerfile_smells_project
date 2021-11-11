FROM continuumio/miniconda
MAINTAINER Carl Janzen <carl.janzen@gmail.com>

RUN apt-get update \
    && apt-get install -y \
      git \
      build-essential \
      python-dev \
      python-pip \
      python-virtualenv \
      unzip

# instead of using /bin/sh, use bash login shell for better nvm/rvm install
SHELL ["/bin/bash", "--login", "-c"]

# set up empty home directory with standard rc files from /etc/skel
ENV HOME /home/someuser
RUN cp -ar /etc/skel ${HOME}

# install nvm, current nodejs, and some common packages
ENV NVM_CLONE_DIR ${HOME}/.nvm
RUN git clone https://github.com/creationix/nvm.git ${HOME}/.nvm \
    && cd ${HOME}/.nvm \
    && git checkout `git describe --abbrev=0 --tags --match "v[0-9]*" origin` \
    && source ${HOME}/.nvm/nvm.sh \
    && nvm install node \
    && nvm use node \
    && npm install -g \
        bower \
        generator-angular \
        generator-karma \
        generator-webapp \
        grunt \ 
        grunt-cli \
        gulp \
        gulp-cli \
        yeoman-generator \
        yo 


# install rvm, current ruby, and some common packages
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 \
    && curl -L https://get.rvm.io | bash -s stable --path ${HOME}/.rvm \
    && source "${HOME}/.rvm/scripts/rvm" \
    && rvm install ruby \
    && rm -rf /var/lib/apt/lists/* \
    && rvm use ruby \
    && gem install \
        bundler \
        compass

#  newly created rvm group gets GID 1000 which conflicts with the mounting strategy, so assign some other GID!
RUN groupmod -g 150 rvm 

# install gosu per: https://gist.github.com/DevoKun/5154c6e645f9ded0f3bd
RUN gpg --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && curl -o /usr/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/bin/gosu.asc \
    && rm /usr/bin/gosu.asc \
    && chmod +x /usr/bin/gosu

VOLUME /tmp
WORKDIR /tmp
COPY entrypoint.sh /usr/bin
COPY login /usr/bin
COPY scripts.sh /usr/local/bin
COPY webdev-toolkit.sh /usr/local/bin
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD ["/bin/bash"]
