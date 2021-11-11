# Trytond 3.2 with custom modules
#
# VERSION	3.2.0.1
 
FROM openlabs/tryton:3.2
MAINTAINER Nicolás Pace <nicolas.pace@unixono.com.ar>

RUN apt-get install -y swig git libssl-dev   # pyafipws dependency

# Setup the modules required for this setup
RUN pip install 'trytond_sale>=3.2,<3.3'
RUN pip install 'trytond_account>=3.2,<3.3'
# RUN pip install 'httplib2'
# RUN pip install 'm2crypto'
# RUN pip install 'git+https://github.com/reingart/pyafipws.git'
# RUN pip install 'git+https://github.com/tryton-ar/account_invoice_ar.git'
