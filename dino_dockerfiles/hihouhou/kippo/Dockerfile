#
# kippo Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

# Update & install packages for installing kippo 
RUN apt-get update && \
    apt-get install -y python-dev openssl python-openssl python-pyasn1 python-twisted subversion authbind

#ADD files 
ADD sshd_config /etc/ssh/
WORKDIR /home/kippo/kippo/

#ADD kippo user
RUN useradd -d /home/kippo -s /bin/bash -m kippo -g sudo

#configure authbind
RUN touch /etc/authbind/byport/22 && \
    chown kippo /etc/authbind/byport/22 && \
    chmod 777 /etc/authbind/byport/22

#configure kippo
RUN svn checkout http://kippo.googlecode.com/svn/trunk/ /home/kippo/kippo && \
    chmod -R 777 /home/kippo
ADD kippo.cfg /home/kippo/kippo/

EXPOSE 22
USER kippo

CMD ["authbind", "--deep", "twistd", "-y", "kippo.tac", "-n"]
