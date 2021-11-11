FROM qnib/uplain-init


RUN apt-get update \
 && apt-get install -y wget vim \
 && wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.2.2/go-github_0.2.2_Linux \
 && chmod +x /usr/local/bin/go-github \
 && echo "# download: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo qwatch-static --regex '.*_Linux$' |head -n1)" \
 && wget -qO /usr/local/bin/qwatch $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo qwatch-static --regex=".*_Linux" |head -n1) \
 && chmod +x /usr/local/bin/qwatch \
 && apt-get purge -y wget \
 && rm -rf /usr/local/bin/go-github
COPY resources/qwatch-container.yml /etc/qwatch.yml
COPY resources/patterns/* /etc/qwatch/patterns/
CMD ["qwatch", "--config", "/etc/qwatch.yml"]
