FROM ubuntu

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >> /etc/apt/sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-updates multiverse" >> /etc/apt/sources.list

# 先更新apt-get
RUN apt-get update && apt-get upgrade -y

# 安装python3
RUN apt-get install python3 -y

# 安装FFmpeg
RUN apt-get install ffmpeg -y

# 安装bottle
RUN apt-get install python3-pip -y
RUN pip3 install bottle

# 安装you-get-web
RUN rm -Rf /var/you-get

RUN apt-get install git -y
RUN git clone https://github.com/demoshow/you-get.git  /var/you-get

WORKDIR /var/you-get
VOLUME /var/you-get

RUN python3 setup.py install

EXPOSE 8080

CMD sudo python3 you-get-web
