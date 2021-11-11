FROM ubuntu:16.04
MAINTAINER felix11h.dev@gmail.com

USER root

# installing the latest version of these basic packages 
# fixing versions through apt is possible, however previous
# versions are often not available and the build will fail
RUN apt-get -qy update
RUN apt-get install -qy python python-dev python-pip git screen

# dependencis for building matplotlib
RUN apt-get -qy build-dep python-matplotlib

# installing fixed python package versions through pip 
RUN pip install --upgrade pip==9.0.1
RUN pip install numpy==1.14.1 scipy==1.0.0 matplotlib==1.4.2 sumatra==0.7.3 \
                gitpython==1.0.1 nose==1.3.7 ipython==5.5.0


# the method of installing graph_tool is likely to change in the
# future, so this command might need to be updated if build fails
# refer to graph_tool documentation: https://graph-tool.skewed.de/
RUN echo "deb http://downloads.skewed.de/apt/xenial xenial universe" | tee -a /etc/apt/sources.list
RUN echo "deb-src http://downloads.skewed.de/apt/xenial xenial universe" | tee -a /etc/apt/sources.list

RUN apt-key adv --keyserver pgp.skewed.de --recv-key 612DEFB798507F25
RUN apt-get -qy update
RUN apt-get install -qy python-graph-tool

#RUN apt-get install -qy texlive-full

RUN useradd -ms /bin/bash docker
USER docker
