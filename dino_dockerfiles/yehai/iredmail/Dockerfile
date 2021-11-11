
FROM ubuntu-upstart:14.04

### Update and customize ubuntu packages.
RUN apt-get update ;\
    apt-get -y upgrade
RUN apt-get -y purge openssh-server openssh-client ;\
    apt-get -y autoremove
RUN apt-get -y install vim nano aptitude wget bzip2 bash-completion

### Download and unzip iRedMail.
ENV IREDMAIL iRedMail-0.9.0
RUN wget https://bitbucket.org/zhb/iredmail/downloads/$IREDMAIL.tar.bz2 ;\
    tar xvjf $IREDMAIL.tar.bz2 ;\
    rm $IREDMAIL.tar.bz2

# ### Install iRedMail.
# COPY config /$IREDMAIL/
# RUN chmod +x /$IREDMAIL/iRedMail.sh
# RUN echo y | /$IREDMAIL/iRedMail.sh

### Make some additional system configurations.
COPY . /tmp/config/
RUN /tmp/config/sysconfig.sh
RUN rm -rf /tmp/config/
