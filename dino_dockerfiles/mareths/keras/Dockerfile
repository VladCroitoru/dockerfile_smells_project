FROM tensorflow/tensorflow:latest
# use of CPU image

LABEL maintainer="Mareths"

# Install Keras
RUN pip --no-cache-dir install \
        keras
# Instal Git
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E1DD270288B4E6030699E45FA1715D88E1DF1F24
RUN su -c "echo 'deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main' > /etc/apt/sources.list.d/git.list"
RUN apt-get update
RUN apt-get install git -y

# Clone deeplearning codelab image
RUN git clone https://github.com/m09/deeplearning-codelab-image.git
