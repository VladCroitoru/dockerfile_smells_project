#
#
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
# Upgrade R 3.4.2 now
#

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
        r-stringr\
        r-processx\
    r-tidyverse\
    r-readr


RUN conda install \
        ipython \
    numpy \
    pandas \
    plotnine \
    matplotlib \
    seaborn \
    phantomjs  \
    statsmodels \
    statsmodels \
    python-utils


RUN conda install -c https://conda.anaconda.org/amueller wordcloud

# The following would not do a conda install so we compile from source
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/DRR_0.0.3.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://ftp.osuosl.org/pub/cran/src/contrib/wordcloud2_0.2.1.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/webshot_0.5.0.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mclust_5.4.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/pracma_2.1.4.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/ggdendro_0.1-20.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/reshape_0.8.7.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/prettyunits_1.0.2.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/progress_1.1.2.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/GGally_1.3.2.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/multiwayvcov_1.2.3.tar.gz',repos=NULL)"


#
# NB extensions is not working when running it in jupyterhub kubernetes so adding this next line
#
RUN conda install -c conda-forge jupyter_contrib_nbextensions
RUN jupyter nbextension install --py widgetsnbextension --sys-prefix
RUN jupyter nbextension enable  --py widgetsnbextension --sys-prefix

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/openxlsx_4.0.17.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/rio_0.5.5.tar.gz',repos=NULL)"

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/survey_3.33.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/coda_0.19-1.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mvtnorm_1.0-7.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/sfsmisc_1.1-1.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/polycor_0.7-9.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/CDM_6.0-101.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/TAM_2.8-21.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mitools_2.3.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mice_2.46.0.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mvtnorm_1.0-7.tar.gz',repos=NULL)"



#
# This should allow users to turn off extension if they do not want them.
#
USER jovyan
RUN pip install scikit-neuralnetwork
RUN jupyter nbextensions_configurator enable


RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/GPArotation_2014.11-1.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/permute_0.9-4.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/vegan_2.4-6.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/pbivnorm_0.6.0.tar.gz',repo=NULL)"
#
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/numDeriv_2016.8-1.tar.gz',repo=NULL)"
#RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mirt_1.26.3.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/Archive/mirt/mirt_1.20.1.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/lavaan_0.5-23.1097.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/lavaan.survey_1.1.3.1.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/sirt_2.4-20.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/miceadds_2.9-15.tar.gz',repos=NULL)"
RUN Rscript -e "install.packages('http://download.nust.na/pub3/cran/src/contrib/neuralnet_1.33.tar.gz',repos=NULL)"
