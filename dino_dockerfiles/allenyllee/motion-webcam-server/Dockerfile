# dockerfile template
#
# VERSION               0.0.1

FROM      ubuntu:16.04
LABEL     maintainer="allen7575@gmail.com"

############
# update package list
############
RUN apt update

##########
# install vim
##########
RUN apt install -y vim


############
# put something here...
############


############
# install motion
############
# htmlpreview.github.io/?https://github.com/Motion-Project/motion/blob/master/motion_guide.html#Abbreviated_Building
# https://htmlpreview.github.io/?https://github.com/Motion-Project/motion/blob/master/motion_guide.html#Abbreviated_Building
#

# dependency
RUN apt-get install -y autoconf automake build-essential pkgconf libtool libzip-dev libjpeg-dev git libavformat-dev libavcodec-dev libavutil-dev libswscale-dev libavdevice-dev

# build & install
RUN bash -c " \
cd ~ && \
git clone https://github.com/Motion-Project/motion.git && \
cd motion && \
autoreconf -fiv && \
./configure && \
make && \
make install && \
cd ~ && rm -rf ./motion"

############
# add, change username,password,group here
############
# change root password
# RUN echo root:root | chpasswd

# add guest user
# useradd - Ubuntu 14.04: New user created from command line has missing features - Ask Ubuntu
# https://askubuntu.com/questions/643411/ubuntu-14-04-new-user-created-from-command-line-has-missing-features
# RUN useradd -m guest -s /bin/bash && \
#    echo guest:guest | chpasswd

# grant access for guest to video device
# RUN usermod -a -G video guest `# grant access to video device`

##############
# upgrade
##############
RUN apt upgrade -y

##############
# cleanup
##############
# debian - clear apt-get list - Unix & Linux Stack Exchange
# https://unix.stackexchange.com/questions/217369/clear-apt-get-list
#
# bash - autoremove option doesn't work with apt alias - Ask Ubuntu
# https://askubuntu.com/questions/573624/autoremove-option-doesnt-work-with-apt-alias
#
RUN apt-get autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#################
# init script
#################

ADD ./scripts/* /scripts/

# starting container process caused "exec: \"./extra/service_startup.sh\": permission denied" · Issue #431 · facebook/fbctf
# https://github.com/facebook/fbctf/issues/431
RUN chmod +x /scripts/*

ENTRYPOINT ["/scripts/init.sh"]

CMD ["bash"]