FROM		phusion/baseimage	
MAINTAINER	Rob Nelson <guruvan@maza.club>

EXPOSE		50001 50002 8000
VOLUME		["/home/maza","/var/tate-server"]
ENTRYPOINT	["/sbin/my_init"]

COPY		./app /app
COPY		./etc /etc
RUN		apt-get update \
		  && apt-get install -y \
		    apg python-dev python2.7 python-pip \
		    git libleveldb1 libleveldb-dev \
		  && echo "bitcoin hard nofile 65536" >> /etc/security/limits.conf \
     		  && echo "bitcoin soft nofile 65536" >> /etc/security/limits.conf \
		  && cd / \
		  && git clone https://github.com/mazaclub/tate-server /tate-server \
		  && cd /tate-server \
		  && python setup.py install \
                  && mv /tate-server/* /app \
		  && chmod +x /etc/service/tate-server/run \
		  && groupadd --gid 2211 maza \
		  && adduser --gid 2211 --disabled-password --gecos mazacoin --uid 2211 maza \
		  && rm -rf /etc/service/sshd
