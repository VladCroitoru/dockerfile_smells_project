FROM ubuntu:14.04
MAINTAINER Guillaume Salva <guillaume@holbertonschool.com>

# Adding this repo so that we can install Shellcheck
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse' >> /etc/apt/sources.list

# Adding this repo for MySQL 5.7
RUN echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' >> /etc/apt/sources.list.d/mysql.list
RUN apt-get update

# curl/wget/git
RUN apt-get install -y curl wget git
# vim/emacs
RUN apt-get install -y vim emacs
# Shell
RUN apt-get install -y bc
RUN apt-get install -y shellcheck=0.3.3-1~ubuntu14.04.1
# C
RUN apt-get install -y build-essential gcc
RUN apt-get install -y valgrind
RUN apt-get install -y ltrace
RUN apt-get install -y libc6-dev-i386
RUN apt-get install -y libssl-dev

# Python
RUN apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
RUN cd /usr/src ; wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz ; tar xzf Python-3.4.3.tgz ; cd Python-3.4.3 ; ./configure ; make altinstall
# be sure it's 3.4 and not 3.5
RUN ! ls /usr/bin/python3.4 && ls /usr/src/Python-3.4.3/python && cp /usr/src/Python-3.4.3/python /usr/bin/python3.4 ; exit 0
# replace python version to have 3.4.4 as default
RUN rm -f /usr/bin/python
RUN rm -f /usr/bin/python3
RUN ln -s /usr/bin/python3.4 /usr/bin/python
RUN ln -s /usr/bin/python3.4 /usr/bin/python3
# Pip
RUN apt-get install -y python3-pip
RUN pip3 uninstall pep8 ; pip3 install pep8 ; pip3 install --upgrade pep8
# check if pep8 is correctly installed
RUN ! ls /usr/bin/pep8 && ls /usr/lib/python3.4/dist-packages/pep8.py && cp /usr/lib/python3.4/dist-packages/pep8.py /usr/bin/pep8 && chmod u+x /usr/bin/pep8 && sed -i '1 s/^.*$/#!\/usr\/bin\/python3/g' /usr/bin/pep8 ; exit 0

# Fabric 3
RUN apt-get install -y libffi-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y python3.4-dev
RUN apt-get install -y libpython3-dev
RUN pip3 install pyparsing
RUN pip3 install appdirs
RUN pip3 install setuptools==40.1.0
RUN pip3 install cryptography==2.8
RUN pip3 install Fabric3==1.14.post1


# SSH
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/^#PasswordAuthentication/PasswordAuthentication/' /etc/ssh/sshd_config
RUN sed -ri 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

ADD run.sh /tmp/run.sh
RUN chmod u+x /tmp/run.sh

# start run!
CMD ["./tmp/run.sh"]
