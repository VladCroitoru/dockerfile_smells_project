FROM debian:stable

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
RUN apt-get install -y mysql-server

#install tango-db
RUN apt-get install -y tango-db

#install tango-db
RUN apt-get install -y tango-test

# install sardana dependencies
RUN apt-get install -y python ipython python-h5py python-lxml python-numpy\ 
                       python-nxs python-ply python-pytango python-qt4\
                       python-qwt5-qt4 python-spyderlib

# instal virtual monitor
RUN apt-get install -y xvfb

# configure virtual monitor env variable
ENV DISPLAY=:1.0

# configure supervisord
COPY supervisord.conf /etc/supervisor/conf.d/

# TODO: use just basic database, not the one with sardemo
# copy & untar mysql tango database (with sardemo) and change owner to mysql user
ADD tangodbsardemo.tar /var/lib/mysql/
RUN chown -R mysql /var/lib/mysql/tango

# define tanago host env var
ENV TANGO_HOST=taurus-test:10000

# start supervisor as deamon
CMD ["/usr/bin/supervisord"]
