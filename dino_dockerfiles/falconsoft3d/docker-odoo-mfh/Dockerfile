FROM bmya/odoo:latest
MAINTAINER Blanco Martín & Asociados <daniel@blancomartin.cl>
# based on https://github.com/ingadhoc/docker-odoo-adhoc
# with custom references
# install some dependencies
USER root

# Generate locale (es_AR for right odoo es_AR language config, and C.UTF-8 for postgres and general locale data)
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && apt-get install -y locales -qq
RUN echo 'es_AR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen
RUN echo 'es_CL.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen
RUN echo 'es_US.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen
RUN echo 'C.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen
RUN dpkg-reconfigure locales && /usr/sbin/update-locale LANG=C.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8


# Install some deps
# adds slqalchemy
RUN apt-get update && apt-get install -y python-pip git vim
RUN apt-get install -y ghostscript  && \
    apt-get install -y python-gevent  && \
    apt-get install -y python-dev freetds-dev  && \
    apt-get install -y python-matplotlib font-manager  && \
    apt-get install -y swig libffi-dev libssl-dev python-m2crypto python-httplib2 mercurial  && \
    apt-get install -y libxml2-dev libxslt-dev python-dev lib32z1-dev liblz-dev  && \
    apt-get install -y swig libssl-dev  && \
    apt-get install -y libcups2-dev 

# 
RUN pip install urllib3
# RUN pip install sqlalchemy
# debug database version
# RUN pip install passlib

# letsencrypt dependencies:
RUN pip install acme-tiny
RUN sudo pip install IPy

# woocommerce dependency
RUN pip install woocommerce
RUN pip install magento




RUN pip install psycogreen

## Install pip dependencies for adhoc used odoo repositories
# 


# Freetds an pymssql added in conjunction
RUN pip install pymssql


RUN pip install geopy==0.95.1 BeautifulSoup pyOpenSSL suds cryptography certifi

# odoo bmya cambiado de orden (antes o despues de odoo argentina)

# to be removed when we remove crypto
RUN pip install suds

# Agregado por Daniel Blanco para ver si soluciona el problema de la falta de la biblioteca pysimplesoap
# RUN git clone https://github.com/pysimplesoap/pysimplesoap.git
# WORKDIR /pysimplesoap/
# RUN python setup.py install

# instala pyafip desde google code usando mercurial
# M2Crypto suponemos que no haria falta ahora
# RUN hg clone https://code.google.com/p/pyafipws
RUN git clone https://github.com/bmya/pyafipws.git
WORKDIR /pyafipws/
# ADD ./requirements.txt /pyafipws/
RUN pip install -r requirements.txt
RUN python setup.py install
RUN chmod 777 -R /usr/local/lib/python2.7/dist-packages/pyafipws/

# RUN git clone https://github.com/reingart/pyafipws.git
# WORKDIR /pyafipws/
# RUN python setup.py install
# RUN chmod 777 -R /usr/local/lib/python2.7/dist-packages/pyafipws/

# odoo etl, infra and others
RUN pip install openerp-client-lib fabric erppeek fabtools

# dte implementation
RUN pip install xmltodict
RUN pip install dicttoxml
RUN pip install elaphe
# RUN pip install hashlib
RUN pip install cchardet
RUN pip install lxml
RUN pip install signxml

#RUN pip install pysftp
RUN pip install pysftp==0.2.8

# oca reports
RUN pip install xlwt

# odoo kineses
RUN pip install xlrd

# create directories for repos
RUN mkdir -p /opt/odoo/stable-addons/oca
RUN mkdir -p /opt/odoo/stable-addons/bmya/odoo-chile
RUN mkdir -p /opt/odoo/.filelocal/odoo
RUN mkdir -p /var/lib/odoo/backups/synced

# update openerp-server.conf file (todo: edit with "sed")
COPY ./openerp-server.conf /etc/odoo/
RUN chown odoo /etc/odoo/openerp-server.conf
RUN chmod 644 /etc/odoo/openerp-server.conf
RUN chown -R odoo /opt/odoo
RUN chown -R odoo /opt/odoo/stable-addons
RUN chown -R odoo /mnt/extra-addons
RUN chown -R odoo /var/lib/odoo
# RUN chown -R odoo /mnt/filelocal/odoo

# oca partner contacts
RUN pip install unicodecsv

# aeroo direct print
RUN apt-get install -y libcups2-dev
RUN pip install git+https://github.com/aeroo/aeroolib.git@master
RUN pip install pycups==1.9.68

# akretion/odoo-usability
RUN pip install BeautifulSoup4

# OCA knowledge
RUN pip install python-magic

# l10n_cl_dte exclusive
# RUN apt-get -y install xmlsec1
# RUN apt-get -y install libxml2-dev libxmlsec1-dev
# RUN pip install dm.xmlsec.binding
RUN pip install SOAPpy
# RUN pip install fs

# odoo suspport
RUN pip install erppeek

# Instalación de repositorios varios BMyA
WORKDIR /opt/odoo/stable-addons/bmya/
# Eliminado para evitar la gran instalación de dependencias que tiene
# (Por ahora para tenerlo estable)
# RUN git clone https://github.com/bmya/addons-vauxoo.git

