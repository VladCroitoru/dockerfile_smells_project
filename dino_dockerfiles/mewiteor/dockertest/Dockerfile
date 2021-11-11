FROM ubuntu:16.04
MAINTAINER mewiteor@hotmail.com
ENV LANG zh_CN.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ADD bin /usr/local/bin/
ADD locale.gen /etc/
RUN apt-get update && apt-get install -y curl w3m zhcon
CMD ["hello"]
