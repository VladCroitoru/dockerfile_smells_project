FROM        ubuntu:focal

RUN         useradd -r -d /var/lib/git/cucyber -s /sbin/nologin cucyber

RUN         apt-get -y update && \
            DEBIAN_FRONTEND=noninteractive apt-get install -y \
                nginx \
                webhook \
                git \
                make \
                curl \
                wget \
                rsync \
                python3 \
                python3-pandocfilters \
                pandoc \
                texlive-latex-extra \
                ruby-dev \
                gcc \
                g++ \
                zlib1g-dev && \
            gem install github-pages jekyll-github-metadata

COPY        ext /ext

CMD         /ext/bin/cucyber-init

EXPOSE      8000
