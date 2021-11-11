FROM soulshake/aws.cli:latest

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y \
    ssh \
    curl \
    jq \
    bsdmainutils \
    pssh \
    python-pip \
    man \
    wkhtmltopdf

RUN pip install termcolor
RUN pip install PyYAML

#RUN pip install -U docker-compose
#COPY . /trainer-tools
#WORKDIR /trainer-tools
#ENTRYPOINT ["scripts/trainer-cli"]
# bind-mount /var/run/docker.sock socket
