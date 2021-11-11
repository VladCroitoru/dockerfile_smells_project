FROM centos:6
RUN \
  yum install -y rpmdevtools git
RUN \
  git clone https://github.com/jbraeuer/yum-s3-plugin.git && \
  cd yum-s3-plugin && \
  chmod +x package


VOLUME /data

CMD cd yum-s3-plugin &&  \
  ./package -d && \
  cp -v /yum-s3-plugin/RPMS/noarch/* /data/ 


