FROM ubuntu:15.10
MAINTAINER Aaron Herres <iam@aaronherres.com>

RUN apt-get update && apt-get install nano -y

RUN apt-get install -y chrony

CMD ["chronyd", "-d"]
