FROM python:2
MAINTAINER Erwin Janssen <erwinjanssen@outlook.com>
RUN mkdir -p /opt/bloodhound
RUN curl -SL "http://ftp.nluug.nl/internet/apache/bloodhound/apache-bloodhound-0.8.tar.gz" -o apache-bloodhound.tar.gz
RUN pip install --upgrade pip
RUN tar xvzf apache-bloodhound.tar.gz
RUN rm apache-bloodhound.tar.gz
RUN cd apache-bloodhound-0.8/installer \
	&& pip install -r requirements.txt \
	&& python bloodhound_setup.py --database-type=sqlite --admin-user=admin --admin-password=adminpassword
CMD tracd --port=8000 /apache-bloodhound-0.8/installer/bloodhound/environments/main

