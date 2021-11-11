FROM qnib/uplain-init

RUN apt-get update \
 && apt-get install -y wget \
 && wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.2.2/go-github_0.2.2_Linux \
 && chmod +x /usr/local/bin/go-github \
 && echo "Download '$(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo qcollect-ng --regex "qcollect-ng.*" --limit 1)'" \
 && wget -qO /usr/local/bin/qcollect-ng $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo qcollect-ng --regex "qcollect-ng.*" --limit 1) \
 && chmod +x /usr/local/bin/qcollect-ng \
 && mkdir -p /opt/qcollect-ng/ \
 && echo "Download '$(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo qcollect-ng --regex "plugins.tar" --limit 1)'" \
 && wget -qO- $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo qcollect-ng --regex "plugins.tar" --limit 1) |tar xf - -C /opt/qcollect-ng/ \
 && apt-get purge -y wget \
 && apt-get autoclean \
 && rm -f /usr/local/bin/go-github

COPY resources/docker/qcollect-ng.yml /etc/
CMD ["qcollect-ng", "--config=/etc/qcollect-ng.yml", "--ld-path=/opt/qcollect-ng/lib/"]