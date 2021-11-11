
FROM python:2.7
MAINTAINER Olivier Fortin <olivier@fanslab.com>

RUN apt-get update && \
        apt-get install -y \
        build-essential \
        cmake \
        libgtk2.0-dev \
        pkg-config \
        python-dev \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        git \
        unzip


RUN pip install numpy

WORKDIR /
RUN wget https://github.com/opencv/opencv/archive/2.4.13.5.zip \
&& unzip 2.4.13.5.zip \
&& cd opencv-2.4.13.5 \
&& mkdir build \
&& cd build \
&& cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_NEW_PYTHON_SUPPORT=ON ..\
&& make \
&& make install \
&& rm /2.4.13.5.zip  \
&& rm -r /opencv-2.4.13.5


RUN pip install \
  alembic==0.9.1 \
  amqp==2.1.4 \
  aniso8601==1.2.0 \
  anyjson==0.3.3 \
  appdirs==1.4.3 \
  Babel==2.5.1 \
  billiard==3.5.0.2 \
  boto==2.46.1 \
  boto3==1.4.4 \
  botocore==1.5.20 \
  cachetools==2.0.0 \
  cairocffi==0.8.0 \
  CairoSVG==1.0.22 \
  celery==4.0.2 \
  cffi==1.9.1 \
  click==6.7 \
  coloredlogs==5.2 \
  coverage==4.3.4 \
  cssselect2==0.2.1 \
  cubes==1.1 \
  docutils==0.13.1 \
  dynamo3==0.4.10 \
  ecdsa==0.13 \
  enum34==1.1.6 \
  expressions==0.2.3 \
  Fabric==1.10.2 \
  facebook-sdk==2.0.0 \
  firebase-admin==2.0.0 \
  Flask==0.12.2 \
  Flask-Admin==1.4.2 \
  flask-admin-s3-upload==0.1.3 \
  Flask-Babel==0.11.2 \
  Flask-Cache==0.13.1 \
  Flask-Compress==1.4.0 \
  Flask-GraphQL==1.4.1 \
  Flask-JWT==0.3.2 \
  Flask-Limiter==0.9.3 \
  Flask-Login==0.4.0 \
  Flask-Migrate==2.0.3 \
  Flask-Moment==0.5.2 \
  Flask-OAuthlib==0.9.3 \
  Flask-RESTful==0.3.5 \
  Flask-Script==2.0.5 \
  Flask-SQLAlchemy==2.3.2 \
  Flask-Testing==0.6.2 \
  flask-thumbnails-s3==0.1.4 \
  Flask-WeasyPrint==0.5 \
  flywheel==0.5.2 \
  functools32==3.2.3.post2 \
  futures==3.0.5 \
  geopy==1.11.0 \
  google-auth==1.0.1 \
  grako==3.19.1 \
  graphene==1.4 \
  graphene-sqlalchemy==1.1.1 \
  graphql-core==1.1 \
  graphql-relay==0.4.5 \
  html2text==2017.10.4 \
  html5lib==0.999999999 \
  htmlmin==0.1.10 \
  humanfriendly==2.4 \
  idna==2.5 \
  ipaddress==1.0.18 \
  iso8601==0.1.11 \
  itsdangerous==0.24 \
  Jinja2==2.10 \
  jmespath==0.9.1 \
  jsonschema==2.6.0 \
  kombu==4.0.2 \
  limits==1.2.1 \
  Mako==1.0.6 \
  MarkupSafe==1.0 \
  mixpanel==4.3.2 \
  mixpanel-py-async==0.1.0 \
  monotonic==1.2 \
  mysql==0.0.1 \
  MySQL-python==1.2.5 \
  nose==1.3.7 \
  oauthlib==2.0.1 \
  olefile==0.44 \
  onesignal==0.1.3 \
  ordereddict==1.1 \
  packaging==16.8 \
  paramiko==1.15.3 \
  passlib==1.7.1 \
  pdfrw==0.4 \
  Pillow==4.1.1 \
  promise==2.0.2 \
  psycopg2==2.7 \
  py==1.4.34 \
  pyasn1==0.2.3 \
  pyasn1-modules==0.0.8 \
  pycparser==2.17 \
  pycrypto==2.6.1 \
  PyJWT==1.4.2 \
  pyparsing==2.2.0 \
  Pyphen==0.9.4 \
  pytest==3.2.2 \
  python-dateutil==2.6.0 \
  python-editor==1.0.3 \
  pytz==2017.3 \
  redis==2.10.5 \
  requests==2.12.1 \
  requests-oauthlib==0.8.0 \
  rsa==3.4.2 \
  s3-saver==0.1.3 \
  s3transfer==0.1.10 \
  singledispatch==3.4.0.3 \
  six==1.10.0 \
  speaklater==1.3 \
  SQLAlchemy==1.1.15 \
  SQLAlchemy-Utils==0.32.12 \
  tinycss2==0.6.1 \
  typing==3.6.1 \
  url-for-s3==0.1.1 \
  vine==1.1.3 \
  WeasyPrint==0.41 \
  webencodings==0.5.1 \
  Werkzeug==0.12.2 \
  WooCommerce==1.2.1 \
  WTForms==2.1 \
  xlrd==1.1.0 \
  xlwt==1.3.0

RUN pip install numpy  --upgrade --ignore-installed
RUN pip install raven[flask] nose2 coverage
