FROM 		ubuntu:15.10
MAINTAINER 	Trever Cullen "iamttc@umich.edu"

RUN			apt-get update -y &&\
			apt-get install -y python python-dev python-pip

COPY 		. /app
WORKDIR 	/app
RUN 		pip install -r requirements.txt

ENTRYPOINT 	["python"]
CMD 		["app.py"]
