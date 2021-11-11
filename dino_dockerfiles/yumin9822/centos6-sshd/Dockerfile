FROM centos:6

RUN yum -y install openssh-server
RUN echo "root:p@ssw0rd99" | chpasswd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN /etc/init.d/sshd restart

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
