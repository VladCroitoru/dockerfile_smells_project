FROM virtualwatershed/vw-py
MAINTAINER Jose Painumkal

LABEL description="This Image builds an ubuntu 14.04 image from vw-py:1.0 and installs the dependencies of vw-webapp." \
      version="1.0"

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python-pip python-dev build-essential \
    git wget curl unzip m4 openssh-client
RUN apt-get install -y libncurses5-dev
RUN apt-get update -y && apt-get install -y libpq-dev libssl-dev libffi-dev
# install nodejs
RUN curl -sL https://deb.nodesource.com/setup_4.x | sh -
RUN apt-get install -y nodejs
RUN npm install -g bower
RUN apt-get install sshpass
RUN apt-get install -y python-matplotlib
RUN apt-get install -y vim

# install docker client to run docker commands inside container
#RUN apt-get install -y docker.io
RUN wget -qO- https://get.docker.com/ | sh


# copy source code
COPY . /var/www/taskmanager
WORKDIR /var/www/taskmanager
ENV PYTHONPATH /var/www/taskmanager

# install requirements
#RUN echo bakkas

RUN pip install -U pip setuptools
RUN pip install -r requirements.txt


RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN bower install

# expose the app port
#EXPOSE 5001
ENV VWTOOLS_PORT 80
ENV VWTOOLS_HOST 0.0.0.0
EXPOSE ${VWTOOLS_PORT}
# run the app server
#ENTRYPOINT ["python"]
#CMD ["manage.py","runserver","-p","${VWADAPTOR_PORT}","-h","${VWADAPTOR_HOST}"]
CMD python manage.py runserver -p ${VWTOOLS_PORT} -h ${VWTOOLS_HOST}
