FROM massimosiani/maven-angular-base
MAINTAINER Pierre Barnoux <pbarnoux@gmail.com>

# Additional dependencies required to run yo angular with default options
RUN apt-get update && apt-get install -y --no-install-recommends \
# post build configuration step of gifsicle-bin@3.0.1
	autoconf \
	automake \
# post build configuration step of optipng-bin@3.0.2
	zlib1g-dev

COPY "/root/*" "/root/"
COPY "/root/bin/*" "/root/bin/"

RUN useradd -c 'Non-root user' -m -d /home/myuser -s /bin/bash myuser
RUN chown -R myuser:myuser /root
USER myuser

ENTRYPOINT ["/bin/bash", "/root/setenv.sh"]
CMD ["/bin/bash"]

