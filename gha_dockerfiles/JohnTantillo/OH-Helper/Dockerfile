# FROM ubuntu:18.04
FROM python:3

RUN apt-get update
# Set the home directory to /root
ENV HOME /root
# cd into the home directory
WORKDIR /root

COPY . .

# RUN pip install pymongo

#this was made using the resouces found at https://hub.docker.com/_/python
# RUN pip install pystrich

# RUN apt-get update --fix-missing
RUN pip install boto
RUN pip install -r requirements.txt

EXPOSE $PORT

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait
CMD /wait && python app.py $PORT

