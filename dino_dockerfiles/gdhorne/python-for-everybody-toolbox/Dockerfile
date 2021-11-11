###############################################################################
# Python Toolbox for Python for Everybody Specialization                      #
#                                                                             #
# Manage containers for the Python for Everybody Specialization               #
# University of Michigan                                                      #
#                                                                             #
# Version 0.1, Copyright (C) 2016 Gregory D. Horne                            #
#                                 (horne at member dot fsf dot org)           #
#                                                                             #
# Licensed under the terms of the GNU General Public license (GPL) v2         #
###############################################################################

# ./container.sh create python-toolbox python-for-everyone-toolbox /home/me/devops

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

ENV     PE_USER pythonista
ENV     HOME /home/${PE_USER}

RUN		useradd --create-home --shell /bin/bash ${PE_USER} \
		&& echo "${PE_USER}:python" | chpasswd \
		&& mkdir ${HOME}/bin \
		&& mkdir ${HOME}/tmp


# miscellaneous packages

RUN     apt-get install --yes --no-install-recommends \
        libssl-dev \
        libcurl4-gnutls-dev \
		curl \
        wget \
        ca-certificates \
		zip \
		unzip


# Git command line client

RUN		apt-get install --yes git git-doc \
		&& git config --system push.default simple


# Python 2.7

RUN		apt-get install --yes --no-install-recommends \
		build-essential \
		python python-dev \
		python-beautifulsoup \
		python-pip


# sqlite

RUN		apt-get install --yes sqlite3

# sqlite database browser

ADD		sqlite_web.sh ${HOME}/bin/sqlite_web.sh

RUN     pip install sqlite-web \
		&& chmod a+x ${HOME}/bin/sqlite_web.sh \
		&& ln -sf ${HOME}/bin/sqlite_web.sh ${HOME}/bin/sqlite_web \
		&& chmod a+x ${HOME}/bin/sqlite_web


# Console/terminal managememnt, text editor and text editor plug-in manager

RUN		apt-get install --yes screen vim \
		&& echo "alias vi=vim" >> ${HOME}/.bashrc \
		&& curl -fLo ${HOME}/.vim/autoload/plug.vim --create-dirs \
                https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim \
		&& mkdir ${HOME}/data

ADD		vimrc ${HOME}/.vimrc


# Text editor (in addition to default vim)

RUN     apt-get install nano


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


# Supervisor deamon

RUN     apt-get install --yes supervisor

COPY    supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN     mkdir -p /var/log/supervisor \
		&& chgrp staff /var/log/supervisor \
		&& chmod g+w /var/log/supervisor \
		&& chgrp staff /etc/supervisor/conf.d/supervisord.conf


RUN		chown -R ${PE_USER}:${PE_USER} ${HOME}


# Clean-up installation environment

RUN     apt-get clean && apt-get autoclean


VOLUME  ${HOME}
WORKDIR ${HOME}


# Make TCP/IP ports accessible outside the container.
#
# Port		Application
# 8000		WeTTY
# 8080		sqlite-web

EXPOSE	8000 8080


# Manages processes within the container

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
