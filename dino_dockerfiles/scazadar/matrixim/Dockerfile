FROM		ubuntu
RUN		apt update && \
		apt install -y build-essential python2.7-dev \ 
		libffi-dev python-pip python-setuptools sqlite3 \
		libssl-dev libjpeg-dev libxslt1-dev
RUN		pip install --upgrade pip && \
		pip install --upgrade setuptools && \
		pip install https://github.com/matrix-org/synapse/tarball/master
COPY		./entrypoint.sh /entrypoint.sh
COPY		./register_new_user.sh /register_new_user.sh
ENTRYPOINT	["/entrypoint.sh"]
