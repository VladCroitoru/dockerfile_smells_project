FROM	centos:7
RUN	yum install -y java-1.8.0-openjdk-devel vim unzip
RUN	curl -LO http://ftp.itu.edu.tr/Mirror/Apache/spark/spark-2.2.1/spark-2.2.1-bin-hadoop2.7.tgz && \
	tar xf spark-2.2.1-bin-hadoop2.7.tgz -C /opt && \
	ln -s /opt/spark-2.2.1-bin-hadoop2.7 /opt/spark && \
	rm -f spark-2.2.1-bin-hadoop2.7.tgz && \
	curl -LO https://s3.amazonaws.com/aws-glue-jes-prod-us-east-1-assets/etl/python/PyGlue.zip && \
	curl -L https://s3.eu-central-1.amazonaws.com/eugene.taranov.me/awsglue/glue-assembly.jar -o /opt/spark/jars/glue-assembly.jar && \
	curl -LO https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.11.tar.gz && \
	tar xf mysql-connector-java-8.0.11.tar.gz && \
	cp mysql-connector-java-8.0.11/mysql-connector-java-8.0.11.jar /opt/spark/jars/ && \
	rm -fr mysql-connector-java-8.0.11 mysql-connector-java-8.0.11.tar.gz && \
	curl -LO http://ftp.itu.edu.tr/Mirror/Apache/hadoop/common/hadoop-2.7.6/hadoop-2.7.6.tar.gz && \
	tar xf hadoop-2.7.6.tar.gz && \
	cp hadoop-2.7.6/share/hadoop/tools/lib/hadoop-aws-2.7.6.jar /opt/spark/jars/ && \
	cp hadoop-2.7.6/share/hadoop/tools/lib/aws-java-sdk-1.7.4.jar /opt/spark/jars/ && \
	rm -fr hadoop-2.7.6 hadoop-2.7.6.tar.gz
RUN	yum install -y epel-release && yum clean all && \
	yum install -y python-devel gcc python2-pip && \
	pip install 'ipython<6.0' && \
	pip install jupyter jupyterthemes jupyter_contrib_nbextensions jupyter_contrib_nbextensions && \
	pip install boto3 botocore awscli
RUN	useradd spark
USER	spark
RUN	mkdir -p /home/spark/.local/share/jupyter/kernels/spark && \
	jupyter contrib nbextension install --user && \
	jupyter nbextensions_configurator enable --user
COPY	libs/sqljdbc42.jar /opt/spark/jars
COPY	pythonrc /home/spark/.pythonrc
COPY	kernel.json /home/spark/.local/share/jupyter/kernels/spark/kernel.json
COPY	start.sh /
ENV	PYTHONSTARTUP=/home/spark/.pythonrc
ENV	PYTHONIOENCODING=utf8
EXPOSE	8888
WORKDIR	/home/spark
ENTRYPOINT ["/bin/bash", "/start.sh"]
