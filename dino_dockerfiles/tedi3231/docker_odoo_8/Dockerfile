FROM odoo:8.0
MAINTAINER Odoo S.A. <info@odoo.com>
#Set default user when running the container
USER root
RUN set -x; \
         curl -o xlrd.deb -SL http://ftp.cn.debian.org/debian/pool/main/p/python-xlrd/python-xlrd_0.9.4-1_all.deb \
                  && dpkg --force-depends -i xlrd.deb
                  RUN chown -R odoo /var/lib/odoo
                  RUN mkdir -p /var/lib/odoo/.fonts
                  RUN chown -R odoo:odoo /var/lib/odoo
                  USER odoo
                  ADD wqy-microhei.ttc /var/lib/odoo/.fonts/
