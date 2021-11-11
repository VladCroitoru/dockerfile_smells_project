FROM ubuntu

RUN apt-get -y update\
&& apt-get -y upgrade\
&& apt-get -y install nginx\
&& apt-get -y clean

COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

WORKDIR /root
