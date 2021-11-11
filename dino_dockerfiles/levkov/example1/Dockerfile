FROM centos:7
MAINTAINER levkov

RUN rm -f /etc/localtime && ln -sf /usr/share/zoneinfo/UTC /etc/localtime
RUN yum update -y
RUN yum install -y epel-release && \
    yum install -y python-pip openssh-server openssh-clients nginx redis dos2unix && \
    pip install supervisor requests==2.5.3 Flask gunicorn redis rq rq-dashboard rq-scheduler BeautifulSoup

RUN groupadd -r siteop && useradd -r -g siteop siteop && \
    echo 'root:ContaineR' | chpasswd

RUN rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
    ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
    sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
    sed -i "s/UsePAM.*/UsePAM yes/g" /etc/ssh/sshd_config

COPY conf/supervisord.conf /etc/supervisord.conf
COPY conf/default /etc/nginx/nginx.conf

ADD app /opt/app/
RUN chmod +x /opt/app/exec.sh && dos2unix /opt/app/exec.sh
EXPOSE 9001 22 80 9181 8080 8081
CMD ["/usr/bin/supervisord"]
