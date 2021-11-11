# Docker file for income-prediction
# Avinash Prabhakaran, Dec, 2017

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# then install the ezknitr packages
#RUN Rscript -e "install.packages('ezknitr', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"
RUN Rscript -e "install.packages('optparse', repos = 'http://cran.us.r-project.org')"

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