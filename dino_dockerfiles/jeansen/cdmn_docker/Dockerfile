FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  locales \
  curl \
  xterm \
  console-setup \
  wget \
  unzip \
  apt-transport-https \
  dirmngr \
  fontconfig \
  man \
  sudo \
  xauth \
  x11-xserver-utils \
  rxvt-unicode-256color \
  perl \
  libfilesys-df-perl \
  libparams-validate-perl \
  libproc-processtable-perl \
  libxft-dev \
  libperl-dev \
  checkinstall \
  git \
  supervisor \
  stress-ng \
  vim \
  openssh-server && \
  apt-get remove -y rxvt-unicode-256color && \
  apt-get clean && \ 
  rm -rf /var/lib/apt/lists/* && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8

ADD http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-9.22.tar.bz2 /tmp/

RUN mkdir -p /tmp/rxvt_src && \
    wget -O - http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-9.22.tar.bz2 | tar -xjf - -C /tmp/rxvt_src

WORKDIR /tmp/rxvt_src/rxvt-unicode-9.22

RUN git clone https://github.com/Jeansen/cdmn.git && \
  patch src/rxvtperl.xs cdmn/resources/rxvtperl.xs.patch && \
  ./configure --enable-everything --enable-256-color && \
  make && checkinstall -y

RUN mkdir /var/run/sshd
RUN echo 'root:test' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22

WORKDIR /

COPY entrypoint.sh entrypoint.sh

CMD /entrypoint.sh
