FROM nelsonramirezs/odoo8:latest
MAINTAINER Nelson Ramirez <info@konos.cl>
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
RUN apt-get update && apt-get install -y python-pip \
                                         git vim mercurial \
                                         ghostscript \
										 python-gevent \
										 python-dev \
										 freetds-dev \
										 python-matplotlib \
										 font-manager \
										 swig \
										 libffi-dev \
										 libssl-dev \
										 python-m2crypto \
										 python-httplib2 \
										 libxml2-dev \
										 libxslt-dev \
										 python-dev \
										 lib32z1-dev \
										 liblz-dev \
										 libcups2-dev \
										 libssl-dev libxml2-dev libxmlsec1-dev pkg-config

WORKDIR /
ADD ./requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN git clone https://github.com/bmya/pyafipws-1.git /pyafipws/
WORKDIR /pyafipws/

# ADD ./requirements.txt /pyafipws/
RUN python setup.py install
RUN chmod -R 777 /usr/local/lib/python2.7/dist-packages/PyAfipWs-2.7.0-py2.7.egg

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

WORKDIR /opt/odoo/stable-addons/bmya/

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
RUN git clone -b 8.0 https://github.com/OCA/connector.git
RUN git clone -b 8.0 https://github.com/OCA/connector-ecommerce.git
RUN git clone -b 8.0 https://github.com/OCA/connector-magento.git
RUN git clone -b 8.0 https://github.com/OCA/e-commerce.git
RUN git clone -b 8.0 https://github.com/OCA/product-attribute.git
RUN git clone -b 8.0 https://github.com/OCA/sale-workflow.git


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
# RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/docs_client_lib.py
RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/*.py
# RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/installer.py
# RUN sed  -i  "s/localhost/aeroo/" /opt/odoo/stable-addons/aeroo_reports/report_aeroo/report_aeroo.py

USER odoo
