FROM debian:stretch

# Update the repo info
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

# install mysql server
RUN apt-get install -y default-mysql-server

#install tango-db
RUN apt-get install -y tango-db

#install tango-test DS
RUN apt-get install -y tango-test

# install taurus dependencies
RUN apt-get install -y python-numpy \
                       python-enum34 \
                       python-guiqwt \
                       python-h5py \
                       python-lxml \
                       python-pint \
                       python-ply \
                       python-pytango \
                       python-qt4 \
                       python-qwt5-qt4 \
                       python-spyderlib \
                       python-pymca5 \
                       qt4-designer \
                       python-sphinx-rtd-theme \
                       graphviz \
                       python-pyqtgraph \
                       python-click \
                       python-pytest

# install some utilities
RUN apt-get install -y git \
                       python-pip \
                       vim \
                       ipython \
                       procps

# instal virtual monitor
RUN apt-get install -y xvfb

# configure virtual monitor env variable
ENV DISPLAY=:1.0

# configure supervisord
COPY supervisord.conf /etc/supervisor/conf.d/

# copy & untar mysql tango database and change owner to mysql user
ADD tangodb-tiny.tar /var/lib/mysql/
RUN chown -R mysql /var/lib/mysql/tango

# define tango host env var
ENV TANGO_HOST=taurus-test:10000

# add EPICS repo 
COPY epicsdebs /epicsdebs
COPY epics.list /etc/apt/sources.list.d/
RUN apt-get update

# install epics
RUN apt-get install -y epics-dev

# install pyepics
RUN pip install pyepics

# copy test epics IOC database
ADD testioc.db /

# add USER ENV (necessary for spyderlib in taurus.qt.qtgui.editor)
ENV USER=root

# WORKAROUND for https://github.com/taurus-org/taurus/issues/836
# It can be removed if python-h5py package is updated to >=2.8
ENV LANG=C.UTF-8

# start supervisor as deamon
CMD ["/usr/bin/supervisord"]
