FROM suchja/wine:latest
MAINTAINER Jan Suchotzki <jan@suchotzki.de>

# unfortunately we later need to wait on wineserver. Thus a small script for waiting is supplied.
USER root
COPY waitonprocess.sh /scripts/
RUN chmod +x /scripts/waitonprocess.sh

# wine should not be run as root!
USER xclient

# Install latest Enterprise Architect Lite version
RUN curl --show-error --location "http://www.sparxsystems.com.au/bin/EALite.exe" -o ealite.msi \
		&& wine msiexec /i ealite.msi /qn \
		&& /scripts/waitonprocess.sh wineserver \
		&& rm -f ealite.msi

RUN echo "alias ealite="\'"wine "\""C:\\\Program Files\\\Sparx Systems\\\EA LITE\\\EA.exe"\""'" > ~/.bash_aliases 

# get at least error information from wine
ENV WINEDEBUG -all,err+all

VOLUME /home/xclient/model
WORKDIR /home/xclient/model
