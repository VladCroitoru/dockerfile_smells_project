FROM michilu/fedora-zero

WORKDIR /tmp
ENV \
  GOOGLE_APPENGINE="/google_appengine" \
  LC_CTYPE="en_US.utf8"

RUN yum install --quiet -y \
  findutils \
  git \
  make \
  npm \
  patch \
  python-devel \
  python-lxml \
  python-pip \
  ruby-devel \
  rubygem-bundler \
  unzip \
  which \
  && yum clean all

COPY Gemfile /tmp/Gemfile
RUN bundle install --quiet --jobs 4

COPY package.json /tmp/package.json
RUN npm install --silent --color false

COPY requirements.txt /tmp/requirements-gae.txt
RUN pip install --quiet -r requirements-gae.txt

COPY requirements.txt /tmp/requirements.txt
RUN pip install --quiet -r requirements.txt

COPY gae/tap/endpoints.patch /tmp/endpoints.patch
COPY gae/tap/docker.patch /tmp/docker.patch
COPY assets/fetch_google_appengine.sh /tmp/fetch_google_appengine.sh
RUN \
  /tmp/fetch_google_appengine.sh &&\
  unzip -q google_appengine.zip -d / &&\
  patch -d $GOOGLE_APPENGINE -p0 -i /tmp/endpoints.patch &&\
  patch -d $GOOGLE_APPENGINE -p0 -i /tmp/docker.patch &&\
  rm -rf /tmp/*
WORKDIR /home
