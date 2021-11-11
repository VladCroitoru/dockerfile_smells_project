FROM fedora:22
RUN dnf -y update
RUN dnf install -y postgresql-server postgresql-contrib
RUN dnf install -y postgis
RUN dnf install -y npm
RUN dnf install -y tar
RUN dnf install -y make
RUN dnf install -y git
RUN dnf install -y wget
RUN dnf install -y spawn
RUN dnf install -y expect
RUN git clone https://github.com/ideal-postcodes/postcodes.io.git /root/postcodes
RUN cd /root/postcodes; npm install
ADD setup.sh /root/postcodes/setup.sh
RUN chmod +x /root/postcodes/setup.sh
RUN su postgres -c 'initdb -D /var/lib/pgsql/data'
RUN cd /root/postcodes; ./setup.sh
ADD run.sh /root/postcodes/run.sh
RUN chmod +x /root/postcodes/run.sh
CMD cd /root/postcodes; ./run.sh
EXPOSE 8000
