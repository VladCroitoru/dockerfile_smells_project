FROM centos:6
MAINTAINER NASU,Tatsuya <tatu.nasu@gmail.com>
RUN yum -y -q update \
  && yum -y -q install \
    gcc git httpd httpd-devel wget \
    ImageMagick-devel \
  && yum clean all
RUN wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm \
  && rpm -ivh rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm \
  && rm rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm \
  && yum -y -q update rpmforge-release \
  && yum clean all
RUN yum -y -q install imlib2 imlib2-devel \
  && yum clean all

RUN git clone https://github.com/yamac/smalllight.git
RUN cd smalllight \
  && ./configure --with-apxs=/usr/sbin/apxs \
  && make && make install

COPY ./httpd/conf.d/smalllight.conf /etc/httpd/conf.d/smalllight.conf
COPY ./html /var/www/html

EXPOSE 80
ENTRYPOINT [ "/usr/sbin/httpd" ]
CMD [ "-D", "FOREGROUND" ]

