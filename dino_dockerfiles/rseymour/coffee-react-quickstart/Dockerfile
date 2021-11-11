FROM ubuntu
ENV PYTHONUNBUFFERED 1
RUN apt-get update -qq
RUN apt-get install -y python-software-properties python g++ make software-properties-common
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get install -y nodejs bundler ruby git
ADD mounted.sh /mnt.sh
RUN chmod 755 /mnt.sh
CMD bash /mnt.sh 
