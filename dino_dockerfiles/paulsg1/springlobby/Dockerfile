FROM ubuntu:20.04

LABEL maintainer="PG"

# build Springlobby
RUN apt update && \
apt install -y git cmake build-essential libopenal-dev cmake libwxgtk3.0-gtk3-dev libcurl4-openssl-dev libalure-dev libboost-thread-dev libboost-filesystem-dev libboost-system-dev libpng-dev libssl-dev minizip  libglib2.0-bin libglib2.0-dev gettext libalure-dev libgettextpo-dev libminizip-dev doxygen libjsoncpp-dev libnotify-dev libboost-test-dev clang-format clang && \
git clone --depth 1 --branch 0.263 --recursive https://github.com/springlobby/springlobby.git && \
cd springlobby/ && \
cmake . && \
make && \
make install

# passwordless login
ADD id_rsa.pub /root/.ssh/authorized_keys

# install and configure SSH
RUN apt-get install -y openssh-server && \
 mkdir /var/run/sshd && \
 echo 'root:qaz123' | chpasswd && \
 sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
 sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# clean up
RUN apt-get clean && \
 rm /var/lib/apt/lists/*.*

# port
EXPOSE 22

# start SSH as daemon
CMD ["/usr/sbin/sshd", "-D"]
