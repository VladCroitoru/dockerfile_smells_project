FROM pnnlhep/osg-base
MAINTAINER Kevin Fox "Kevin.Fox@pnnl.gov"

RUN \
  #sed -i 's@osg/3.2@osg/3.3@g' /etc/yum.repos.d/osg-el6* && \
  sed -i 's@repo.grid.iu.edu@repo.opensciencegrid.org@' /etc/yum.repos.d/osg-el6* && \
  yum upgrade -y
RUN \
  yum install -y osg-se-bestman lcmaps-plugins-gums-client lcmaps-plugins-basic lcmaps-plugins-verify-proxy pyxattr sudo attr globus-proxy-utils globus-gass-copy-progs && \
  yum install -y java-1.8.0-openjdk-headless.x86_64 java-1.8.0-openjdk java-1.8.0-openjdk-devel-1.8.0.191.b12-0.el6_10.x86_64 && \
  rm -f /etc/alternatives/java_sdk && \
  ln -s /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.191.b12-0.el6_10.x86_64/ /etc/alternatives/java_sdk && \
  ls -l /etc/alternatives/java_sdk/bin
ADD ./adler32 /usr/bin/adler32
RUN chmod +x /usr/bin/adler32
ADD ./start.sh /etc/start.sh
RUN chmod +x /etc/start.sh
RUN cp -a /etc/lcmaps.db /etc/lcmaps.db.bak
RUN echo globus_mapping liblcas_lcmaps_gt4_mapping.so lcmaps_callout echo > /etc/grid-security/gsi-authz.conf.bak
ADD srm /etc/sudoers.d/srm
RUN sed -i 's/&$//' /usr/sbin/bestman.server

CMD ["/etc/start.sh"]
