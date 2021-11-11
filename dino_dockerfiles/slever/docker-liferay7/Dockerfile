# Liferay Portal 7 CE
#
# VERSION               0.0.1

FROM java:8

MAINTAINER Sebastien LEVER, sebastien.lever@gmail.com

# Download Liferay Portal 6.2-ce-ga4  
RUN wget -q http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/7.0.0%20GA1/liferay-portal-tomcat-7.0-ce-ga1-20160331161017956.zip

# Unzip the Portal Tomcat Bundle
RUN unzip -qq liferay-portal-tomcat-7.0-ce-ga1-20160331161017956.zip

# Default customized portal-ext.properties that will enable the users
# to point the Liferay home to the mount volume
ADD ./liferay/conf/portal-ext.properties /liferay-portal-7.0-ce-ga1/portal-ext.properties

# Remove the bundle
RUN rm liferay-portal-tomcat-7.0-ce-ga1-20160331161017956.zip

# Setup Mount Volume Directories
RUN mkdir -p /liferay/deploy && mv liferay-portal-7.0-ce-ga1/data /liferay/data && mv liferay-portal-7.0-ce-ga1/osgi liferay/osgi

# Liferay Home Dir
VOLUME  /liferay

## Container Start

WORKDIR /liferay-portal-7.0-ce-ga1

# Expose the ports HTTP | OSGi console

EXPOSE 8080 

EXPOSE 11311

## Add points of extension
ONBUILD ADD ./deploy /liferay/deploy
ONBUILD ADD ./lib    /liferay-portal-7.0-ce-ga1/tomcat-8.0.32/lib
ONBUILD COPY ./bin/*.sh /liferay-portal-7.0-ce-ga1/tomcat-8.0.32/bin/

# Start Liferay
ENTRYPOINT ["tomcat-8.0.32/bin/catalina.sh"]
CMD ["run"]
