FROM        ubuntu:14.04

MAINTAINER Danilo Trani Recchia <danilo@deltatecnologia.com> 

ENV BACKUP_INTERVAL 10d
ENV BACKUP_OUTPUT_FORLDER /backup
ENV BACKUP_PREFIX jasperbackup

ENV SEND_BACKUP_TO_AWS false
ENV DELETE_AFTER_UPLOAD_TO_AWS true

ENV S3_BUCKET_NAME docker-jasper-backups.example.com
ENV AWS_ACCESS_KEY_ID **DefineMe**
ENV AWS_SECRET_ACCESS_KEY **DefineMe**
ENV AWS_DEFAULT_REGION us-east-1

ENV report_scheduler_mail_sender_host mail.localhost.com
ENV report_scheduler_mail_sender_username admin
ENV report_scheduler_mail_sender_password password
ENV report_scheduler_mail_sender_from admin@localhost.com
ENV report_scheduler_mail_sender_protocol smtp
ENV report_scheduler_mail_sender_port 25
ENV report_scheduler_web_deployment_uri http://localhost:8080/jasperserver

ADD files/backup_scheduler.sh /backup_scheduler.sh
ADD files/runme.sh /runme.sh

RUN         apt-get update && apt-get install -y \
                groff awscli \
                wget

RUN	    wget -q "http://downloads.sourceforge.net/project/jasperserver/JasperServer/JasperReports%20Server%20Community%20Edition%206.0.1/jasperreports-server-cp-6.0.1-linux-x64-installer.run?r=http%3A%2F%2Fcommunity.jaspersoft.com%2Fproject%2Fjasperreports-server%2Freleases&ts=1430837523&use_mirror=ufpr" -O /tmp/jasper.run && \
		chmod +x /tmp/jasper.run && \
		/tmp/jasper.run --prefix /opt/jasperserver \
			--mode unattended --jasperserver_install_sampledata 0 \
			--debuglevel 4 --tomcat_installation_type bundled \
			--tomcat_server_port 8080 --tomcat_server_shutdown_port 8005 --postgres_password postgres && \
		rm /tmp/jasper.run && \
		wget -q "http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.35/mysql-connector-java-5.1.35.jar" \
			-O /opt/jasperserver/apache-tomcat/lib/mysql-connector-java-5.1.35.jar && \
		chmod +x /runme.sh /backup_scheduler.sh && \
        	cat /opt/jasperserver/apache-tomcat/webapps/jasperserver/WEB-INF/js.quartz.properties | grep -v mail|grep -v deployment > /opt/jasperserver/apache-tomcat/webapps/jasperserver/WEB-INF/js.quartz.properties.template 

VOLUME /backup

# Expose port
EXPOSE 8080 

# Run 
ENTRYPOINT /runme.sh
