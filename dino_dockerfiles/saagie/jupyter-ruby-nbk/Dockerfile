FROM jupyter/minimal-notebook:0b3ec811c968

MAINTAINER Saagie

USER root

# Create default workdir (useful if no volume mounted)
RUN mkdir /notebooks-dir && chown 1000:100 /notebooks-dir

RUN apt-get update && \
	apt-get install --no-install-recommends -y software-properties-common \
	curl gnupg2 dirmngr libtool libleveldb-dev gawk zlib1g-dev libyaml-dev \
	libsqlite3-dev sqlite3 autoconf libgmp-dev libgdbm-dev libncurses5-dev \
	automake bison pkg-config libffi-dev libgmp-dev libreadline6-dev libssl-dev

# Hack used to be able to install rbczmq
RUN ln -s /usr/bin/libtoolize /usr/bin/libtool

USER $NB_USER

RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB

# Install RVM
RUN curl -L https://get.rvm.io | bash -s stable

# Check if any system library is missing
RUN /bin/bash -l -c "rvm requirements"

# Enable rvm for Jovyan user
RUN echo "source $HOME/.rvm/scripts/rvm" >> ~/.bashrc
RUN /bin/bash -l -c "source $HOME/.rvm/scripts/rvm"

# Install Ruby 2.4.x
RUN /bin/bash -l -c "rvm install 2.4"
RUN /bin/bash -l -c "rvm use 2.4 --default"

# Install Ruby dependencies
RUN /bin/bash -l -c "gem install --no-ri --no-rdoc bundler:1.16.1 rbczmq:1.7.9 iruby:0.3 nyaplot:0.1.6 distribution:0.7.3 impala:0.5.1 mikon:0.1.3 statsample:2.1.0 mongo:2.4.3 cabalist:0.0.4 ml:0.4.0 classifier-reborn:2.2.0 executable-hooks:1.3.2"
# RUN /bin/bash -l -c "gem install --user-install executable-hooks:1.3.2"

RUN /bin/bash -l -c "iruby register"

# Define default workdir
WORKDIR /notebooks-dir

# Default: run without authentication
CMD ["/bin/bash", "-l", "-c", "start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''"]
