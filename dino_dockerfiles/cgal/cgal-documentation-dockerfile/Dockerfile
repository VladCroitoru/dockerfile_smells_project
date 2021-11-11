FROM cgal/testsuite-docker:ubuntu
MAINTAINER Philipp Moeller <bootsarehax@gmail.com>
RUN  apt-get update \
  && apt-get install -y bison \
     git \
     flex \
     graphviz \
     python3 \
     python3-pyquery \
     texlive-binaries \
  && apt-get clean -y

RUN mkdir /doxygen
WORKDIR /doxygen

RUN git clone https://github.com/CGAL/doxygen.git cgal_dox && \
    mkdir cgal_1_8_13 && \
    cd cgal_dox && \
    git checkout release_1_8_13_patched && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    cp bin/doxygen ../../cgal_1_8_13 && \
    cd ../../ && rm -rf cgal_dox



RUN git clone https://github.com/doxygen/doxygen.git off_dox && \
    mkdir cgal_1_9_1 && \
    cd off_dox && \
    git checkout Release_1_9_1 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    cp bin/doxygen ../../cgal_1_9_1 && \
    cd ../../ && rm -rf off_dox

USER root

COPY ./docker_entrypoint.sh /
ENTRYPOINT ["/docker_entrypoint.sh"]
CMD ["cgal_build_documentation"]
