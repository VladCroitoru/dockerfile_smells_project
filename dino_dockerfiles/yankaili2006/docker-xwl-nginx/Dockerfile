FROM nginx:mainline-alpine
MAINTAINER coola58 "yankaili2006@gmail.com"

ENV WWW_HOME /usr/share/nginx/html
RUN mkdir -p $WWW_HOME
WORKDIR $WWW_HOME

#update system timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
 
#update application timezone
RUN echo "Asia/Shanghai" >> /etc/timezone

ADD nginx.conf /etc/nginx/nginx.conf
ADD anjia1 $WWW_HOME/anjia1

