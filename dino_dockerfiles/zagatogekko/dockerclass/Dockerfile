FROM eboraas/apache
MAINTAINER Alan Acosta <zagato.gekko@gmail.com>

LABEL "Contenedor de Apache"

#RUN yum -y install vim gcc nano
# COPY nano-2.3.1-10.el7.x86_64.rpm /root/
#COPY vim-minimal-7.4.160-1.el7.x86_64.rpm /root
COPY apache2.conf /etc/apache2/sites-available/000-default.conf
# RUN rpm -i /root/nano-2.3.1-10.el7.x86_64.rpm

# RUN rpm -i /root/gcc*

# CMD "docker run -dti zagatogekko/apache"

