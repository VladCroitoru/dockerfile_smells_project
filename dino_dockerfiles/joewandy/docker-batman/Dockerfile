# Dockerfile to install rstudio-server + BATMAN + scientific python libraries for NMR spectral processing
# See:
# - https://github.com/wiseio/datascience-docker/tree/master/datascience-base
# - https://github.com/ContinuumIO/docker-images/blob/master/miniconda/Dockerfile
# - https://github.com/rocker-org/rocker/wiki/Using-the-RStudio-image

FROM ubuntu:16.04
MAINTAINER Joe Wandy <joe.wandy@glasgow.ac.uk>

ENV TERM xterm
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

############### install R-studio ###############

RUN apt-get -y update \
      && apt-get -y install curl wget r-base libapparmor1 libcurl4-openssl-dev libxml2-dev libssl-dev gdebi-core \
      && apt-get -y install ssh htop libopenmpi-dev \
      && apt-get -y install vim cowsay figlet \
      && apt-cache search r-cran | cut -f 1 -d ' ' | xargs apt-get -y install

# grab latest rstudio-server
RUN curl https://s3.amazonaws.com/rstudio-server/current.ver | \
        xargs -I {} wget http://download2.rstudio.org/rstudio-server-{}-amd64.deb -O rstudio.deb \
      && gdebi -n rstudio.deb \
      && rm rstudio.deb \
      && apt-get clean

# install batman & other R packages here
ADD installBatman.R /home/root/installBatman.R
RUN /usr/bin/Rscript /home/root/installBatman.R

# create rstudio user
RUN useradd -m -d /home/rstudio rstudio \
      && echo rstudio:rstudio | chpasswd

############### install minimal Anaconda Python ###############

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.1.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

ENV PATH /opt/conda/bin:$PATH
ADD requirements_conda.txt /home/root/requirements_conda.txt
ADD requirements_pip.txt /home/root/requirements_pip.txt
RUN conda install --yes --file /home/root/requirements_conda.txt
RUN pip install -r /home/root/requirements_pip.txt

# Get latest nmrglue library
RUN git clone https://github.com/jjhelmus/nmrglue.git /home/root/nmrglue && cd /home/root/nmrglue && python setup.py install

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes in jypyter notebook.
# see http://jupyter-notebook.readthedocs.io/en/latest/public_server.html
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

# expose port 8787 for rstudio-server, 9999 for jupyter notebook
EXPOSE 8787 9999

# The code, data and results are mapped here
VOLUME /home/rstudio/NMR
RUN git clone https://github.com/joewandy/pyBatman.git /home/rstudio/codes

# copy the scripts that we need to run the analysis
ADD run_analysis.sh /home/root/run_analysis.sh
RUN chmod a+x /home/root/run_analysis.sh
WORKDIR /home/rstudio
CMD ["/home/root/run_analysis.sh"]

# also copy the script to run Rstudio and Jupyter notebook in the background
ADD run_servers.sh /home/root/run_servers.sh
RUN chmod a+x /home/root/run_servers.sh