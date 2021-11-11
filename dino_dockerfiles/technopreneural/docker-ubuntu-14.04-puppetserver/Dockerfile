FROM 		ubuntu:14.04
MAINTAINER	technopreneural@yahoo.com

		# Create volume to access puppet code from host
VOLUME		["/etc/puppetlabs/code/"]

EXPOSE		443 8140 8142 61613

#RUN		echo "acquire::http::proxy \"http://192.168.69.240:3142\";" > /etc/apt/apt.conf.d/02proxy

RUN		apt-get update \
		&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
			curl \

		# Install puppetlabs apt repository
		&& curl -O http://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb \
		&& dpkg -i puppetlabs-release-pc1-trusty.deb \
		&& rm puppetlabs-release-pc1-trusty.deb \

		# Install puppetserver
		&& apt-get update \
		&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
			puppetserver \

		# Reduce memory allocation to 512MB from 4GB default
		&& sed -i '/JAVA_ARGS=/s/\(-Xm[sx]\)2g/\1512m/g' /etc/default/puppetserver \

		# Cleanup
		&& rm -rf /var/lib/apt/lists/*

ENTRYPOINT	["/opt/puppetlabs/bin/puppetserver", "foreground"]
