from ubuntu:14.04

run apt-get update -y
run apt-get install -y mercurial
run apt-get install -y git
run apt-get install -y python
run apt-get install -y curl
run apt-get install -y wget
run apt-get install -y vim
run apt-get install -y strace
run apt-get install -y diffstat
run apt-get install -y pkg-config
run apt-get install -y cmake
run apt-get install -y build-essential
run apt-get install -y tcpdump
run apt-get install -y screen
run apt-get install -y emacs
run apt-get install -y openjdk-7-jdk
run apt-get install -y maven

run apt-get install -y python-dev python-setuptools gcc
run easy_install SQLAlchemy

run apt-get install -y gnuplot
run apt-get install -y python-matplotlib

run wget https://bootstrap.pypa.io/get-pip.py
run python get-pip.py
run pip install pymysql
run pip install networkx

# Setup home environment
run useradd -s /bin/bash dev
run mkdir /home/dev && chown -R dev: /home/dev

# Create a shared data volume
# We need to create an empty file, otherwise the volume will
# belong to root.
# This is probably a Docker bug.
run mkdir /var/shared/
run touch /var/shared/placeholder
run chown -R dev:dev /var/shared
volume /var/shared

workdir /home/dev
env HOME /home/dev
add vimrc /home/dev/.vimrc
add vim /home/dev/.vim
add bash_profile /home/dev/.bash_profile

# Link in shared parts of the home directory
run ln -s /var/shared/.ssh
run ln -s /var/shared/.bash_history
run ln -s /var/shared/.gitconfig

run chown -R dev: /home/dev
run chown -R dev: /home/dev/.vim

# add two more shared volumes
run mkdir /input \
&& touch /input/placeholder \
&& chown -R dev:dev /input \
&& mkdir /output \
&& touch /output/placeholder \
&& chown -R dev:dev /output
volume ["/input","/output"]

# run as root to allow docker build etc.
#user dev
