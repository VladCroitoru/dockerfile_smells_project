#
# s3repo
# utility to push RPMS to a yum repo hosted on s3
#
# inspired by https://github.com/discordianfish/docker-lloyd
#
FROM fedora:20
MAINTAINER James DeFelice <james.defelice@gmail.com>

#ENV BUCKET_NAME mythtv-testing
#ENV ACCESS_KEY  ...
#ENV SECRET_KEY  ...

RUN yum -y install git python-setuptools python-dateutil python-magic createrepo
RUN git clone https://github.com/s3tools/s3cmd.git /s3cmd
RUN cd /s3cmd && python setup.py install

ADD s3cfg /.s3cfg

WORKDIR /home/makerpm/exports/RPMS

ADD run.sh /
CMD /run.sh
