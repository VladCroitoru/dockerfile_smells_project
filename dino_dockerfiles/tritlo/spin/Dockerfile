from ubuntu


RUN apt-get update  &&\
    apt-get upgrade &&\
    apt-get install -y build-essential man less byacc curl


ENV VERSION 645

RUN curl -L http://spinroot.com/spin/Src/spin$VERSION.tar.gz -o /spin.tar.gz &&\
    tar -xf /spin.tar.gz &&\
    rm /spin.tar.gz && \
    cd /Spin/Src* &&\
    make &&\
    make install &&\
    cd / &&\
    rm -rf Spin spin.tar.gz &&\
    mkdir /data

WORKDIR /data

ENTRYPOINT ["spin"]
