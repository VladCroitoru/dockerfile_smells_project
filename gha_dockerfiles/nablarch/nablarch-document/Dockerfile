FROM python:3.6.8
RUN apt-get update

# Sphinxのセットアップ
RUN pip install --upgrade pip && pip install Sphinx==1.6.3 && pip install javasphinx==0.9.15 && pip install sphinx-rtd-theme==0.2.4

# textlintのセットアップ
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs npm
COPY package*.json /root/
WORKDIR /root
RUN npm install && npm audit fix
RUN pip install docutils-ast-writer