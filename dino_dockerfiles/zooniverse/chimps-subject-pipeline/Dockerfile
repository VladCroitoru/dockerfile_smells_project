FROM ubuntu:14.04

RUN apt-get update

RUN apt-get install -y ruby ruby-dev build-essential curl mysql-client \
        libmysqlclient-dev python-pip

RUN curl http://johnvansickle.com/ffmpeg/builds/ffmpeg-git-64bit-static.tar.xz \
        | tar -xvJ -C /usr/local/bin --strip-components=1 --wildcards \
            \*/ffprobe \*/ffmpeg

RUN gem install aws aws-sdk bson mimemagic mysql2 connection_pool
RUN pip install awscli
RUN aws configure set s3.signature_version s3v4

ADD . /opt/chimps/

WORKDIR /opt/chimps/

ENTRYPOINT [ "/usr/bin/ruby" ]
