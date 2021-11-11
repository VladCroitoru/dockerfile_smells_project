###############################################################################
# Website Development Toolbox for Responsive Website Development and          #
# Design Specialization                                                       #
#                                                                             #
# Build a Docker image for the Responsive Website Development and Design      #
# Specialization                                                              #
# University of London                                                        #
#                                                                             #
# Version 0.1, Copyright (C) 2015 Gregory D. Horne                            #
#                                 (horne at member dot fsf dot org)           #
#                                                                             #
# Licensed under the terms of the GNU General Public license (GPL) v2         #
###############################################################################

# ./container.sh create web-toolbox web-development-toolbox /home/horne/Projects/devops

FROM	ubuntu:14.04

MAINTAINER	"Gregory D. Horne" horne@member.fsf.org

ENV     DEBIAN_FRONTEND noninteractive

RUN		apt-get update


# Configure the regional language settings

ENV     LOCALE en_US.UTF-8

RUN		dpkg-reconfigure locales \
		&& locale-gen ${LOCALE} \
		&& /usr/sbin/update-locale LANG=${LOCALE}


# Create default user account 

ENV     WDT_USER webdev
ENV     HOME /home/${WDT_USER}

RUN		useradd --create-home --shell /bin/bash ${WDT_USER} \
		&& echo "${WDT_USER}:website" | chpasswd \
		&& mkdir ${HOME}/bin \
		&& mkdir ${HOME}/data \
		&& mkdir ${HOME}/tmp \
		&& mkdir ${HOME}/www


# miscellaneous packages

RUN     apt-get install --yes --no-install-recommends \
        libssl-dev \
        libcurl4-gnutls-dev \
		curl \
        wget \
        ca-certificates \
		zip \
		unzip \
		cmake


# Git command line client

RUN		apt-get install --yes git git-doc \
		&& git config --system push.default simple


# JavaScript Shell

RUN     wget --quiet --output-document=${HOME}/tmp/jsshell-linux-x86_64.zip \
			http://ftp.mozilla.org/pub/firefox/nightly/latest-oak/jsshell-linux-x86_64.zip \
		&& mkdir ${HOME}/bin/javascript-shell \
		&& unzip ${HOME}/tmp/jsshell-linux-x86_64.zip -d ${HOME}/bin/javascript-shell \
		&& ln -s ${HOME}/bin/javascript-shell/js ${HOME}/bin/js \
		&& rm ${HOME}/tmp/jsshell-linux-x86_64.zip \
		&& echo ${HOME}/bin/javascript-shell >> /etc/ld.so.conf


# Bootstrap CSS, JQuery Libraries, and HandlebarsJS

RUN		wget --quiet --output-document=${HOME}/tmp/bootstrap-3.3.6.zip \
				https://github.com/twbs/bootstrap/releases/download/v3.3.6/bootstrap-3.3.6-dist.zip \
		&& unzip ${HOME}/tmp/bootstrap-3.3.6.zip -d ${HOME}/tmp \
		&& cp -r ${HOME}/tmp/bootstrap-3.3.6-dist/css ${HOME}/www \
		&& cp -r ${HOME}/tmp/bootstrap-3.3.6-dist/fonts ${HOME}/www \
		&& cp -r ${HOME}/tmp/bootstrap-3.3.6-dist/js ${HOME}/www \
		&& mv ${HOME}/www/css/bootstrap.css ${HOME}/www/css/bootstrap-3.3.6.css \
		&& mv ${HOME}/www/css/bootstrap.min.css ${HOME}/www/css/bootstrap-3.3.6.min.css \
		&& mv ${HOME}/www/css/bootstrap-theme.css ${HOME}/www/css/bootstrap-theme-3.3.6.css \
		&& mv ${HOME}/www/css/bootstrap-theme.min.css ${HOME}/www/css/bootstrap-theme-3.3.6.min.css \
		&& mv ${HOME}/www/js/bootstrap.js ${HOME}/www/js/bootstrap-3.3.6.js \
		&& mv ${HOME}/www/js/bootstrap.min.js ${HOME}/www/js/bootstrap-3.3.6.min.js \
		&& rm ${HOME}/www/css/*.map \
		&& rm -r ${HOME}/tmp/* \
		&& wget --quiet --output-document=${HOME}/www/js/jquery-2.1.4.min.js http://code.jquery.com/jquery-2.1.4.min.js \
		&& wget --quiet --output-document=${HOME}/www/js/jquery-2.1.4.js http://code.jquery.com/jquery-2.1.4.js \
		&& wget --quiet --output-document=${HOME}/www/js/handlebars-4.0.5.js http://builds.handlebarsjs.com.s3.amazonaws.com/handlebars.runtime-v4.0.5.js


# lighttpd

RUN		apt-get install --yes lighttpd \
		&& sed -i 's/\/var\/www/\/home\/webdev\/www/' /etc/lighttpd/lighttpd.conf	


# MeteorJS JavaScript Application Platform

RUN		curl --silent https://install.meteor.com/ | sh


# WeTTY

RUN		apt-get install --yes nodejs-legacy npm \
		&& cd /tmp \
		&& git clone https://github.com/krishnasrinivas/wetty \
		&& cd wetty \
		&& npm install \
		&& mkdir /opt/wetty \
		&& cp app.js /opt/wetty/app.js \
		&& cp bin/wetty.js /opt/wetty/wetty.js \
		&& sed -i 's/\.\.\/app/\/opt\/wetty\/app\.js/' /opt/wetty/wetty.js \
		&& chmod +x /opt/wetty/wetty.js \
		&& cp -r node_modules /opt/wetty \
		&& cp -r public /opt/wetty \
		&& ln -s /opt/wetty/wetty.js /usr/local/bin/wetty.js \
		&& rm -r /tmp/wetty

ADD		index.html ${HOME}/www/index.html


 # Console/terminal managememnt, text editor and text editor plug-in manager

RUN     apt-get install --yes screen vim \
        && echo "alias vi=vim" >> ${HOME}/.bashrc \
		&& apt-get install --yes python-dev \
        && curl -fLo ${HOME}/.vim/autoload/plug.vim --create-dirs \
			https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

ADD     vimrc ${HOME}/.vimrc



# Supervisor deamon

RUN     apt-get install --yes supervisor

COPY    supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN     mkdir -p /var/log/supervisor \
		&& chgrp staff /var/log/supervisor \
		&& chmod g+w /var/log/supervisor \
		&& chgrp staff /etc/supervisor/conf.d/supervisord.conf


RUN		chown -R ${WDT_USER}:${WDT_USER} ${HOME}


# Clean-up installation environment

RUN     apt-get clean && apt-get autoclean


VOLUME  ${HOME}
WORKDIR ${HOME}


# Make TCP/IP ports accessible outside the container.
#
# Port		Application
# 80		lighttpd
# 3000		MeteorJS
# 8000		WeTTY

EXPOSE	80 3000 8000


# Manages processes within the container

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

