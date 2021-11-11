FROM ubuntu:14.04
EXPOSE 5000
MAINTAINER Chet Carello "cpuskarz@cisco.com"

VOLUME ["/app/data"]

# Install basic utilities
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install setuptools wheel

ADD . /app
WORKDIR /app
RUN pip install -r  requirements.txt

#ARG DATA_SERVER="http://192.168.99.100:32810"

CMD ["python", "mydrummer_app.py"]


# Below are just notes for work in progress
#ENTRYPOINT ["python"]
#CMD ["export DATA_SERVER=http://192.168.99.100:32810"]
#CMD ["mydrummer_app.py", "--dataserver=$DATA_SERVER"]
#CMD ["mydrummer_app.py, --dataserver=http://192.168.99.100:32819"]
#CMD ["mydrummer_app.py", "--dataserver=",$DATA_SERVER]
#CMD ["mydrummer_app.py --dataserver=DATA_SERVER"]

# NOTES -------------------
# this works
#CMD ["mydrummer_app.py", "--dataserver=http://192.168.99.100:32819"]

# this works from command line:
#docker run -it -P --name=drum_app1bb drum_app1bb mydrummer_app.py --dataserver="http://192.168.99.100:32819"

# this also works if DB is global before running:
#docker run -it -P --name=drum_app1bb drum_app1bb mydrummer_app.py --dataserver=$DB
# so how do I get $DB into Dockerfile at build?

# Below ENV shows up in global envs once the container is booted. How do I get CMD to see this?
#ENV DB_SERVER "http://192.168.99.100:32819"
