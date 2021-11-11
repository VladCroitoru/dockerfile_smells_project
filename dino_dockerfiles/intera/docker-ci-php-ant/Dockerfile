FROM intera/ci-php:7.2-ubuntu

RUN apt-get update \
	&& apt-get dist-upgrade -y

RUN apt-get install -y \
	    gettext \
	    curl \
	    default-jdk \
	    ant \
	    mysql-client \
	    pdftk-java

RUN apt-get install -y ruby clang gcc make ruby-dev libffi-dev

RUN gem install compass --no-document

RUN apt-get -y purge clang gcc make ruby-dev libffi-dev \
    && apt-get --purge -y autoremove \
	&& apt-get autoclean \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*
