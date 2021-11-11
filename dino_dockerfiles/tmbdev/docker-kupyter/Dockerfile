FROM ubuntu:16.04
MAINTAINER Tom Breuel <tmbdev@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get -y update \
    && apt-get -y install sudo lsb-release build-essential curl software-properties-common \
    && echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c -s) main" \
           >> /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key  add - \
    && apt-get update -y && apt-get dist-upgrade -y && apt-get -y install apt-utils

RUN apt-get -y install locales && locale-gen en_US.UTF-8 && dpkg-reconfigure locales \
    && apt-get -y install python python2.7-dev libpython2.7-dev git \
        python-pip wget mercurial git python-dev python-cffi \
        libpng-dev libjpeg-dev libtiff5-dev \
    && pip install --upgrade pip && pip install --upgrade pkgconfig \
    && apt-get install -y google-cloud-sdk kubectl \
    && apt-get -y install openssh-server stunnel4 daemon libhdf5-dev \
        lsof iputils-ping socat netcat dnsutils aria2 net-tools \
        socat netrw netcat libxml2-dev libxslt-dev sshfs dropbear-bin \
        telnet-ssl sqlite3 silversearcher-ag \
    && apt-get -y install salt-master salt-minion salt-api salt-proxy salt-ssh salt-syndic

RUN apt-get -y install python-tk tightvncserver tmux rxvt \
    xterm mlterm imagemagick firefox blackbox imagemagick \
    vim-gtk gnome-terminal i3 chromium-browser

RUN pip install --upgrade setuptools pyzmq msgpack-python \
        simplejson lxml Pillow olefile redis python-redis-log rlog \
    && pip install --upgrade numpy scipy matplotlib scikit-learn scikit-image \
        sklearn-extras imread imageio imread tifffile \
    && pip install --upgrade ipython[all] jupyter h5py pandas reportlab \
        editdistance bokeh

RUN pip install --upgrade jupyterlab && jupyter serverextension enable --py jupyterlab --sys-prefix
RUN pip install --upgrade dask dask[complete] distributed
RUN pip install --upgrade google-cloud-storage
RUN pip install --upgrade youtube-dl

RUN pip install http://download.pytorch.org/whl/cpu/torch-0.3.1-cp27-cp27mu-linux_x86_64.whl 
RUN pip install torchvision
# RUN apt-get install -y netcat-openbsd
RUN apt-get install -y netcat-traditional
RUN apt-get install -y redis-tools
RUN apt-get install -y webfs
RUN apt-get install -y iperf3 iozone3

RUN pip install git+git://github.com/tmbdev/redrun
RUN pip install git+git://github.com/tmbdev/htpar
RUN pip install git+git://github.com/NVLabs/dlinputs
RUN pip install git+git://github.com/NVLabs/dltrainers
RUN pip install git+git://github.com/NVLabs/dlmodels
