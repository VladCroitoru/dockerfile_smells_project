# FROM node:6.9
# FROM debian:jessie-slim
# FROM debian:8
FROM ubuntu:16.04

MAINTAINER Dan Levy <dan@danlevy.net>

LABEL io.elph.meta.author=dan.levy \
      io.elph.meta.base_image=elasticsuite/docker-build-server

# apt-get install software-properties-common python-software-properties

# a few minor docker-specific tweaks
# see https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap
RUN set -xe \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L40-L48
  && echo '#!/bin/sh' > /usr/sbin/policy-rc.d \
  && echo 'exit 101' >> /usr/sbin/policy-rc.d \
  && chmod +x /usr/sbin/policy-rc.d \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L54-L56
  && dpkg-divert --local --rename --add /sbin/initctl \
  && cp -a /usr/sbin/policy-rc.d /sbin/initctl \
  && sed -i 's/^exit.*/exit 0/' /sbin/initctl \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L71-L78
  && echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L85-L105
  && echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean \
  && echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >> /etc/apt/apt.conf.d/docker-clean \
  && echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L109-L115
  && echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L118-L130
  && echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L134-L151
  && echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests

# delete all the apt list files since they're big and get stale quickly
RUN rm -rf /var/lib/apt/lists/*
# this forces "apt-get update" in dependent images, which is also good

# enable the universe
RUN sed -i 's/^#\s*\(deb.*universe\)$/\1/g' /etc/apt/sources.list

# # make systemd-detect-virt return "docker"
# # See: https://github.com/systemd/systemd/blob/aa0c34279ee40bce2f9681b496922dedbadfca19/src/basic/virt.c#L434
# RUN mkdir -p /run/systemd && echo 'docker' > /run/systemd/container

# # overwrite this with 'CMD []' in a dependent Dockerfile
# CMD ["/bin/bash"]


ENV PATH="/vendor/bundle/ruby/2.1.3/bin:/app/vendor/bundle/ruby/2.1.3/bin:/root/.rvm/bin:/root/.yarn/bin:/usr/local/bin:/usr/bin:/bin:/sbin:/usr/sbin:$PATH" \
    DOCKER_OPTS="--mtu 1400" \
    NVM_DIR=/usr/local/nvm

# # FOR POSTGRES: Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
# RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d
# RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/update-alternatives
RUN mkdir -p /usr/share/man/man1 && mkdir -p /usr/share/man/man7 && \
    apt update -qq && \
    DEBIAN_FRONTEND=noninteractive \
    apt install -y --no-install-recommends \
    build-essential apt-utils lsof sudo ca-certificates dialog gettext imagemagick gnupg2 \
    aufs-tools iptables libmagickwand-dev libc6-dev libffi-dev gnutls-bin sqlite3 libsqlite3-dev \
    curl rsync git-core apt-transport-https openssh-client libcurl3-openssl-dev libyaml-dev \
    python-software-properties software-properties-common postgresql-9.5 libpq-dev gawk \
    libreadline6-dev autoconf libgmp-dev libgdbm-dev libncurses5-dev automake libtool bison
    # reqs for ruby v2.1.x: gawk, libreadline6-dev, autoconf, libgmp-dev, libgdbm-dev, libncurses5-dev, automake, libtool, bison
# cgroupfs-mount
### postgresql-server-dev-9.4
WORKDIR /tmp
COPY Gemfile* /tmp/
# COPY ruby-2.1.3.tgz /app/ruby-2.1.3.tgz
RUN printf 'export PATH="/vendor/bundle/ruby/2.1.3/bin:/app/vendor/bundle/ruby/2.1.3/bin:/root/.rvm/bin:/root/.yarn/bin:/usr/local/bin:$PATH"\n \n[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"\n ' >> /etc/profile
#     sudo tar -xvf /app/ruby-2.1.3.tgz -C /usr/local
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 && \
    /bin/bash -c "curl -L https://get.rvm.io | bash && \
    source /etc/profile.d/rvm.sh && \
    rvm get head && rvm install 2.1.3 && rvm use 2.1.3 && \
    gem install bundler --no-ri --no-rdoc && \
    printf '\n#################\nGEM DEBUG INFO\n##############\n\n' && \
    gem environment"

    #  && bundle install --deployment --path /vendor

    # bundle install  --deployment \
    #                 --jobs 8 \
    #                 --retry 3 \
    #                 --path /vendor

# USER www-data
# RUN DEBIAN_FRONTEND=noninteractive \
#   gem install bundler --no-rdoc --no-ri && \
#   bundle install --deployment --jobs 4 --retry 3 && \
#   rsync -ar vendor / && \
#   printf '\n#################\nGEM DEBUG INFO\n##############\n\n' && \
#   bundle exec gem environment
  #  && \
  # printf '\n#################\nRAILS PKG LOCATIONS\n##############\n\n' && \
  # bundle exec gem which rails railties 2>/dev/null
ENV RANCHER_COMPOSE_VERSION=0.12.1 \
    DOCKER_COMPOSE_VERSION=1.9.0 \
    DOCKER_VERSION=1.12.5

WORKDIR /app
# USER root
### Install docker binary ###
RUN curl --insecure -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz && \
    tar --strip-components=1 -xzf docker-$DOCKER_VERSION.tgz -C /usr/local/bin && \
    chmod +x /usr/local/bin/docker && \
    ### Same deal, install docker-compose ###
    curl --insecure -L "https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-compose-$(uname -s)-$(uname -m)" > /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose &&
    sudo curl -L "https://github.com/rancher/rancher-compose/releases/download/$RANCHER_COMPOSE_VERSION/rancher-compose-linux-amd64-$RANCHER_COMPOSE_VERSION.tar.gz" > /tmp/rancher-compose.tar.gz && \
    sudo tar -xzf /tmp/rancher-compose.tar.gz -C /tmp/ && \
    sudo mv /tmp/rancher-compose-$RANCHER_COMPOSE_VERSION/rancher-compose /usr/local/bin && \
    sudo chmod +x /usr/local/bin/rancher-compose && \
    ### Now Node/Npm/NVM
    /bin/bash -c "curl --insecure -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash && \
    source $NVM_DIR/nvm.sh && nvm install 6 && nvm alias default 6 && nvm use 6"
    # if [ -f \"$(which node)\" ]; then\n    ln -s \"$(which node)\" /usr/local/bin/node\nfi"

  # npm config set user 0 && \
  # npm config set unsafe-perm true && \

# RUN /bin/bash -x -c "source $NVM_DIR/nvm.sh && \
#   printf \" PATH: $PATH  \n nvm path: $(which nvm) \" && \
#   echo $(which node) && \
#   sudo chmod -Rfc 755 $(which node) && \
#   sudo chmod -Rfc 755 $(which npm) && \
#   npm i -g yarn \
#   babel-cli \
#   babel-core \
#   babel-preset-es2015 \
#   gulp-cli \
#   less \
#   less-plugin-autoprefix \
#   less-plugin-clean-css \
#   webpack"

# https://raw.githubusercontent.com/docker/docker/master/contrib/check-config.sh

RUN echo "WARN: INHERIT/OVERRIDE THIS DOCKER IMAGE - SET ENTRYPOINT!"
