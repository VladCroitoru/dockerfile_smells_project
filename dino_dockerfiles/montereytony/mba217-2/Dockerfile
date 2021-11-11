#
# to do a test build by hand (instead of the automated hub.docker.com build) you
# can do this:
#
#    docker build --rm --tag ds-test .
#
# git status
# git commit -m "comments Ubuntu and R to 3.4.2 "
# git push
#


FROM jupyter/datascience-notebook

USER root

ENV DEBIAN_FRONTEND noninteractive

# Let's do updates first and install some needed libraries and utilites
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get update -y  && apt-get dist-upgrade -y
RUN apt install build-essential libssl-dev libffi-dev python-dev  lib32ncurses5-dev -y
# gtar was used by pandoc so we need this
RUN ln -s /bin/tar /bin/gtar
RUN /usr/bin/apt-get install unzip
RUN /usr/bin/wget https://github.com/jgm/pandoc/releases/download/2.1/pandoc-2.1-1-amd64.deb
RUN /usr/bin/dpkg -i pandoc-2.1-1-amd64.deb
RUN rm pandoc-2.1-1-amd64.deb

#
# Upgrade R now
#

RUN conda update -n base conda
RUN conda update -c r r-base

RUN conda install \
	gcc_linux-64 \
	gfortran_linux-64 \
	r-essentials \
	r-htmlwidgets \
	r-gridExtra \
	r-e1071 \
	r-rgl \
	r-xlsxjars \
	r-xlsx \
	r-rJava \
	r-aer  \
	r-png \
	r-devtools \
	r-digest \
	r-evaluate \ 
	r-memoise  \
	r-withr  \
	r-irdisplay \
	r-r6  \
	r-irkernel \
	r-jsonlite\
	r-lubridate\
	r-magrittr\
	r-pbdzmq \
	r-rcpp \
	r-repr \
	r-stringi\
	r-stringr  \
	r-processx  \
    r-reshape \
    r-tidyverse \
    r-readr \
    r-mice  \
    r-progress 

RUN conda install \
	ipython \
    numpy \
    pandas \
    plotnine \
    matplotlib \
    seaborn \
    phantomjs  \
    statsmodels \
    python-utils 

    #mittner \
RUN conda install -c conda-forge csvkit=1.0.2 
RUN pip install scikit-neuralnetwork

RUN conda install -c https://conda.anaconda.org/amueller wordcloud

# The following would not do a conda install so we compile from source

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/kernlab_0.9-25.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/CVST_0.2-1.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/DRR_0.0.3.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://ftp.osuosl.org/pub/cran/src/contrib/wordcloud2_0.2.1.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/webshot_0.5.0.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mclust_5.4.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/pracma_2.1.1.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/ggdendro_0.1-20.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/GGally_1.3.2.tar.gz',repos=NULL)"
#RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/miceadds_2.9-15.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/multiwayvcov_1.2.3.tar.gz',repos=NULL)"



RUN pip install -e 'git://github.com/irskep/clubsandwich.git@master#egg=clubsandwich'

#
# NB extensions is not working when running it in jupyterhub kubernetes so adding this next line
#
RUN conda install -c conda-forge jupyter_contrib_nbextensions
RUN jupyter nbextension install --py widgetsnbextension --sys-prefix
RUN jupyter nbextension enable  --py widgetsnbextension --sys-prefix
#
# This should allow users to turn off extension if they do not want them.
#
USER jovyan
RUN jupyter nbextensions_configurator enable
