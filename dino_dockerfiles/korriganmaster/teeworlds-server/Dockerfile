FROM ubuntu:latest
MAINTAINER KorriganMaster <contact@korrigansoft.com>
ARG BUILD_DATE
ARG VCS_REF
LABEL 	com.korrigansoft.build-date=$BUILD_DATE \
		com.korrigansoft.docker.dockerfile="/Dockerfile" \
		com.korrigansoft.license="MIT" \
		com.korrigansoft.name="Teeworlds server Docker image" \
		com.korrigansoft.vcs-ref=$VCS_REF \
		com.korrigansoft.vcs-type="Git" \
		com.korrigansoft.vcs-url="https://github.com/KorriganMaster/teeworlds-server"
RUN apt-get update && apt-get install -y \
		teeworlds-server \
	&& rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/games/teeworlds-server /usr/local/bin/teeworlds-server
RUN useradd teeworlds --home /teeworlds --create-home
COPY ./entrypoint.sh /
RUN chmod a+x /entrypoint.sh
COPY ./serverconfig.cfg /teeworlds
RUN mkdir /teeworlds/datas
RUN chown -R teeworlds:teeworlds /teeworlds
USER teeworlds
WORKDIR /teeworlds
EXPOSE 8303/udp
ENTRYPOINT /entrypoint.sh