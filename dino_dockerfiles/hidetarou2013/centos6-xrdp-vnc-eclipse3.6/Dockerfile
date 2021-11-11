FROM kevensen/centos-vnc-eclipse
MAINTAINER hidetarou2013 <hidetoshi_maekawa@e-it.co.jp>

RUN ls -la /usr/bin/vncserver
RUN grep "1024" /usr/bin/vncserver
USER root
WORKDIR /usr/bin
RUN sed -i -e 's/1024x768/1536x1024/g' vncserver
USER kioskuser
