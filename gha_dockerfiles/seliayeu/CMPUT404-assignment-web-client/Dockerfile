# this docker file describes the test environment for the assignment
FROM ubuntu:18.10
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-dev python3-setuptools python3-pip curl wget git vim 
RUN pip3 install django flask-sockets flask gunicorn
RUN echo -e '\n\n\n\n\n\n\n\n' | adduser --disabled-password --quiet me
RUN apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8     
USER me
WORKDIR /home/me
# This is how we get your tests to run (arbitrary shell scripts)
# ADD arb.sh /home/me/arb.sh
