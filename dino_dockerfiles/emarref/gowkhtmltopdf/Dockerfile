FROM golang:1.6-onbuild

RUN cd /tmp

# Install dependencies. Make a cuppa.
RUN apt-get update \
    && apt-get install -y build-essential xorg libssl-dev libxrender-dev wget gdebi xz-utils

# Download and install wkhtmltopdf
RUN wget http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
RUN tar xvfJ wkhtmltox-0.12.3_linux-generic-amd64.tar.xz -C /usr/share/wkhtmltopdf
RUN cp /usr/share/wkhtmltopdf/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf \
    && cp /usr/share/wkhtmltopdf/bin/wkhtmltoimage /usr/local/bin/wkhtmltoimage
