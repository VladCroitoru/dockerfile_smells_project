FROM frolvlad/alpine-python3
MAINTAINER Quint Guvernator <quint@guvernator.net>

# to allow us to install (signed) dependencies
RUN pip3 install --upgrade pip
RUN pip3 install certifi

# install dependencies
RUN pip3 install googlemaps flask Flask-Moment

# add the project to the container
RUN mkdir -p /srv/lastcall
WORKDIR /srv/lastcall
ADD src .

# run the project
EXPOSE 80
CMD ["python3", "webapp.py"]
