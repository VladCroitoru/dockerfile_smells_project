###############################################################################
# Machine Learning Toolbox for Machine Learning Specialization                #
#                                                                             #
# Manage containers for the Machine Learning Specialization                   #
# University of Washington                                                    #
#                                                                             #
# Version 0.1, Copyright (C) 2016 Gregory D. Horne                            #
#                                 (horne at member dot fsf dot org)           #
#                                                                             #
# Licensed under the terms of the GNU General Public license (GPL) v2         #
###############################################################################

# ./container.sh create machine-learning-toolbox machine-learning-toolbox /home/me/datascience

FROM	ubuntu:14.04

MAINTAINER	"Gregory D. Horne" horne@member.fsf.org

ENV     DEBIAN_FRONTEND noninteractive

RUN		apt-get update


# Configure the regional language settings

ENV     LOCALE en_CA.UTF-8

RUN		dpkg-reconfigure locales \
		&& locale-gen ${LOCALE} \
		&& /usr/sbin/update-locale LANG=${LOCALE}


# Create default user account 

ENV     MLT_USER mlt
ENV     HOME /home/${MLT_USER}

RUN		apt-get install --yes sudo \
		&& useradd --create-home --shell /bin/bash ${MLT_USER} \
		&& adduser ${MLT_USER} sudo \
		&& echo "${MLT_USER}:science" | chpasswd \
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

RUN     apt-get install --yes --no-install-recommends \
        build-essential

RUN     apt-get install --yes --no-install-recommends \
        gfortran \
        python \
        python-dev \
        python-numpy \
        python-matplotlib \
        python-pip \
		&& mkdir ${HOME}/.python-eggs


# GraphLab Create

# libsodium 

RUN		apt-get install --yes --no-install-recommends \
        autoconf \
        automake

RUN		wget https://download.libsodium.org/libsodium/releases/libsodium-1.0.8.tar.gz --output-document=/tmp/libsodium-1.0.8.tar.gz \
		&& cd /tmp \
		&& tar -xzvf libsodium-1.0.8.tar.gz \
		&& cd libsodium-1.0.8 \
		&& ./configure \
		&& make && make check && make install \
		&& rm -rf /tmp/libsodium*

# zeromq

RUN		apt-get install --yes --no-install-recommends \
		libtool \
		pkg-config

RUN     wget http://download.zeromq.org/zeromq-4.1.4.tar.gz --output-document=/tmp/zeromq-4.1.4.tar.gz \
		&& cd /tmp \
        && tar -xzvf zeromq-4.1.4.tar.gz \
        && cd zeromq-4.1.4 \
        && ./configure \
        && make install \
        && ldconfig \
		&& rm -rf /tmp/zeromq*

ADD		graphlab.sh ${HOME}/bin/graphlab.sh

RUN		chmod a+x ${HOME}/bin/graphlab.sh


# Jupyter (formerly IPython Notebook)

RUN		pip install jupyter

RUN     cd ${HOME} \
        && jupyter notebook --generate-config \ 
        && sed -i "s/# c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '0.0.0.0'/"\
              ${HOME}/.jupyter/jupyter_notebook_config.py


# Console/terminal managememnt, text editor and text editor plug-in manager

RUN		apt-get install --yes screen vim \
		&& echo "alias vi=vim" >> ${HOME}/.bashrc \
		&& curl -fLo ${HOME}/.vim/autoload/plug.vim --create-dirs \
                https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim \
		&& mkdir ${HOME}/data

ADD		vimrc ${HOME}/.vimrc


# Python Markdown

RUN		pip install markdown2
RUN		pip install --upgrade Pweave
RUN		pip install --user pyreport	


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

ADD		supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN     mkdir -p /var/log/supervisor \
		&& chgrp staff /var/log/supervisor \
		&& chmod g+w /var/log/supervisor \
		&& chgrp staff /etc/supervisor/conf.d/supervisord.conf


RUN		chown -R ${MLT_USER}:${MLT_USER} ${HOME}


# Clean-up installation environment

RUN     apt-get clean && apt-get autoclean


VOLUME  ${HOME}
WORKDIR ${HOME}


# Make TCP/IP ports accessible outside the container.
#
# Port		Application
# 8000		WeTTY
# 8888		Jupyter

EXPOSE	8000 8888


# Manages processes within the container

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

