From golang

MAINTAINER github.com/Milesfeng


RUN apt-get update -y && apt-get install -y git 

WORKDIR /

RUN git clone https://github.com/Milesfeng/go_chatroom.git

EXPOSE 5000 

CMD cd go_chatroom && go run .
