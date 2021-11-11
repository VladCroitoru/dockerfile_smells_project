FROM semoss/docker-r-python:R3.6.2-debian10 as base

FROM semoss/docker-tomcat:debian10 as mavenpuller

# skip cache based on the semoss-artifacts 
RUN apt-get update -y \
	&& apt-get install -y curl lsof \
	&& mkdir /opt/semosshome
ADD "https://api.github.com/repos/SEMOSS/semoss-artifacts/git/refs/heads/master" skipcache
RUN cd /opt && git clone https://github.com/SEMOSS/semoss-artifacts \
	&& chmod 777 /opt/semoss-artifacts/artifacts/scripts/*.sh \
	&& /opt/semoss-artifacts/artifacts/scripts/update_latest_dev.sh \
	&& chmod 777 /opt/semosshome/config/Chromedriver/*

FROM base

LABEL maintainer="semoss@semoss.org"

ENV PATH=$PATH:/opt/semoss-artifacts/artifacts/scripts
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib:/usr/local/lib/R/site-library/rJava/jri
ENV R_HOME=/usr/lib/R

# Install Rclone
# Create semosshome
# Clone semoss-artifacts scripts
# Update latest dev code
# Install Chrome
# Set LD_PRELOAD on Tomcat

RUN	wget https://downloads.rclone.org/v1.47.0/rclone-v1.47.0-linux-amd64.deb \
	&& dpkg -i rclone-v1.47.0-linux-amd64.deb \
	&& apt-get install -f \
	&& rm rclone-v1.47.0-linux-amd64.deb \
	&& chmod 777 /usr/bin/rclone \
	&& mkdir /opt/semosshome \
	&& mkdir $TOMCAT_HOME/webapps/Monolith \
	&& mkdir $TOMCAT_HOME/webapps/SemossWeb \
	&& echo "export LD_PRELOAD=/usr/lib/python3.7/config-3.7m-x86_64-linux-gnu/libpython3.7.so" >> $TOMCAT_HOME/bin/setenv.sh \
	&& cp /usr/lib/jvm/zulu8.44.0.13-ca-fx-jdk8.0.242-linux_x64/lib/tools.jar $TOMCAT_HOME/lib \
	&& sed -i "s/tomcat.util.scan.StandardJarScanFilter.jarsToSkip=/tomcat.util.scan.StandardJarScanFilter.jarsToSkip=*.jar,/g" $TOMCAT_HOME/conf/catalina.properties;

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list \
	&& apt-get update \
	&& apt-get install -y google-chrome-stable

ADD "https://api.github.com/repos/SEMOSS/semoss-artifacts/git/refs/heads/master" skipcache
RUN apt-get update -y \
	&& apt-get install -y curl lsof \
	&& cd /opt && git clone https://github.com/SEMOSS/semoss-artifacts \
	&& chmod 777 /opt/semoss-artifacts/artifacts/scripts/*.sh

COPY --from=mavenpuller /opt/semosshome /opt/semosshome
COPY --from=mavenpuller $TOMCAT_HOME/webapps/Monolith $TOMCAT_HOME/webapps/Monolith
COPY --from=mavenpuller $TOMCAT_HOME/webapps/SemossWeb $TOMCAT_HOME/webapps/SemossWeb
COPY --from=mavenpuller /opt/semoss-artifacts/ver.txt /opt/semoss-artifacts/ver.txt

WORKDIR /opt/semoss-artifacts/artifacts/scripts

CMD ["start.sh"]
