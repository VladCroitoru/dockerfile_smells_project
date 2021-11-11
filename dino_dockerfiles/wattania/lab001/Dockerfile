FROM ubuntu
MAINTAINER Wattana <>

# set timezone to Bangkok

ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
 && echo $TZ > /etc/timezone
