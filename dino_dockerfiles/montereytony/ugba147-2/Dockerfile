#
#
# Build: docker build --rm --tag ds-test .
# Push: docker tag my_image $DOCKER_ID_USER/my_image
#
# git status
# git commit -m "comments Ubuntu and R to 3.4.2 "
# git push
#

FROM jupyter/datascience-notebook:latest
USER root
ENV DEBIAN_FRONTEND noninteractive
# Install.
#RUN \
#  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
#  apt-get update && \
#  apt-get -y upgrade && \
#  apt-get install -y build-essential  && \
# apt-get install -y software-properties-common && \
# apt-get install -y apt-utils && \
#  apt-get install -y byobu curl git htop man unzip vim wget && \
#  rm -rf /var/lib/apt/lists/*

# Let's do updates first and install some needed libraries and utilites
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get update -y  && apt-get dist-upgrade -y
RUN apt -y install build-essential libssl-dev libffi-dev python-dev  lib32ncurses5-dev zip  unzip 
# gtar was used by pandoc so we need this
RUN ln -s /bin/tar /bin/gtar
RUN apt-get remove r-base-core -y && apt-get install r-base-core -y
RUN /usr/bin/wget https://github.com/jgm/pandoc/releases/download/2.1/pandoc-2.1-1-amd64.deb \
    &&  /usr/bin/dpkg -i pandoc-2.1-1-amd64.deb \
    && rm pandoc-2.1-1-amd64.deb

#
# Upgrade R 3.4.2 now
#
#RUN pip uninstall ipykernel
#RUN pip install ipykernel
#RUN conda clean -tipsy
RUN conda update -n base conda
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/pbdZMQ_0.3-3.tar.gz',repos=NULL,dependencies = TRUE)"
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
        r-aer  \
        r-png \
        r-rJava \
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
        r-rcpp \
        r-repr \
        r-stringi\
        r-stringr\
        r-processx\
        r-tidyverse\
        r-readr 

RUN conda install -c r r-igraph 

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

RUN conda install -c https://conda.anaconda.org/amueller wordcloud

# The following would not do a conda install so we compile from source
RUN Rscript -e "install.packages('https://ftp.osuosl.org/pub/cran/src/contrib/wordcloud2_0.2.1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/webshot_0.5.1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mclust_5.4.2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/pracma_2.2.2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/ggdendro_0.1-20.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/reshape_0.8.7.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/prettyunits_1.0.2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/progress_1.2.0.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/reshape_0.8.8.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/GGally_1.4.0.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/multiwayvcov_1.2.3.tar.gz',repos=NULL,dependencies = TRUE)"


#
# NB extensions is not working when running it in jupyterhub kubernetes so adding this next line
#
RUN conda install -c conda-forge jupyter_contrib_nbextensions
RUN jupyter nbextension install --py widgetsnbextension --sys-prefix
RUN jupyter nbextension enable  --py widgetsnbextension --sys-prefix

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/openxlsx_4.1.0.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/rio_0.5.16.tar.gz',repos=NULL,dependencies = TRUE)"

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/survey_3.35-1.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/coda_0.19-2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mvtnorm_1.0-8.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/sfsmisc_1.1-3.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/polycor_0.7-9.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/CDM_7.1-20.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/TAM_3.0-21.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mitools_2.3.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mitml_0.3-7.tar.gz',repos=NULL,dependencies = TRUE)"

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/mice_3.3.0.tar.gz',repos=NULL,dependencies = TRUE)"

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/GPArotation_2014.11-1.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/permute_0.9-4.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/vegan_2.5-3.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/pbivnorm_0.6.0.tar.gz',repo=NULL)"

RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/numDeriv_2016.8-1.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/Archive/mirt/mirt_1.20.1.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/lavaan_0.6-3.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/lavaan.survey_1.1.3.1.tar.gz',repo=NULL)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/sirt_3.1-80.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/miceadds_3.0-16.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/RcppRoll_0.2.2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/DEoptimR_1.0-8.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/robustbase_0.93-3.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/gower_0.1.2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/kernlab_0.9-27.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/CVST_0.2-2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/DRR_0.0.3.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.rstudio.com/src/contrib/SQUAREM_2017.10-1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/lava_1.6.1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/prodlim_2018.04.18.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/ddalpha_1.3.3.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/dimRed_0.1.0.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/ipred_0.9-6.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/recipes_0.1.2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/withr_2.1.2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/caret_6.0-79.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/neuralnet_1.33.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/irlba_2.3.2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/kknn_1.3.1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/gtools_3.8.1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/gdata_2.18.0.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/caTools_1.17.1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/gplots_3.0.1.1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/ROCR_1.0-7.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/MLmetrics_1.1.1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/dummies_1.5.6.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/slam_0.1-44.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/NLP_0.2-0.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/tm_0.7-6.tar.gz',repos=NULL,dependencies = TRUE)"

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get clean \
    apt autoremove
#####Important########
##To set Oracle JDK8 as default, install the "oracle-java8-set-default" package.
##E.g.: sudo apt install oracle-java8-set-default
##On Ubuntu systems, oracle-java8-set-default is most probably installed
##automatically with this package.
######################

#RUN  apt install oracle-java8-set-default
#RUN export LD_LIBRARY_PATH=/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server
#RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/rJava_0.9-9.tar.gz',repos=NULL,dependencies = TRUE)"


RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/clipr_0.5.0.tar.gz',repos=NULL,dependencies = TRUE)"
RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$JAVA_LD_LIBRARY_PATH
RUN R CMD javareconf
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/RWekajars_3.9.3-1.tar.gz',repos=NULL,dependencies = TRUE)"
#RUN conda install -c glaxosmithkline r-rwekajars 

#RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/RWekajars_3.9.2-1.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/RWeka_0.4-39.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/rpart.plot_2.1.2.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/gbm_2.1.5.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/zipcode_1.0.tar.gz',repos=NULL,dependencies = TRUE)"
RUN Rscript -e "install.packages('https://cran.r-project.org/src/contrib/caret_6.0-81.tar.gz',repos=NULL,dependencies = TRUE)"
#
# This should allow users to turn off extension if they do not want them.
#
USER jovyan

