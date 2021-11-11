FROM		ubuntu:14.04
MAINTAINER	technopreneural@yahoo.com

# Create volume for data
# NOTE: use "docker run -v <folder_path>:<volume>..." to bind volume to host folder
VOLUME		["/var/lib/mysql/", "/var/log/mysql/"]

# Expose port 3306 (MySQL) to other containers
# NOTE: use "docker run -p 3306:3306..." to map port to host
EXPOSE  	3306

# Enable (or disable) apt-cache proxy
#ENV		http_proxy http://192.168.69.240:3142

# Install package(s) 
RUN		apt-get update \
		&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
			mysql-server \

# Delete downloaded data afterwards to reduce image footprint
		&& rm -rf /var/lib/apt/lists/* \

# Remove warnings
		&& sed -i '/^\(key_buffer\)\([\w\t]*=\)/s//\1_size\2/' /etc/mysql/my.cnf \
		&& sed -i '/^\(myisam-recover\)\([\w\t]*=\)/s//\1-options\2/' /etc/mysql/my.cnf \

# Allow connection from all interfaces
# NOTE: the effect of the line above should be equivalent to that of the line below
#		sed -i "s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
		&& sed -i "s/^bind-address/#bind-address/" /etc/mysql/my.cnf

ENV		PASSWORD=root \
		USER=mysql \
		RUNDIR=/run/mysql \
		LOGDIR=/var/log/mysql \
		DATADIR=/var/lib/mysql \
		PORT=3306 \
		INIT=0

COPY		run.sh /root/run.sh

ENTRYPOINT	["/root/run.sh"]
