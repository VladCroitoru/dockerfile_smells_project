FROM vladus2000/rutorrent
MAINTAINER vladus2000 <docker@matt.land>

COPY shiz/ /home/evil/shiz/

RUN \
	/install-devel.sh && \
	su - evil -c 'yay -S --needed --noconfirm pyinstaller python2-setuptools flac lame mp3gain sox vorbis-tools vorbisgain whatmp3 jackett-bin wget rsync unzip p7zip zip openssh rar libglvnd ffmpeg radarr sonarr su-exec mylar3 pymedusa par2cmdline nzbget streamlink-git' && \
	pip uninstall --no-input --yes twisted && \
	pip uninstall --no-input --yes automat && \
	pip uninstall --no-input --yes pytest && \
	pip install --no-input -r /usr/lib/pymedusa/requirements.txt && \
	chown -R evil:evil ~evil/shiz && \
	cp ~evil/shiz/*.sh / && \
	cp ~evil/shiz/nzbget.conf /config && \
	chmod +x /*.sh && \
	rm -rf /var/lib/{jackett,radarr,sonarr,mylar,pymedusa} && \
	su - evil -c 'mkdir -p /config/{jackett,radarr,sonarr,mylar,pymedusa}' && \
	ln -s /config/jackett /var/lib/jackett && \
	ln -s /config/radarr /var/lib/radarr && \
	ln -s /config/sonarr /var/lib/sonarr && \
	ln -s /config/mylar /var/lib/mylar && \
	ln -s /config/pymedusa /var/lib/pymedusa && \
	ln -s /config/nzbget.conf ~evil/.nzbget && \
	/rm-devel.sh

# for rutorrent (via nginx)
EXPOSE 8069
# for rtorrent
EXPOSE 49152

CMD /bin/bash -c /startup.sh

VOLUME /config
VOLUME /downloads

