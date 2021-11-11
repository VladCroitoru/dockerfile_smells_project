FROM vaultvulp/pipenv-ubuntu

MAINTAINER vaultvulp

# Installing packages
RUN pip install -U tox && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs && \
    npm install -g yarn
