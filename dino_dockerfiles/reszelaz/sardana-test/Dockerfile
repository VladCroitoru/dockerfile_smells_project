FROM debian:stretch

RUN apt-get update

# install and configure supervisor
RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

# change installation dialogs policy to noninteractive
# otherwise debconf raises errors: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive

# change policy for starting services while installing
# otherwise policy-rc.d denies execution of start
# http://askubuntu.com/questions/365911/why-the-services-do-not-start-at-installation
# finally the approach is to not start services when building image
# the database will be fead from file, instead of creating tables
# RUN echo "exit 0" > /usr/sbin/policy-rc.d

# install some utilities
RUN apt-get install -y python3-pip \
                       git \
                       procps \
                       vim

# install mysql server
RUN apt-get install -y default-mysql-server
# workarounds for problems with starting mysqld
RUN sed -i 's/\/var\/run\/mysqld\/mysqld.pid/\/tmp\/mysqld.pid/g' /etc/mysql/mariadb.conf.d/50-server.cnf
RUN sed -i 's/\/var\/run\/mysqld\/mysqld.sock/\/tmp\/mysqld.sock/g' /etc/mysql/mariadb.conf.d/50-server.cnf
RUN mkdir /var/run/mysqld
RUN ln -s /tmp/mysqld.sock /var/run/mysqld/mysqld.sock
RUN ln -s /tmp/mysqld.pid /var/run/mysqld/mysqld.pid

#install tango-db
RUN apt-get install -y tango-db
# install libtango 9.3.4 with patch packaged at ALBA (includes fix for PyTango#315)
COPY liblog4tango5v5_9.3.4+dfsg1-2~bpo9+1+salsaci_amd64.deb /tmp/
COPY libtango9_9.3.4+dfsg1-2~bpo9+1+salsaci_amd64.deb /tmp/
RUN dpkg -i /tmp/liblog4tango5v5_9.3.4+dfsg1-2~bpo9+1+salsaci_amd64.deb
RUN dpkg -i /tmp/libtango9_9.3.4+dfsg1-2~bpo9+1+salsaci_amd64.deb

# install pyqt4 dummy package to avoid dependency problem with python3-qwt
ADD python3-pyqt4-dummy_1.0_all.deb /
RUN dpkg -i /python3-pyqt4-dummy_1.0_all.deb

# define preferred Qt for qtchooser
ENV QT_SELECT 5

# install taurus dependencies
RUN apt-get install -y python3-numpy \
                       python3-pyqt5 \
                       python3-pyqt5.qtopengl \
                       python3-guiqwt \
                       python3-gdbm \
                       python3-h5py \
                       python3-lxml \
                       python3-pint \
                       python3-future \
                       python3-ply \
                       python3-pytango \
                       python3-spyderlib \
                       python3-pymca5 \
                       qt4-designer \            
                       graphviz \
                       texlive \
                       texlive-latex-extra \
                       dvipng

# install PyTango 9.3.3 with patch packaged at ALBA (includes fix for PyTango#315)
RUN apt-get remove -y python3-pytango
ADD python3-tango_9.3.3-patch1-1~bpo9+1+salsaci_amd64.deb /
RUN dpkg -i /python3-tango_9.3.3-patch1-1~bpo9+1+salsaci_amd64.deb

# install sardana dependencies
RUN apt-get install -y python3-qtconsole \
                       python3-itango \
                       python3-matplotlib

# install pyqtgraph packaged at ALBA
RUN apt-get install -y python3-pyqtgraph \
                       python3-pyqt5 \
                       pyqt5-dev-tools \
                       qtbase5-dev-tools
RUN apt-get remove -y python3-pyqtgraph
ADD python3-pyqtgraph_0.11.0+8.e3948c-1~bpo9+1+salsaci_all.deb /
RUN dpkg -i /python3-pyqtgraph_0.11.0+8.e3948c-1~bpo9+1+salsaci_all.deb

RUN pip3 install -U pip
# install taurus 4.9.0.dev0
RUN pip3 install git+https://gitlab.com/taurus-org/taurus.git@824dd60ed
RUN pip3 install taurus_pyqtgraph

# install sphinx from PyPI to avoid problems with intersphinx mappings to PyTango
RUN pip3 install --upgrade sphinx sphinx_rtd_theme

# install sphinx napoleon extension to enable Google Style or Numpy Style docstrings
RUN pip3 install sphinxcontrib-napoleon

# installed latest version of pytest to run sardana tests
RUN pip3 install --upgrade pytest

# Change locale from POSIX to C.UTF-8 due to taurus-org/taurus#836
ENV LANG C.UTF-8

# add USER ENV (necessary for spyderlib in taurus.qt.qtgui.editor)
ENV USER=root

# configure supervisord
COPY supervisord.conf /etc/supervisor/conf.d/

# add macroserver environment with:
# _SAR_DEMO = <sar_demo execution results>
# JsonRecorder = True
# ScanDir = /tmp
# ScanFile = test.h5, test.dat
# ActiveMntGrp = mntgrp01
RUN mkdir -p /tmp/tango/MacroServer/demo1
COPY macroserver.properties* /tmp/tango/MacroServer/demo1/

# copy & untar mysql tango database (with sardemo) and change owner to mysql user
ADD tangodbsardemo.tar /var/lib/mysql/
RUN chown -R mysql /var/lib/mysql/tango

ENV TANGO_HOST=sardana-test:10000

# instal virtual monitor
RUN apt-get install -y xvfb

# configure virtual monitor env variable
ENV DISPLAY=:1.0

# start supervisor as deamon
CMD /usr/bin/supervisord -n
