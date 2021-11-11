FROM ubuntu:14.04   
  
#刷新包缓存 并且 安装wget工具  
RUN apt-get update && apt-get install -y wget  
#设置工作目录  
WORKDIR /home  
# 安装jdk  
RUN wget --no-cookies --no-check-certificate --header "Cookie:gpw_e24=http%3a%2f%2fwww.oracle.com%2ftechnetwork%2fjava%2fjavase%2fdownloads%2fjdk7-downloads-1880260.html;oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz  
RUN tar -zxf jdk-7u79-linux-x64.tar.gz  
  
# 配置环境变量  
ENV JAVA_HOME /home/jdk1.7.0_79  
ENV JRE_HOME $JAVA_HOME/jre  
ENV CLASSPATH .:$JAVA_HOME/lib:$JRE_HOME/lib  
ENV PATH $PATH:$JAVA_HOME/bin  
  
#安装 tomcat7  
#RUN apt-get update  
# 中国下载路径
# RUN wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-7/v7.0.62/bin/apache-tomcat-7.0.62.tar.gz  
# RUN tar xvf apache-tomcat-7.0.62.tar.gz  
RUN wget http://apache.fayea.com/tomcat/tomcat-7/v7.0.70/bin/apache-tomcat-7.0.70.tar.gz
RUN tar xvf apache-tomcat-7.0.70.tar.gz  
  
#配置tomcat的环境变量  
ENV CATALINA_HOME /home/apache-tomcat-7.0.70  
  
EXPOSE 8080  
  
#设置tomcat 自启动  
CMD [ "/home/apache-tomcat-7.0.70/bin/catalina.sh", "run" ]  