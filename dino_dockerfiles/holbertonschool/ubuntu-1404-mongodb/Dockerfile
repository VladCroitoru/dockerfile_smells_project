# Container for developing in MongoDb and Python 3 at Holberton School

FROM holbertonschool/ubuntu-1404-python3
MAINTAINER Guillaume Salva <guillaume@holbertonschool.com>

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
RUN echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.6 multiverse" > /etc/apt/sources.list.d/mongodb-org-3.6.list

RUN apt-get update

RUN mkdir -p /data/db

RUN apt-get install -y mongodb-org

RUN pip3 install pymongo

ADD init.d-mongod /etc/init.d/mongod
RUN chmod u+x /etc/init.d/mongod

ADD run.sh /tmp/run.sh
RUN chmod u+x /tmp/run.sh

# start run!
CMD ["./tmp/run.sh"]
