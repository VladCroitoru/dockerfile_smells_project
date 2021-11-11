# Use the barebones version of Ruby 2.2.3.
FROM nawatt/rails-essentials:latest

# Optionally set a maintainer name to let people know who made this image.
MAINTAINER Muhammad Al-Syrwan <mhdsyrwan@gmail.com>

RUN apt-get install -yq libqtwebkit-dev --fix-missing --no-install-recommends

RUN curl -o /tmp/wkhtml2pdf.tar.xz http://download.gna.org/wkhtmltopdf/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz

RUN tar -C /tmp/ -xvf /tmp/wkhtml2pdf.tar.xz wkhtmltox

RUN cp -RT /tmp/wkhtmltox / && rm -fR /tmp/wkhtmltox
