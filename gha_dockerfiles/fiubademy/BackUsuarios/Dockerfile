FROM ubuntu
RUN apt-get -y update 
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
COPY Commands.sh /app/
COPY src/service/. /app/
CMD ./Commands.sh

