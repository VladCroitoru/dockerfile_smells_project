FROM ubuntu:14.04.2

ADD build/etc/apt/apt.conf.d/90-AlwaysYes /etc/apt/apt.conf.d/90-AlwaysYes

RUN apt-get update
RUN apt-get install wget
RUN apt-get install subversion
RUN apt-get install build-essential
RUN apt-get install flex
RUN apt-get install bison
RUN apt-get install libboost-dev
RUN apt-get install gputils
RUN apt-get install stx-btree-dev
#RUN wget "http://downloads.sourceforge.net/project/sdcc/snapshot_builds/amd64-unknown-linux2.5/sdcc-snapshot-amd64-unknown-linux2.5-20150616-9248.tar.bz2?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fsdcc%2Ffiles%2Fsnapshot_builds%2Famd64-unknown-linux2.5%2F&ts=1434521841&use_mirror=freefr" -O sdcc.tar.bz2
#RUN wget "http://downloads.sourceforge.net/project/sdcc/sdcc-linux-x86/3.5.0/sdcc-3.5.0-rc1-i386-unknown-linux2.5.tar.bz2?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fsdcc%2Ffiles%2Fsdcc-linux-x86%2F3.5.0%2F&ts=1434516578&use_mirror=netcologne" -O sdcc.tar.bz2
#RUN tar xf sdcc.tar.bz2
#RUN cp -r sdcc-3.5.0-rc1/* /usr/.

RUN svn checkout svn://svn.code.sf.net/p/gputils/code/trunk gputils-code

WORKDIR /gputils-code/gputils
RUN ./configure
RUN make
RUN make install
WORKDIR /
RUN svn checkout svn://svn.code.sf.net/p/sdcc/code/tags/sdcc-3.5.0-pre1 sdcc
WORKDIR /sdcc/sdcc
RUN ./configure
RUN make
RUN make install
