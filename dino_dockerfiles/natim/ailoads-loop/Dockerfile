FROM python:3.4-wheezy
MAINTAINER Mozilla Cloud Services

RUN echo "deb http://ftp.debian.org/debian sid main" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-virtualenv
RUN apt-get install -y git
RUN apt-get install -y wget
RUN apt-get install -y python3-dev

# Adding loads user
RUN adduser --system loads
USER loads

# deploying the ailoads-loop project
RUN git clone https://github.com/tarekziade/ailoads-loop /home/loads/ailoads-loop
RUN cd /home/loads/ailoads-loop; make build

# run the test
CMD cd /home/loads/ailoads-loop; bin/ailoads -v -d $LOOP_DURATION -u $LOOP_NB_USERS
