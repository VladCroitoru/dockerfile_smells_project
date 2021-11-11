FROM ubuntu AS ssl

WORKDIR /opt/qnib/ssl/
RUN apt-get update \
 && apt-get install -y openssl
RUN openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem \
  -days 365 -nodes -subj "/C=DE/ST=Berlin/L=Berlin/O=QNIB Solutions/OU=IT Department/CN=qnib.org"

## Final image
FROM qnib/alplain-init

COPY --from=ssl /opt/qnib/ssl /opt/qnib/ssl
VOLUME ["/opt/qnib/ssl"]
LABEL org.qnib.havener.port.8080=""
# Instructs gosslterm to use volume-from when spining up container in network namespace
LABEL org.qnib.gosslterm.ssl.volume.from=true
# Defines the SSL directory for SSL termination
LABEL org.qnib.gosslterm.ssl.volume.path=/opt/qnib/ssl/

RUN apk --no-cache add curl wget jq \
 && wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.2.2/go-github_0.2.2_MuslLinux \
 && chmod +x /usr/local/bin/go-github \
 && echo "# go-httpcheck: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo go-httpcheck --regex '.*_Alpine' |head -n1)" \
 && wget -qO /usr/local/bin/go-httpcheck "$(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo go-httpcheck --regex '.*_Alpine' |head -n1)" \
 && chmod +x /usr/local/bin/go-httpcheck \
 && rm -f /usr/local/bin/go-github
HEALTHCHECK --interval=5s --retries=15 --timeout=2s \
  CMD /usr/local/bin/healthcheck.sh
COPY opt/qnib/entry/*.sh /opt/qnib/entry/
COPY opt/healthchecks/20-httpcheck.sh /opt/healthchecks/
CMD ["go-httpcheck"]
