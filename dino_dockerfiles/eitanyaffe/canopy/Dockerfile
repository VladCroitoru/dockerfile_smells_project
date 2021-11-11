FROM eitanyaffe/gcc-base

# install git
RUN sudo apt-get update && sudo apt-get install -y git

# install make
RUN sudo apt-get -y install make

# install canopy binary
ENV GIT_DIR /git
RUN mkdir $GIT_DIR
RUN cd $GIT_DIR && git clone https://bitbucket.org/HeyHo/mgs-canopy-algorithm.git

WORKDIR $GIT_DIR/mgs-canopy-algorithm/src
RUN make all