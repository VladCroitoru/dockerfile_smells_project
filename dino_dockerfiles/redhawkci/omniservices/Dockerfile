FROM centos:6
MAINTAINER Ryan Bauman <ryanbauman@gmail.com>

COPY redhawk.repo /etc/yum.repos.d/

RUN yum update -y && \
    yum install -y epel-release && \
    yum install -y omniORB-servers \
                   omniEvents-server \
                   supervisor && yum clean all

COPY supervisord.conf /etc/
COPY omniORB.cfg /etc/

#configure omniEvents
RUN mkdir -p /var/log/omniEvents
RUN chown omniORB /var/log/omniEvents

#expose ports for omniNames and omniEvents
EXPOSE 2809
EXPOSE 11169

CMD ["/usr/bin/supervisord", "-n"]
