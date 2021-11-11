FROM rhub/r-minimal

RUN installr -d -t "bash openssl-dev libgit2-dev" -a "openssl libgit2" gert gh remotes

COPY rebuilds /pkg
COPY entrypoint.sh /entrypoint.sh

RUN R -e 'remotes::install_local("/pkg")'

ENTRYPOINT ["sh","/entrypoint.sh"]
