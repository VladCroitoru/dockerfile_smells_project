FROM nginx:1.13.0

EXPOSE 8080

ADD nginx.conf /etc/nginx/nginx.conf
RUN apt-get update && apt-get install -y unzip wget && mkdir /usr/share/nginx/html/data

RUN wget -O /usr/share/nginx/html/data/libreoffice-calc-kan.zip "https://www.dropbox.com/s/8cp96e91vmbujim/libreoffice-calc-kan.zip?dl=1" && \
    unzip /usr/share/nginx/html/data/libreoffice-calc-kan.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/libreoffice-calc-kan.zip;
