FROM openmatchmaking/docker-base-python-image:3.7
RUN apt-get update && apt-get -y install make

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY strategist /app
WORKDIR /app
