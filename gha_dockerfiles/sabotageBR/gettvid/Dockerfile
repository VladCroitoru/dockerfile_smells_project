FROM evandromoura/wildfly:nettools-2.0

	LABEL MAINTAINER Evandro Moura <evandromoura@gmail.com>

	USER jboss
	
	ARG cliente

	ENV PYTHONIOENCODING=utf-8

	COPY kubernetes/docker-entrypoint.sh $JBOSS_HOME/docker-entrypoint.sh
	
	#RUN chown jboss $JBOSS_HOME/docker-entrypoint.sh && \
	# 	chmod a+x $JBOSS_HOME/docker-entrypoint.sh

	#KUBE_PING
	COPY kubernetes/kubeping-module $JBOSS_HOME/modules/system/layers/base/org/jgroups/kubernetes
	
	#CONEXAO
	COPY kubernetes/standalone-full-ha.xml $JBOSS_HOME/standalone/configuration/standalone-full-ha.xml
	COPY kubernetes/postgresql-42.2.23.jre6.jar $JBOSS_HOME/standalone/deployments/

	#BUILD
	COPY /target/gettvid.war $JBOSS_HOME/standalone/deployments/
	
	#PORTAS
	EXPOSE 8080 8009 9990 7600 8888
	
	

	ENTRYPOINT $JBOSS_HOME/docker-entrypoint.sh