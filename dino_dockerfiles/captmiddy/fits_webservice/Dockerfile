FROM dordoka/tomcat
MAINTAINER "Anthony Moulen <amoulen@g.harvard.edu>"
ADD catalina.properties /opt/tomcat/conf
ADD http://projects.iq.harvard.edu/files/fits/files/fits-0.10.2.zip /home
ADD http://projects.iq.harvard.edu/files/fits/files/fits-1.1.1.war /opt/tomcat/webapps/fits.war
RUN mkdir /processing
RUN cd /home ; unzip -q fits-0.10.2.zip ; rm /home/fits*zip ; mv /home/fits-* /home/fits
VOLUME ["/processing"]
