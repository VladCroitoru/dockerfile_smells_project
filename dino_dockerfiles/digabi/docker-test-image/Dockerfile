FROM debian:stretch

RUN apt-get update && \
    apt-get -y install gnupg jq ca-certificates cmake curl g++ gcc git libx11-dev libffi-dev libnss3-tools locales make bsdtar latexmk texlive-latex-recommended texlive-latex-extra\
    texlive texlive-lang-european texlive-fonts-recommended texlive-fonts-extra netcat-traditional ruby ruby-dev sudo libsystemd-dev && \
    curl 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | apt-key add - && \
    echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/chrome.list && \
    echo 'deb http://deb.debian.org/debian stretch-backports main' > /etc/apt/sources.list.d/stretch-backports.list && \
    apt-get update && \
    apt-get -y install google-chrome-unstable postgresql-9.6 postgresql-contrib-9.6 postgresql-server-dev-9.6 && \
    apt-get -y install -t stretch-backports golang && \
    rm -rf /var/lib/apt/lists/* && \
    echo 'fi_FI.UTF-8 UTF-8' > /etc/locale.gen && \
    locale-gen && \
    ln -sf /usr/share/zoneinfo/Europe/Helsinki /etc/localtime && \
    sed -i 's/md5/trust/' /etc/postgresql/9.6/main/pg_hba.conf && \
    echo "TimeZone = 'Europe/Helsinki'" >> /etc/postgresql/9.6/main/postgresql.conf && \
    pg_ctlcluster 9.6 main start && \
    sudo -u postgres psql -c 'CREATE USER digabi WITH SUPERUSER;' && \
    pg_ctlcluster 9.6 main stop && \
    adduser --system --uid 1001 digabi && \
    curl https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | sudo -u digabi bash && \
    sudo -u digabi bash -c 'cd ; . ~/.nvm/nvm.sh; for v in 8.11.3 8.17.0 10.17.0 12.4.0 12.6.0 12.7.0 12.8.0 12.14.0 14.16.0; do nvm install $v; nvm exec $v npm install -g yarn; done' && \
    gem install fpm
