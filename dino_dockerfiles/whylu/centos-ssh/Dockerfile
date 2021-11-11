FROM centos:6.6
MAINTAINER WhyLu ML <whylu.ml@gmail.com>

# setup resource folder bind to container
ENV SETUP_RES_HOST ./setupResources
ENV SETUP_RES_CONTAINER /opt/.setupResources

## login msg
RUN echo '[ CentOS 6.6 ]' > /etc/motd


# openssh
RUN yum install -y openssh-server openssh-clients && \
    ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
    
# SSH login fix: user is kicked off after login
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config

# add setup resources
ADD ${SETUP_RES_HOST}/*.sh ${SETUP_RES_CONTAINER}/
RUN chmod +x ${SETUP_RES_CONTAINER}/*.sh


EXPOSE 22
CMD ${SETUP_RES_CONTAINER}/run.sh

