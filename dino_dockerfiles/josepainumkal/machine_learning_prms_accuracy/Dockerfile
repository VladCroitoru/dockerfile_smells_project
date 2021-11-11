FROM josepainumkal/docker-pyspark
MAINTAINER Jose Painumkal
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


#copy source code

COPY . /regtool
WORKDIR /regtool
ENV PYTHONPATH /var/www/regtool
#install requirements

#RUN echo bakkas
RUN pip install -r requirements.txt

#RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN bower install --allow-root
#expose the app port

EXPOSE 5000
ENV RGTOOL_PORT 80
ENV RGTOOL_HOST 0.0.0.0
EXPOSE ${RGTOOL_PORT}
#run the app server

#ENTRYPOINT ["python"]

#CMD ["manage.py","runserver","-p","${VWADAPTOR_PORT}","-h","${VWADAPTOR_HOST}"]
CMD python views.py