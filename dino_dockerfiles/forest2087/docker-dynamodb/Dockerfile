FROM tray/java:8-jre
MAINTAINER Forest W

#Create work space
RUN mkdir /var/dynamodb_wd

WORKDIR /var/dynamodb_wd

#Get package from amazon
RUN /usr/bin/curl -L http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest | /bin/tar xz

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME ["/var/dynamodb_local", "/var/dynamodb_wd"]

RUN apt-get update

RUN apt-get install -y python-pip python-dev
RUN pip install boto
RUN pip install boto3

RUN mkdir /var/dynamodump

WORKDIR /var/dynamodump

ADD Build/dump.tar /var/dynamodump

RUN if [ -d "/Users/forest/.aws" ]; then cp -r /Users/forest/.aws ~/.aws; fi

ADD Build/start.sh   /sbin/start.sh
RUN chmod +x /sbin/start.sh
CMD ["/sbin/start.sh"]
