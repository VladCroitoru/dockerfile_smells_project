# sshd
#
# VERSION               0.0.2

FROM ubuntu:14.04
MAINTAINER Sven Dowideit <SvenDowideit@docker.com>

RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y build-essential
RUN apt-get install -y automake
RUN apt-get install -y bison flex
RUN apt-get install -y libcurl4-gnutls-dev
RUN apt-get install -y autotools-dev
RUN apt-get install -y libboost-dev
RUN apt-get install -y openssh-server
RUN apt-get install -y git
RUN apt-get install -y cmake
RUN apt-get install -y libpthread-stubs0-dev


RUN git clone https://github.com/miloyip/rapidjson /tmp/rapidjson
RUN sudo cp -r /tmp/rapidjson/include/rapidjson /usr/include/

ENV PATH_GSOAP /root/gsoap
RUN git clone https://github.com/JinpengLI/gsoap.git $PATH_GSOAP


RUN sed -i '1i#ifndef WITH_COOKIES\n#define WITH_COOKIES\n#endif\n' $PATH_GSOAP/gsoap/stdsoap2.h
RUN cd $PATH_GSOAP && aclocal
RUN cd $PATH_GSOAP && autoheader
RUN cd $PATH_GSOAP && automake --add-missing
RUN cd $PATH_GSOAP && autoconf
RUN cd $PATH_GSOAP && automake
RUN cd $PATH_GSOAP && ./configure
RUN cd $PATH_GSOAP && make
RUN cd $PATH_GSOAP && sudo make install

ENV PATH_CARMIN_R2S /root/CARMIN_R2S
RUN git clone https://github.com/JinpengLI/CARMIN_R2S.git ${PATH_CARMIN_R2S}
RUN cp $PATH_CARMIN_R2S/CMakeLists.txt.origin $PATH_CARMIN_R2S/CMakeLists.txt
RUN mkdir -p $PATH_CARMIN_R2S/build && cd $PATH_CARMIN_R2S/build && cmake .. && make

RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
