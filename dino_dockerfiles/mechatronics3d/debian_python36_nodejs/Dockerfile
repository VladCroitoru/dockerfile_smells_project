# Copyright (c) 2012-2016 Codenvy, S.A.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
# Contributors:
# Codenvy, S.A. - initial API and implementation
# Modified by Behzad Samadi to add python3.6

FROM python:3.6-jessie
    
RUN apt-get update && \
    apt-get -y install build-essential libkrb5-dev gcc make ruby-full rubygems debian-keyring && \
    gem install --no-rdoc --no-ri sass -v 3.4.22 && \
    gem install --no-rdoc --no-ri compass && \
    apt-get clean && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* 

RUN wget -qO- https://deb.nodesource.com/setup_7.x | bash -
RUN apt update && apt -y install nodejs

EXPOSE 5000 8080
RUN npm install --unsafe-perm -g gulp bower grunt grunt-cli yeoman-generator yo generator-angular generator-karma generator-webapp

WORKDIR /projects

LABEL che:server:8080:ref=vue che:server:8080:protocol=http che:server:5000:ref=flask che:server:5000:protocol=http
