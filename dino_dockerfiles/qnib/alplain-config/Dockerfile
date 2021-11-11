FROM qnib/alplain-init:2017-11-06.v1

RUN wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.3.0/go-github_0.3.0_MuslLinux \
 && chmod +x /usr/local/bin/go-github \
 && echo "# confd: $(/usr/local/bin/go-github rLatestUrl --ghorg kelseyhightower --ghrepo confd --regex 'confd-[0-9\.]+-linux-amd64' --limit 1)" \
 && wget -qO /usr/local/bin/confd "$(/usr/local/bin/go-github rLatestUrl --ghorg kelseyhightower --ghrepo confd --regex 'confd-[0-9\.]+-linux-amd64' --limit 1)" \
 && chmod +x /usr/local/bin/confd \
 && echo "# go-fisherman: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo go-fisherman --regex '.*_Alpine' --limit 1)" \
 && wget -qO /usr/local/bin/go-fisherman "$(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo go-fisherman --regex '.*_Alpine' --limit 1)" \
 && chmod +x /usr/local/bin/go-fisherman
COPY opt/qnib/entry/20-confd.sh /opt/qnib/entry/
