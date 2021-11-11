FROM        ubuntu

MAINTAINER  serverwentdown

RUN         apt-get update \
            && apt-get install -y openssl wget zip unzip tar xz-utils gzip openssh-client git xvfb libxrender1 fontconfig \
            && wget -O /tmp/wkhtmltox.tar.xz https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
            && tar -C /usr/local --strip-components 1 -xvf /tmp/wkhtmltox.tar.xz \
            && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD         ["/bin/bash"]
