FROM debian:stretch
MAINTAINER Naoaki Obiki
RUN apt-get update && apt-get install -y sudo git supervisor
ARG username="git"
RUN groupadd $username && useradd -g $username -d /home/$username $username && mkdir /home/$username
RUN apt-get update && apt-get install -y git-core
ADD settings/git-daemon/.gitconfig /home/$username
ADD settings/supervisor/conf.d/git-daemon.conf /git-daemon.conf.org
RUN chown -R $username:$username /home/$username
RUN echo "mkdir -p /repos/git && chown -R $username:$username /repos/git/" >> /git-daemon.sh && chmod +x /git-daemon.sh
COPY bootstrap.sh /
RUN chmod +x /bootstrap.sh
CMD ["/bootstrap.sh"]
