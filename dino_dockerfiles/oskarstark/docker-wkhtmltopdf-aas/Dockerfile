FROM ubuntu:18.04

MAINTAINER Oskar STARK <oskarstark@googlemail.com>

RUN sed 's/main$/main universe/' -i /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
                                   apt-get upgrade -y

# Download and install wkhtmltopdf
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install wget xz-utils libxrender1 libfontconfig1 libxext6 python-pip fontconfig libjpeg-turbo8 xfonts-75dpi xfonts-base && \
    wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb && \
    dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb

# Cleanup
RUN rm -rf wkhtmltox_0.12.5-1.bionic_amd64.deb
RUN DEBIAN_FRONTEND=noninteractive apt-get -y remove wget xz-utils && \
                                   apt-get -y autoremove && \
                                   apt-get -y clean

RUN pip install werkzeug executor gunicorn

ADD app.py /app.py
EXPOSE 80

ENTRYPOINT ["usr/local/bin/gunicorn"]

# Show the extended help
CMD ["-b", "0.0.0.0:80", "--log-file", "-", "app:application"]
