# Dockerfile for epstudy
# GZ, Dec. 16, 2017

# Use rocker/tidyverse as the base image
FROM rocker/tidyverse

# get OS updates and install build tools
RUN apt-get update
RUN apt-get install -y build-essential

# install graphviz
RUN apt-get install -y graphviz

# install git
RUN apt-get install -y wget
RUN apt-get install -y make git

# clone, build makefile2graph,
# then copy key makefile2graph files to usr/bin so they will be in $PATH
RUN git clone https://github.com/lindenb/makefile2graph.git

RUN make -C makefile2graph/.

RUN cp makefile2graph/makefile2graph usr/bin
RUN cp makefile2graph/make2graph usr/bin

# Install packrat to manage dependencies
RUN Rscript -e "if (!('packrat' %in% installed.packages())) \
    install.packages('packrat', repos = 'http://cran.us.r-project.org')"

# Install ezknitr for rendering rmarkdown
RUN Rscript -e "if (!('ezknitr' %in% installed.packages())) \
    install.packages('ezknitr', repos = 'http://cran.us.r-project.org')"

# If you need to use the h2o package, install Java runtime env
# RUN apt-get update && \
#     apt-get install default-jre
# If you also need to build or run h2o tests, install jdk
# RUN apt-get install default-jdk

# Add packrat folder to /home/epstudy for env restore.
# Note the packrat env is not optimized. Redundant libraries
# are not removed so it might take some time to build the image. 
# Modify the packrat.lock file to remove those
# you do not need to speed up the build.
RUN mkdir /home/epstudy
ADD .Rprofile /home/epstudy
ADD packrat /home/epstudy/packrat
WORKDIR /home/epstudy

# Setup env in docker run (to reduce auto build time). 
# If the env is not set up previously, it will create 
# a new env and install all the libraries listed in packrat.lock
CMD ["Rscript", "-e", "packrat::restore()"]