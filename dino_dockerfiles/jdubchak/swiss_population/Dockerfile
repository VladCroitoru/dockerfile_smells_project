# Docker file for swiss_population 
# Jordan Dubchak, Dec 2017

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# then install all packages used in project
RUN Rscript -e "install.packages('ezknitr', repos = 'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"
RUN Rscript -e "install.packages('tidyverse', repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages('ggswissmaps', repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages('packrat', repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "install.packages('ggplot2', repos = 'http://cran.us.r-project.org')"

# install python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# get python package dependencies
RUN apt-get install -y python3-tk

# install numpy
RUN pip3 install numpy

