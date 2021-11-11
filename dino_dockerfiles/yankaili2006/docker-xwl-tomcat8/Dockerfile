FROM dordoka/tomcat
MAINTAINER coola58 "yankaili2006@gmail.com"

ENV APP_HOME /opt/tomcat
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

#update system timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
 
#update application timezone
RUN echo "Asia/Shanghai" > /etc/timezone


ADD server.xml $APP_HOME/conf/server.xml
ADD run.sh $APP_HOME/run.sh

RUN /bin/sh -c $APP_HOME/run.sh
