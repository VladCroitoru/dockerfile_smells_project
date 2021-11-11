FROM tomcat

RUN ["rm", "-fr", "/usr/local/tomcat/webapps/ROOT"]
COPY ./sample/sample.war /usr/local/tomcat/webapps/sample.war
RUN unzip -C /usr/local/tomcat/webapps/sample.war -d /usr/local/tomcat/webapps/sample
#RUN rm -rf /usr/local/tomcat/webapps/sample.war
COPY ./sample/test01.txt /usr/local/tomcat/webapps/ 

#TO BE ADDED
COPY ./sample/server /usr/local/tomcat/conf/

EXPOSE 8089

CMD ["catalina.sh", "run"]
