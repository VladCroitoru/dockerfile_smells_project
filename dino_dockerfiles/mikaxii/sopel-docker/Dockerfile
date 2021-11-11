FROM python:3
MAINTAINER Mika <mika@recalbox.fr>

RUN apt-get update
RUN apt-get install gettext libenchant1c2a -y 

RUN useradd -m -d /home/sopel sopel
WORKDIR /home/sopel

RUN pip install backports.ssl_match_hostname
RUN pip install sopel

ENV IRC_NICK nickname
ENV IRC_HOST irc.freenode.net
#ENV use_ssl = false
ENV IRC_PORT 6667
ENV IRC_OWNER owner
ENV IRC_ADMINS someadmins
ENV IRC_CHANS "#chan"
#ENV auth_method = nickserv
ENV IRC_PASSWD super_pass
#ENV reply_errors = false
ENV SOPEL_EXTRA	/home/sopel/.sopel/modules
ENV ENABLE_MODULES some_modules


RUN mkdir -p /home/sopel/.sopel/modules
ADD modules/* /home/sopel/.sopel/modules/
ADD default.cfg.tpl /home/sopel/.sopel/default.cfg.tpl
ADD start.sh /usr/bin
RUN chown sopel:sopel /home/sopel -R

USER sopel
CMD start.sh
