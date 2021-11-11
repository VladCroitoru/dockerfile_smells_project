FROM    centos:centos7
RUN     rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm
RUN     yum install -y python-pip
RUN     pip install beaver
RUN     mkdir /app
RUN     mkdir /app/log
ADD     beaver.conf /app/beaver.conf

VOLUME ["/app/log"]

CMD    curl -o /app/beaver.conf $BEAVERCONF_URL; \
       beaver -c /app/beaver.conf $BEAVER_OPTS
