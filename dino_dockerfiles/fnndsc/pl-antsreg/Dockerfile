# Docker file for the antsreg plugin app

FROM fnndsc/centos-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/antsreg" 
COPY ["antsreg", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

##################  ANTS INSTALLATION ##################
RUN yum install -y cmake make git libstdc++-static && \
    cd $HOME &&                                       \
    git clone https://github.com/Chris210634/ANTs.git &&    \
    cd ANTs &&                                        \
    git reset --hard 9b0eec74a33c174fcedebf174b5c6baca9c21ccd \
    mkdir -p bin/ants &&                              \
    cd bin/ants                                       \
    echo "Starting ccmake" &&                         \
    cmake $HOME/ANTs -DUSE_PROCESS_PARALLELIZE_ITK=ON \
                     -DBUILD_TESTING=OFF              \
                     -DRUN_LONG_TESTS=OFF             \ 
                     -DRUN_SHORT_TESTS=OFF &&         \
    echo "End ccmake" &&                              \
    make -j 10 &&                                     \
    cp -r ~/ANTs/Scripts/. ~/ANTs/bin/ants/bin &&     \
    cp -r ~/ANTs/bin/ants/bin ~ 

ENV ANTSPATH=${HOME}/bin/ 

ENV PATH=${ANTSPATH}:$PATH
#######################################################

##################  DCM2NIIX INSTALLATION #############
RUN cd $HOME &&                                             \
    git clone https://github.com/rordenlab/dcm2niix.git &&  \
    cd dcm2niix &&                                          \ 
    git checkout tags/v1.0.20171204 &&                      \
    mkdir build && cd build &&                              \
    cmake ..    &&                                          \ 
    make &&                                                 \
    cp ./bin/dcm2niix $ANTSPATH &&                          \
    yum remove -y cmake make git libstdc++-static &&        \
    rm -rf ~/dcm2niix && rm -rf ~/ANTs    
#######################################################

RUN pip3 install -r requirements.txt

CMD ["antsreg.py", "--help"]
