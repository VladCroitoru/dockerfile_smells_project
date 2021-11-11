FROM amazonlinux
ENV AWSLOGS_ENV "false"
ENV AWSCLI_ENV "false"
ENV AWS_REGION = "us-east-1"
RUN yum update -y && yum install -y \
		awslogs \
	&& yum clean all \
	&& easy_install supervisor 

#RUN pip-2.6 install --upgrade pip
#RUN pip install supervisor supervisor-stdout
COPY supervisord.conf /etc/supervisord.conf
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh

