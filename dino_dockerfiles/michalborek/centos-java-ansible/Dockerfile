FROM michalborek/centos-java:openjdk
MAINTAINER Michal Borek <michal@greenpath.pl>

USER root

RUN yum clean all && \
    yum -y install epel-release && \
    yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools git python-pip
RUN mkdir /etc/ansible/
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts
RUN mkdir /opt/ansible/
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible
WORKDIR /opt/ansible/ansible
RUN git submodule update --init
RUN wget http://raw.githubusercontent.com/ansible/ansible/devel/lib/ansible/plugins/callback/json.py -O /opt/ansible/ansible/lib/ansible/plugins/json.py
ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin 
ENV PYTHONPATH /opt/ansible/ansible/lib 
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library

USER ms 
CMD [ -f /ms/config ] && . /ms/config ; java $MS_JAVA_OPTS -jar "/ms/${MS_JAR_NAME}"