# Reemplaza a Odoo Addons
RUN git clone -b 8.0 https://github.com/bmya/sale.git
RUN git clone -b 8.0 https://github.com/bmya/product.git
RUN git clone -b 8.0 https://github.com/bmya/survey.git
RUN git clone -b 8.0 https://github.com/bmya/account-financial-tools.git
RUN git clone -b 8.0 https://github.com/bmya/partner.git
RUN git clone -b 8.0 https://github.com/bmya/stock.git
RUN git clone -b bmya_custom2 https://github.com/bmya/odoo-support.git
RUN git clone -b 8.0 https://github.com/bmya/project.git
RUN git clone -b 8.0 https://github.com/bmya/adhoc-project.git
RUN git clone -b 8.0 https://github.com/bmya/account-payment.git
RUN git clone -b 8.0 https://github.com/bmya/account-invoicing.git
RUN git clone -b 8.0 https://github.com/bmya/website.git
RUN git clone -b 8.0 https://github.com/bmya/odoo-web.git
RUN git clone -b 8.0 https://github.com/bmya/multi-company.git
RUN git clone -b 8.0 https://github.com/bmya/account-analytic.git
RUN git clone -b 8.0 https://github.com/bmya/purchase.git
RUN git clone -b 8.0 https://github.com/bmya/reporting-engine.git
RUN git clone -b 8.0 https://github.com/bmya/crm.git
RUN git clone -b 8.0 https://github.com/bmya/adhoc-crm.git
RUN git clone -b 8.0 https://github.com/bmya/miscellaneous.git
RUN git clone -b 8.0 https://github.com/bmya/surveyor.git
RUN git clone -b 8.0 https://github.com/bmya/odoo-logistic.git

# Modulos de OCA
RUN git clone -b 8.0 https://github.com/bmya/server-tools.git
RUN git clone -b 8.0 https://github.com/bmya/margin-analysis.git
RUN git clone -b 8.0 https://github.com/bmya/pos-addons.git
RUN git clone -b 8.0 https://github.com/bmya/pos.git

# Localización Argentina
RUN git clone -b 8.0 https://github.com/bmya/odoo-argentina.git

RUN git clone -b 8.0 https://github.com/bmya/odoo-bmya-cl.git

# Otras dependencias de BMyA
RUN git clone -b 8.0 https://github.com/bmya/odoo-bmya.git
RUN git clone -b 8.0 https://github.com/bmya/website-addons.git
# Otras (todo: revisar el tko porque hay módulos que no conviene instalar)
RUN git clone -b 8.0 https://github.com/bmya/odoo-single-adv.git
RUN git clone -b bmya_custom https://github.com/bmya/tkobr-addons.git tko
RUN git clone https://github.com/bmya/addons-yelizariev.git
RUN git clone https://github.com/bmya/ws-zilinkas.git

WORKDIR /opt/odoo/stable-addons/bmya/odoo-chile/
RUN git clone -b 8.0 https://github.com/odoo-chile/l10n_cl_vat.git
RUN git clone -b 8.0 https://github.com/odoo-chile/base_state_ubication.git
RUN git clone -b 8.0 https://github.com/odoo-chile/decimal_precision_currency.git
RUN git clone -b 8.0 https://github.com/odoo-chile/invoice_printed.git

WORKDIR /opt/odoo/stable-addons/oca/
RUN git clone -b 8.0 https://github.com/OCA/knowledge.git
RUN git clone -b 8.0 https://github.com/OCA/web.git
RUN git clone -b 8.0 https://github.com/OCA/bank-statement-reconcile.git
RUN git clone -b 8.0 https://github.com/OCA/account-invoicing.git
# MAGENTO
#RUN git clone -B 8.0 https://github.com/OCA/connector.git
RUN git clone -B 8.0 https://github.com/OCA/connector-ecommerce.git
RUN git clone -B 8.0 https://github.com/OCA/connector-magento.git
RUN git clone -B 8.0 https://github.com/OCA/e-commerce.git
RUN git clone -B 8.0 https://github.com/OCA/product-attribute.git
RUN git clone -B 8.0 https://github.com/OCA/sale-workflow.git

#Respaldos
RUN git clone -B 8.0 https://github.com/Yenthe666/auto_backup.git


RUN chown -R odoo:odoo /opt/odoo/stable-addons
WORKDIR /opt/odoo/stable-addons/
RUN git clone -b 8.0 https://github.com/aeroo/aeroo_reports.git

## Clean apt-get (copied from odoo)
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Make auto_install = False for various modules
# RUN sed  -i  "s/'auto_install': True/'auto_install': False/" /usr/lib/python2.7/dist-packages/openerp/addons/im_chat/__openerp__.py
RUN sed  -i  "s/'auto_install': True/'auto_install': False/" /usr/lib/python2.7/dist-packages/openerp/addons/im_odoo_support/__openerp__.py
RUN sed  -i  "s/'auto_install': True/'auto_install': False/" /usr/lib/python2.7/dist-packages/openerp/addons/bus/__openerp__.py
RUN sed  -i  "s/'auto_install': True/'auto_install': False/" /usr/lib/python2.7/dist-packages/openerp/addons/base_import/__openerp__.py
RUN sed  -i  "s/'auto_install': True/'auto_install': False/" /usr/lib/python2.7/dist-packages/openerp/addons/portal/__openerp__.py
# RUN sed  -i  "s/'auto_install': False/'auto_install': True/" /opt/odoo/stable-addons/bmya/addons-yelizariev/web_logo/__openerp__.py

# Change default aeroo host name to match docker name
RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/docs_client_lib.py
RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/installer.py
RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/report_aeroo.py

USER odoo
