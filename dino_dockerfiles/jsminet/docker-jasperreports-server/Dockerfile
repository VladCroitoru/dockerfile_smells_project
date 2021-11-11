FROM ubuntu:17.04
MAINTAINER JS Minet

ENV JS_CE_VERSION 6.3.0
ENV JS_CE_HOME /opt/jasperreports-server-cp-${JS_CE_VERSION}
ENV PATH $PATH:${JS_CE_HOME}

RUN apt-get update && apt-get install -y wget \
	&& wget --progress=bar:force:noscroll -O jasperreports-server-linux-x64-installer.run http://netcologne.dl.sourceforge.net/project/jasperserver/JasperServer/JasperReports%20Server%20Community%20Edition%20${JS_CE_VERSION}/jasperreports-server-cp-${JS_CE_VERSION}-linux-x64-installer.run \
	&& chmod a+x jasperreports-server-linux-x64-installer.run \
	&& /jasperreports-server-linux-x64-installer.run --mode unattended --jasperLicenseAccepted yes --postgres_password Postgres1 \
	&& rm jasperreports-server-linux-x64-installer.run \
	&& rm -rf ${JS_CE_HOME}/apache-ant ${JS_CE_HOME}/buildomatic \
			  ${JS_CE_HOME}/docs ${JS_CE_HOME}/samples ${JS_CE_HOME}/scripts \
	&& rm ${JS_CE_HOME}/TIBCO-EULA.txt ${JS_CE_HOME}/uninstall \
	&& apt-get clean

EXPOSE 8080 

CMD ctlscript.sh start && tail -f /dev/null