FROM ubuntu:16.04

LABEL maintainer="PG"

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y apt-utils \
 less lsof psmisc \
 info man-db \
 vim nano \
 lynx links \
 command-not-found bash-completion mc htop
# p7zip-full sudo byobu net-tools inetutils-ping inetutils-traceroute mtr-tiny tcpdump colordiff

# add student accounts
RUN addgroup studenci && for i in `seq 1 20`; do adduser student_$i --gecos "student" --ingroup studenci --force-badname --disabled-password; echo "student_$i:wcy" | chpasswd; chage -d 0 student_$i; done

# special prompt
ADD .bash_aliases /etc/skel/
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

# port & volume
EXPOSE 22
VOLUME /home

# start SSH as daemon
CMD ["/usr/sbin/sshd", "-D"]