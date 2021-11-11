FROM tomcat

#RUN wget http://apachemirror.wuchna.com/tomcat/tomcat-8/v8.5.54/bin/apache-tomcat-8.5.54.tar.gz
WORKDIR /usr/local/tomcat/webapps
RUN mkdir oracle
WORKDIR oracle
ADD myapp . 
EXPOSE 8080

# ENTRYPOINT / CMD will be inherited by tomcat base image 
