FROM felix11h/scipy3_env-jupyter
MAINTAINER felix11h.dev@gmail.com

USER root
RUN pip3 install networkx

# current the method of installing graph_tool as
# documented on website https://graph-tool.skewed.de/
# installs graph_tool version 2.26
RUN echo "deb http://downloads.skewed.de/apt/xenial xenial universe" | tee -a /etc/apt/sources.list
RUN echo "deb-src http://downloads.skewed.de/apt/xenial xenial universe" | tee -a /etc/apt/sources.list

RUN apt-key adv --keyserver pgp.skewed.de --recv-key 612DEFB798507F25
RUN apt-get -qy update
RUN apt-get install -qy python3-graph-tool

RUN apt-get install -qy pandoc
RUN apt-get install texlive


# FROM ubuntu:16.04
# MAINTAINER felix11h.dev@gmail.com

# USER root

# RUN apt-get update
# RUN apt-get install -y git python3-pip python3-nose screen
# RUN pip3 install ipython numpy scipy matplotlib pandas gitpython sumatra networkx

# # Adapted from Ivo Jimenez
# RUN apt-get -yq update && \
#     apt-get install -qy --fix-missing \
#         texlive \
#         texlive-latex-extra \
# 	texlive-science \
#         texlive-math-extra \
# 	dvipng && \
#     apt-get -yq autoremove && \
#     apt-get clean -y && \
# rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# RUN pip3 install --upgrade pip
# RUN pip3 install jupyter

# RUN pip3 install RISE
# RUN jupyter-nbextension install rise --py --sys-prefix
# RUN jupyter-nbextension enable rise --py --sys-prefix

# RUN useradd -ms /bin/bash docker

# WORKDIR /home/lab

# EXPOSE 8888
