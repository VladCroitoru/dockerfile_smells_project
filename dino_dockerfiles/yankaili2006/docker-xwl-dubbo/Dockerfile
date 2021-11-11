FROM java:8
MAINTAINER coola58 "yankaili2006@gmail.com"

ENV APP_HOME /myapp
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

#update system timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#update application timezone
RUN echo "Asia/Shanghai" > /etc/timezone

#COPY /data/.m2/repository/com/xunwulian/xwl-dubbo/1.0-SNAPSHOT/xwl-dubbo-1.0-SNAPSHOT-jar-with-dependencies.jar $APP_HOME/app.jar

ADD run.sh $APP_HOME/run.sh

RUN /bin/sh -c $APP_HOME/run.sh

CMD ["java","-jar","app.jar"]
