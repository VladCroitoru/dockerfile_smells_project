FROM odoo:9.0

USER root

RUN echo 'Rock n Roll'
# install dep
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
apt-get install -y apt-utils git python-setuptools && \
apt-get install -y python-genshi python-cairo python-lxml && \
apt-get install -y libreoffice-script-provider-python && \
apt-get install -y python3-uno python3-pip

RUN pip install simplejson xlrd
RUN pip3 install jsonrpc2 daemonize
RUN apt-get install -y libreoffice-writer libreoffice-calc xvfb openjdk-7-jre
RUN apt-get clean


RUN mkdir /opt/aeroo
RUN git clone https://github.com/aeroo/aeroolib.git /opt/aeroo/aeroolib
RUN git clone https://github.com/aeroo/aeroo_docs.git /opt/aeroo/aeroo_docs
WORKDIR /opt/aeroo/aeroolib
RUN python setup.py install

RUN echo Y | python3 /opt/aeroo/aeroo_docs/aeroo-docs start -c /etc/aeroo-docs.conf
RUN ln -s /opt/aeroo/aeroo_docs/aeroo-docs /etc/init.d/aeroo-docs

RUN update-rc.d aeroo-docs defaults
RUN echo 'start aeroo-docs service'
RUN service aeroo-docs start

RUN echo '#!/bin/sh' > /etc/init.d/office
RUN echo '/usr/bin/soffice --nologo --nofirststartwizard --headless --norestore --invisible "--accept=socket,host=localhost,port=8100,tcpNoDelay=1;urp;" &' >> /etc/init.d/office

RUN chmod +x /etc/init.d/office
RUN update-rc.d office defaults
RUN /etc/init.d/office restart
