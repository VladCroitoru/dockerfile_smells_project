FROM jetty:9.3

#ENV http_proxy http://proxy:8080
#ENV https_proxy http://proxy:8080

# create download directory
RUN mkdir -p ~/build/helenos
RUN cd ~/build/helenos
 
# download war
RUN wget https://s3.amazonaws.com/lbk/helenos-1.5.war
 
# copy to helenos.war
RUN cp helenos-1.5.war helenos.war
 
# make jetty user the owner of helenos.war
RUN chown jetty:jetty helenos.war
 
# move the war file to webapps
RUN mv helenos.war /usr/local/jetty/webapps/
RUN mkdir /usr/local/jetty/webapps/WEB-INF/
COPY default.properties /usr/local/jetty/webapps/WEB-INF/
COPY default.properties /usr/local/jetty/webapps/

EXPOSE 8080 
# Using jetty
# http://localhost:8080/helenos
WORKDIR $JETTY_HOME
CMD java -jar start.jar
 
# test


 

