from php:7.0

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -yq \
    ant \
    build-essential \
    curl \
    git \
    libffi-dev \
    libssl-dev \
    net-tools \
    python-dev \
    python-setuptools \
    python-software-properties \
    sudo \
    unzip \
    zip \
    zlib1g-dev

RUN docker-php-ext-install pdo_mysql zip mbstring pcntl

# install node
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
RUN apt-get install nodejs -yq

# install composer
RUN curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer

# install pip
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-pip.py

# install ansible
RUN pip install --upgrade cffi cryptography ansible
