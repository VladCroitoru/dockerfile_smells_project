FROM centos:7
RUN yum install -y python-setuptools git gcc python-devel && easy_install pip && pip install -U flask requests netifaces && cd /var/tmp && git clone https://github.com/tnaganawa/open-pager-url
EXPOSE 5001
CMD ["/bin/bash", "-c", "cd /var/tmp/open-pager-url; ./entrypoint.sh"]
