# Docker file to run pipeline and text analysis for predicting traffic to msn.com
# Avinash Prabhakaran, May, 2018

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# Installing other dependencies
RUN Rscript -e "install.packages(c('optparse', 'argparse', 'doParallel'), repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages(c('feather', 'moments', 'strip', 'jsonlite'), repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages(c('stringi', 'tidytext', 'tm','stm', 'stopwords', 'servr', 'LDAvis'), repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages(c('forecast', 'tseries', 'imputeTS', 'quantreg'), repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages(c('zoo', 'scales', 'cowplot'), repos = 'http://cran.us.r-project.org')"

# install python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# get python package dependencies
RUN apt-get install -y python3-tk

# install numpy, pandas and scikit-learn
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install scipy
RUN pip3 install scikit-learn
RUN pip3 install pillow
RUN pip3 install h5py
RUN pip3 install tensorflow
RUN pip3 install keras
RUN pip3 install imbalanced-learn
