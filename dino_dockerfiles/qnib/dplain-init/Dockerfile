FROM debian:9.3

#ENV LANG=en_US.UTF-8 \
#    LANGUAGE=en_US:en \
#    LC_ALL=en_US.UTF-8
RUN apt-get update \
 && apt-get install -y --no-install-recommends wget ca-certificates \
 && wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.3.0/go-github_0.3.0_Linux \
 && chmod +x /usr/local/bin/go-github \
 && echo "# init-plain: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo init-plain --regex 'init-plain.tar' --limit 1)" \
 && wget -qO - "$(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo init-plain --regex 'init-plain.tar' --limit 1)" |tar xf - --strip-components=1 -C / \
 && echo "Download: $(/usr/local/bin/go-github rLatestUrl --ghorg tianon --ghrepo gosu --regex 'gosu-amd64' --limit 1)" \
 && wget -qO /usr/local/bin/gosu $(/usr/local/bin/go-github rLatestUrl --ghorg tianon --ghrepo gosu --regex 'gosu-amd64' --limit 1) \
 && chmod +x /usr/local/bin/gosu \
 && echo "# go-fisherman: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo go-fisherman --regex '.*_x86' --limit 1)" \
 && wget -qO /usr/local/bin/go-fisherman "$(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo go-fisherman --regex '.*_x86' --limit 1)" \
 && chmod +x /usr/local/bin/go-fisherman \
 && apt-get purge -y wget ca-certificates libidn11 openssl \
 && rm -rf /var/lib/apt/lists/*
HEALTHCHECK --interval=5s --retries=5 --timeout=2s \
  CMD /usr/local/bin/healthcheck.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
