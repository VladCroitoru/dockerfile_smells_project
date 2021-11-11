FROM centos/python-34-centos7

USER root

RUN yum install -y epel-release
#install ffmpeg
RUN rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
RUN rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
RUN yum install ffmpeg ffmpeg-devel -y

CMD ["ffmpeg", "-formats", ">", "./formats.txt"] # Don't know if piping in works like this in Docker CMD