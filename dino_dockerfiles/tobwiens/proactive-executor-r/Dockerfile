# Run on top of java 7
FROM dockerfile/java:openjdk-7-jdk
MAINTAINER Tobias Wiens <tobwiens@gmail.com>

# Install R
RUN ["/bin/bash", "-c", "apt-get update && \
apt-get install r-base \
-y"]

#RUN ["/bin/bash", "-c", "R CMD javareconf"]

RUN ["/bin/bash", "-c", "apt-get install r-cran-rjava -y"]

RUN ["/bin/bash", "-c", "apt-get build-dep r-cran-rgl -y"]

# Install mysql dev and mesa commond dev (GL/glu.h) for R packages
RUN ["/bin/bash", "-c", "apt-get install libmysqlclient-dev xvfb r-cran-rgl -y"]

# Install packages needed for proactive-tutorial
RUN ["/bin/bash", "-c", "echo \"install.packages(c('rJava','gtools', 'codetools', 'stringr'), repos='http://cran.univ-paris1.fr/',lib='/usr/local/lib/R/site-library', dependencies=TRUE) \" | R --no-save"] 


# Install all packages important for executing the task
ENV R_HOME /usr/lib/R
WORKDIR /data/context

#Add Multi-Node support - add mpirun
RUN ["/bin/bash", "-c", "apt-get install openmpi-bin -y"]
  
