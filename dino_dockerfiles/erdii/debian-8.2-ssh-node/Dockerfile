FROM erdii/debian-8.2-ssh
MAINTAINER erdii <erdii@nym.hush.com>

# install curl
RUN apt-get install -y curl

# add node repo and install it
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -
RUN apt-get install -y nodejs
