FROM ubuntu:trusty 

ENV FRAPPE_USER frappe
ENV ERPNEXT_APPS_JSON https://raw.githubusercontent.com/frappe/bench/master/install_scripts/erpnext-apps-master.json

RUN useradd $FRAPPE_USER \
 && mkdir /home/$FRAPPE_USER \
 && mkdir /home/$FRAPPE_USER/e-invoice \
 && chown -R $FRAPPE_USER.$FRAPPE_USER /home/$FRAPPE_USER

WORKDIR /home/$FRAPPE_USER

RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    sudo \
    cron \
    supervisor \
    npm

RUN wget https://raw.githubusercontent.com/frappe/bench/master/install_scripts/setup_frappe.sh \
 && bash setup_frappe.sh --setup-production

RUN apt-get -y remove build-essential \
    python-dev \
    python-software-properties \
    libmariadbclient-dev \
    libxslt1-dev \
    libcrypto++-dev \
    libssl-dev \
 && apt-get -y autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/ \
    /home/$FRAPPE_USER/.cache \
    /home/$FRAPPE_USER/*.deb

VOLUME ["/var/lib/mysql", "/home/frappe/frappe-bench/sites/site1.local/", "/home/frappe/e-invoice"]
COPY all.conf /etc/supervisor/conf.d/
EXPOSE 80 8000

CMD ["/usr/bin/supervisord", "-n"] 
