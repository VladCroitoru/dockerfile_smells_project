FROM paulflorea/python3-uwsgi-bower-grunt:latest

# Download and install wkhtmltopdf and xvfb to use wkhtmltopdf without X server
RUN apt-get install -y wkhtmltopdf xvfb

RUN echo '#!/bin/sh \n\
xvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf -q $*'\
> /usr/bin/wkhtmltopdf.sh

RUN chmod a+x /usr/bin/wkhtmltopdf.sh
RUN ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf