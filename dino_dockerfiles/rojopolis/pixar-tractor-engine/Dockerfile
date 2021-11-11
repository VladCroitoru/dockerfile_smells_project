FROM centos:6

ADD Tractor-2.2_1715407-linuxRHEL6_gcc44icc150.x86_64.rpm .
RUN rpm -ivh Tractor-2.2_1715407-linuxRHEL6_gcc44icc150.x86_64.rpm &&\
    rm -f Tractor-2.2_1715407-linuxRHEL6_gcc44icc150.x86_64.rpm && \
    useradd -ms /bin/bash tractor

VOLUME /var/spool/tractor

EXPOSE 80

CMD ["/opt/pixar/Tractor-2.2/bin/tractor-engine", "-c", "/var/spool/tractor"]