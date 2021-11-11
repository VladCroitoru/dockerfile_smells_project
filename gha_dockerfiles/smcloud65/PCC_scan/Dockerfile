FROM ubuntu:16.04

#LABEL version="1.1"
LABEL description="Test with Labels & Env Variables in Image"
LABEL deployment="dev"

ENV MYSQL_HOST="DB_Server"
ENV MYSQL_USER="operations"
ENV MYSQL_PASSWORD="5TTnvuTDJJSq6"

RUN apt-get update   && \
    # apt-get -y upgrade   && \
    apt-get -y install openssl shellinabox ca-certificates iputils-ping wget curl telnet sudo && \
    adduser lab --gecos "Me,Office,WorkPhone,HomePhone" --disabled-password  && \
    echo 'lab:$6$88GqT260$I8mtFOPBqCSeDWUdDcWBV0oDR1c2NAbg7WFh/6n6cb60sWdXhLJDQ6ELEAIErDr2p5syvVZkcsualGt4pC8Es1' | chpasswd --encrypted  && \
    apt-get clean 

EXPOSE 4200

ENTRYPOINT ["shellinaboxd", "-s", "/:LOGIN", "--disable-ssl"]







