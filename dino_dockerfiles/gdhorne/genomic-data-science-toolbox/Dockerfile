###############################################################################
# Data Science Toolbox for Genomic Data Science Specialization                #
#                                                                             #
# Build a Docker image for the Genomic Data Science Specialization            #
# Johns Hopkins University                                                    #
#                                                                             #
# Version 0.1, Copyright (C) 2015 Gregory D. Horne                            #
#                                 (horne at member dot fsf dot org)           #
#                                                                             #
# Licensed under the terms of the GNU General Public license (GPL) v2         #
###############################################################################


# ./container.sh create genomics-data-toolbox gdhorne/genomics-data-science-toolbox /home/me/datascience

FROM	ubuntu:latest

MAINTAINER	"Gregory D. Horne" horne@member.fsf.org

ENV     ARCH amd64
ENV     BIOPYTHON_VERSION 1.66
ENV     RSTUDIO_VERSION 0.99.892

ENV     DEBIAN_FRONTEND noninteractive

RUN		apt-get update


# Configure the regional language settings

ENV     LOCALE en_US.UTF-8

RUN		dpkg-reconfigure locales \
		&& locale-gen ${LOCALE} \
		&& /usr/sbin/update-locale LANG=${LOCALE}


# Create default user account 

ENV     GDST_USER gdst
ENV     HOME /home/${GDST_USER}

RUN		useradd --create-home --shell /bin/bash ${GDST_USER} \
		&& echo "${GDST_USER}:science" | chpasswd \
		&& mkdir ${HOME}/bin \
		&& mkdir ${HOME}/tmp


# miscellaneous packages

RUN     apt-get install --yes --no-install-recommends \
        libssl-dev \
        libcurl4-gnutls-dev \
		curl \
        wget \
        ca-certificates \
		man

# X11

 RUN     apt-get install --yes xvfb xauth xfonts-base


# Git command line client

RUN		apt-get install --yes git git-doc \
		&& git config --system push.default simple

# Python 2.7 (required for Galaxy)

RUN     apt-get install -y --no-install-recommends \
		python \
		python-dev \
		python-pip


# Python 3

RUN		apt-get install --yes --no-install-recommends \
		build-essential \
		python3 python3-dev \
		gfortran \
		python3-numpy \
		python3-pip

# Jupyter (formerly IPython Notebook)

RUN     pip3 install jupyter \
		&& python2 -m pip install ipykernel \
		&& python2 -m ipykernel install --user


# BioPython

RUN     cd /tmp \
		&& wget -c -nv http://biopython.org/DIST/biopython-${BIOPYTHON_VERSION}.tar.gz \
        && tar -xzf biopython-${BIOPYTHON_VERSION}.tar.gz \
		&& cd biopython* \
        && python3 setup.py build \
        && python3 setup.py install \
        && cd / \
        && rm -rf /tmp/biopython-${BIOPYTHON_VERSION}.tar.gz /tmp/biopython*


# Galaxy

ENV     GALAXY_ACCOUNT galaxy
ENV     GALAXY_HOME /home/${GALAXY_ACCOUNT}

RUN     useradd --groups staff --create-home --shell /bin/bash ${GALAXY_ACCOUNT} \
        && echo "galaxy:science" | chpasswd

RUN     cd ${GALAXY_HOME} \
        && git clone https://github.com/galaxyproject/galaxy/ \
        && chown -R ${GALAXY_ACCOUNT}:${GALAXY_ACCOUNT} ./galaxy \
        && cd galaxy \
        && git checkout -b master origin/master \
        && sed -i 's/export GALAXY_CONFIG_FILE/export GALAXY_CONFIG_FILE\n    exit 0/' run.sh \
        && ./run.sh \
        && sed -i 's/exit 0/#exit 0/' run.sh \
        && cp config/galaxy.ini.sample config/galaxy.ini \
        && sed -i 's/#host = 127.0.0.1/host = 0.0.0.0/' config/galaxy.ini

RUN     sed -i 's/#admin_users = None/admin_users = gdst@domain.tld/' ${GALAXY_HOME}/galaxy/config/galaxy.ini


# Statistical Computing Evironment and Programming Language

RUN     echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" \
        >> /etc/apt/sources.list \
        && apt-key adv --keyserver keyserver.ubuntu.com --recv-key 51716619E084DAB9 \
        && apt-get update \
        && apt-get install --yes --force-yes --no-install-recommends \
        r-base r-base-dev r-doc-info r-recommended \
        libxml2-dev \
		poppler-utils \
        texlive texlive-xetex texlive-latex-extra lmodern \
        && mkdir -p /etc/R/ \
		&& echo "options(repos = list(CRAN = 'https://cran.rstudio.com/'), \
		download.file.method = 'libcurl')" /etc/R/Rprofile.site \
		&& sed -i 's/^R_LIBS_USER/#R_LIBS_USER/' /etc/R/Renviron \
		&& echo "R_LIBS_USER=~/R/packages" >> /etc/R/Renviron \
		&& echo "R_LIBS=~/R/packages" >> /etc/R/Renviron.site


# RStudio Server

RUN		apt-get install --yes psmisc libapparmor1 \
		&& wget -c -nv http://download2.rstudio.org/rstudio-server-${RSTUDIO_VERSION}-${ARCH}.deb \
		&& dpkg -i rstudio-server-${RSTUDIO_VERSION}-${ARCH}.deb \
		&& rm rstudio-server-${RSTUDIO_VERSION}-${ARCH}.deb

RUN		echo "r-libs-user=~/R/packages" >> /etc/rstudio/rsession.conf


# Pandoc

RUN     wget -c -nv https://github.com/jgm/pandoc/releases/download/1.16.0.2/pandoc-1.16.0.2-1-amd64.deb \
		&& dpkg -i pandoc-1.16.0.2-1-amd64.deb \
		&& rm pandoc-1.16.0.2-1-amd64.deb


# Jupyter notebook

RUN		cd ${HOME} \
		&& jupyter notebook --generate-config \ 
		&& sed -i "s/# c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '0.0.0.0'/"\
			  ${HOME}/.jupyter/jupyter_notebook_config.py


# Bioconductor Package for R

ADD     bioconductor_installation.r /tmp/bioconductor_installation.r
RUN     Rscript /tmp/bioconductor_installation.r \
		&& rm /tmp/bioconductor_installation.r


# Console/terminal managememnt, text editor and text editor plug-in manager

RUN		apt-get install --yes screen vim nano \
		&& echo "alias vi=vim" >> ${HOME}/.bashrc \
		&& curl -fLo ${HOME}/.vim/autoload/plug.vim --create-dirs \
                https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim \
		&& mkdir ${HOME}/data

ADD		vimrc ${HOME}/.vimrc


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


RUN		mkdir ${HOME}/.python-eggs

RUN		chown -R ${GDST_USER}:${GDST_USER} ${HOME}


# Clean-up installation environment

RUN     apt-get clean && apt-get autoclean


VOLUME  ${HOME}
WORKDIR ${HOME}


# Make TCP/IP ports accessible outside the container.
#
# Port		Application
# 8000		WeTTY
# 8080		Galaxy Server
# 8787		RStudio Server
# 8888		Jupyter

EXPOSE	8000 8080 8787 8888


# Manages processes within the container

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

