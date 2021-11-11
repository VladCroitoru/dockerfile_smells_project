# docker run --rm -ti -v /var/run/:/var/run/:rw monitoringartist/play.monitoringartist.com

FROM alpine:latest

RUN \
  apk add -U py2-pip docker && \
  pip install 'docker-compose==1.9.0' && \
  rm -rf $(apk info -L iptables) && \
  rm -rf $(apk info -L git) && \
  rm -rf $(apk info -L libssh2) && \
  rm -rf $(apk info -L iptables) && \
  rm -rf $(apk info -L libmnl) && \
  rm -rf $(apk info -L libnftnl-libs) && \
  rm -rf $(apk info -L xz-libs) && \
  rm -rf $(apk info -L pcre) && \
  rm -rf $(apk info -L libseccomp) && \
  rm -rf $(apk info -L libcurl) && \
  rm -rf $(apk info -L xz)

ADD run.sh /
ADD docker-compose.yml /

ENTRYPOINT ["/run.sh"]

CMD start
