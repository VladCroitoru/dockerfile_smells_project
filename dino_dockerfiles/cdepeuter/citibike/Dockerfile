# our base image

# https://github.com/jupyter/docker-stacks/blob/master/pyspark-notebook/Dockerfile
# https://github.com/prakhar1989/FoodTrucks/blob/master/Dockerfile
# https://hub.docker.com/r/datagovsg/python-spark/~/dockerfile/
# https://github.com/CoorpAcademy/docker-pyspark/blob/master/Dockerfile



FROM ubuntu:16.04
MAINTAINER Conrad De Peuter <conrad.depeuter@gmail.com>


RUN apt-get -yqq update

# get python
RUN apt-get -yqq install python-pip python-dev



# get npm
RUN apt-get -yqq install nodejs npm
RUN ln -s /usr/bin/nodejs /usr/bin/node


ADD flask-app /opt/flask-app
WORKDIR /opt/flask-app


# fetch app specific deps
RUN npm install
RUN npm run build


RUN pip install  -r requirements.txt

# specify the port number the container should expose
EXPOSE 5000

# start app
CMD [ "python", "./app.py" ]