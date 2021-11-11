FROM kamekoopa/centos:7.0-systemd
MAINTAINER kamekoopa <hogehugo@gmail.com>

RUN yum install -y epel-release

#RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm
#RUN rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm

RUN yum install --enablerepo=epel -y \
  tar \
  wget \
  make \
  gcc \
  zlib-devel \
  bzip2-devel \
  openssl-devel \
  ncurses-devel \
  sqlite-devel \
  readline-devel \
  tk-devel \
  gdbm-devel \
  db4-devel \
  libpcap-devel \
  xz-devel \
  python-devel \
  libffi-devel \
  libyaml-devel \
  nginx


# install nginx
RUN systemctl enable nginx
EXPOSE 8080


# install pytnon
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tar.xz
RUN tar xvf Python-3.4.2.tar.xz
WORKDIR /tmp/Python-3.4.2
RUN ./configure --prefix=/usr/local
RUN make
RUN make altinstall


# install kvwatcher
RUN mkdir /root/kvwatcher
WORKDIR /root/kvwatcher

COPY requirements.txt /root/kvwatcher/requirements.txt
RUN pip3.4 install -r requirements.txt

COPY setup.py /root/kvwatcher/setup.py
COPY README.rst /root/kvwatcher/README.rst
COPY kvwatcher /root/kvwatcher/kvwatcher
COPY src /root/kvwatcher/src

RUN python3.4 setup.py install

COPY kvwatcher.service /usr/lib/systemd/system/kvwatcher.service
RUN systemctl enable kvwatcher


CMD ["/sbin/init"]
