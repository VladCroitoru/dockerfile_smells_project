FROM mono

RUN apt-get update && apt-get -y --no-install-recommends install wget unzip && \
    apt-get autoremove -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm -rf /var/lib/{apt,dpkg,cache,log}

RUN wget -O release.zip "$(curl -s https://api.github.com/repos/yar229/WebDavMailRuCloud/releases/latest | grep browser_download_url | grep Net45 | cut -d '"' -f 4)" && \
    unzip release.zip -d /src && \
    rm -rf release.zip

EXPOSE 801

CMD ["mono","/src/wdmrc.exe", "-h", "http://*"]
