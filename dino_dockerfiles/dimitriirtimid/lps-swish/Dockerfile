FROM ubuntu:16.04

LABEL maintainer = "dimitri_dekker@hotmail.com"
# Thanks to Kacper Sokol <ks1591@bristol.ac.uk> as this dockerfile is inspired by https://hub.docker.com/r/so8cool/swish

USER root
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-add-repository ppa:swi-prolog/devel
RUN apt-get update
RUN apt-get install -y git swi-prolog graphviz npm nodejs-legacy curl
RUN npm install -g bower

# Set environment variables
ENV SHELL /bin/bash
ENV SWISH_DIR swish
ENV LPS_DIR lps
ENV SWISH_USER swish
ENV HOME /home/$SWISH_USER
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Create swish user
RUN useradd -m -s /bin/bash $SWISH_USER
RUN mkdir -p $HOME
RUN chown $SWISH_USER $HOME


USER $SWISH_USER

# setup swish environment
WORKDIR $HOME
RUN git clone https://github.com/SWI-Prolog/swish.git $SWISH_DIR
WORKDIR $HOME/$SWISH_DIR
# modify the server.pl file so the server port is opened on all networks otherwise the port does not get exposed
RUN sed -i -e 's/server(localhost:3050)/server(3050)/g' server.pl
RUN bower install
RUN make src

# setup LPS environment
WORKDIR $HOME
RUN git clone https://bitbucket.org/lpsmasters/lps_corner $LPS_DIR
WORKDIR $HOME/$LPS_DIR/swish/web/lps
RUN bower install vis paper

# expose the network port of the swish web server
EXPOSE 3050

# Configure container startup
WORKDIR $HOME/$LPS_DIR/swish
ENTRYPOINT /usr/bin/swipl -l user_module_file.pl -l ../../swish/server.pl -g server:server
