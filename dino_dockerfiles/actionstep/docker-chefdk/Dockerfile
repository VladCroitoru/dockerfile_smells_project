FROM debian:jessie
MAINTAINER operations <ops+docker@actionstep.com>

RUN apt-get update && apt-get install -y curl rsync ssh git
RUN curl -O https://packages.chef.io/files/stable/chefdk/1.5.0/debian/8/chefdk_1.5.0-1_amd64.deb
RUN dpkg -i chefdk_1.5.0-1_amd64.deb
RUN rm chefdk_1.5.0-1_amd64.deb

#RUN curl -O https://packages.chef.io/files/stable/chefdk/2.1.11/debian/8/chefdk_2.1.11-1_amd64.deb
#RUN dpkg -i chefdk_2.1.11-1_amd64.deb
#RUN rm chefdk_2.1.11-1_amd64.deb
