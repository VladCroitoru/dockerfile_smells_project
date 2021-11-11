# Docker file for wine_classification
# Nazli Ozum Kafaee, Dec 2017

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# install the ezknitr packages
RUN Rscript -e "install.packages('ezknitr', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"

# install python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# get python package dependencies
RUN apt-get install -y python3-tk

# install necessary python packages
RUN pip3 install numPy
RUN pip3 install pandas
RUN pip3 install scipy
RUN pip3 install scikit-learn
RUN pip3 install argparse
RUN pip3 install graphviz
RUN pip3 install matplotlib
