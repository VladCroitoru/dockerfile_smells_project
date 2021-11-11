FROM andrie/tensorflowr
MAINTAINER Steph Locke <steph@itsalocke.com>
RUN git clone https://github.com/lockedata/DOCKER-tensorflowr.git  && \
    cd DOCKER-tensorflowr/  && \
    chmod 777 ./mkusers.sh  && \
    ./mkusers.sh 
