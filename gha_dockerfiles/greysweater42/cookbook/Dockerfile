FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y git
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN apt-get install software-properties-common -y
RUN add-apt-repository -y "ppa:marutter/rrutter3.5"
RUN apt-get update

RUN apt-get install libssl-dev -y
RUN apt-get install libcurl4-openssl-dev -y
RUN apt-get install libxml2-dev -y
RUN apt-get install liblapack-dev -y
RUN apt-get install gfortran -y
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip

RUN apt-get install pandoc=2.5-3build2 -y
RUN apt-get install r-base-core=3.6.3-2 -y

RUN Rscript -e 'install.packages("remotes")'
COPY dependencies/installer.R /dependencies/installer.R
COPY dependencies/requirements.R.txt /dependencies/requirements.R.txt
WORKDIR /dependencies
RUN Rscript installer.R

RUN Rscript -e 'devtools::install_github("greysweater42/decisionTree")'
RUN Rscript -e 'devtools::install_github("vqv/ggbiplot")'
# RUN Rscript -e "blogdown::install_hugo(version = '0.52')"
RUN apt-get install hugo -y

COPY dependencies/requirements.python.txt /dependencies/requirements.python.txt
RUN pip3 install -r requirements.python.txt

