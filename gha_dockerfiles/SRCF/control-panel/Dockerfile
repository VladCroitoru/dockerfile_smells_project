FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
	apt-get install --quiet --yes --no-install-recommends software-properties-common && \
	add-apt-repository ppa:malcscott/python-ucam-webauth && \
	apt-get update && \
	apt-get install --quiet --yes --no-install-recommends python3-flask python3-flask-sqlalchemy python3-ucam-webauth python3-yaml && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# python-srcf dependencies
# (Self-contained stanza to aid in deletion when python-srcf gets PPA-ed)
RUN apt-get update && \
	apt-get install --quiet --yes --no-install-recommends python3-six python3-psycopg2 python3-ldap3 python3-pymysql python3-sqlalchemy && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# srcflib dependencies
# (Self-contained stanza to aid in deletion when python-srcf gets PPA-ed)
RUN apt-get update && \
	apt-get install --quiet --yes --no-install-recommends python3-requests python3-pylibacl && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# flask_talisman and srcflib and srcf
RUN apt-get update && \
	apt-get install --quiet --yes --no-install-recommends python3-pip && \
	apt-get install --quiet --yes --no-install-recommends git python3-setuptools && \
	pip3 install git+https://github.com/srcf/srcflib && \
	pip3 install git+https://github.com/srcf/srcf-python && \
	pip3 install flask_talisman && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

COPY pubkey2 /etc/apache2/ucam_webauth_keys/pubkey2
COPY pubkey500 /etc/apache2/ucam_webauth_keys/pubkey500

WORKDIR /opt/srcf/control

COPY . .

EXPOSE 5000

CMD ["python3", "run.py"]
