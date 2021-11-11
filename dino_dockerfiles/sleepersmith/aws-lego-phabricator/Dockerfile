FROM nginx:1.8.1

ARG phabricator_hash=27006fedccc2f487dcaf7177f6d127ccd0e6df7d
ARG libphutil_hash=518dacd785fb19d67643e4a113e99b8825a87f99
ARG arcanist_hash=e7906e47cba2006fa46553d462abf1f685845f20

RUN apt-get update -q && \
    apt-get install -y -q unzip curl sudo && \
    apt-get install -y -q git mercurial subversion python-pygments dpkg-dev && \
    apt-get install -y -q php5 php5-mysql php5-gd php5-dev php5-curl php-apc php5-cli php5-json php5-fpm
	
RUN mkdir /home/local && mkdir /home/local/storage
WORKDIR /home/local

RUN curl -o phabricator.zip -J -L https://github.com/phacility/phabricator/archive/$phabricator_hash.zip && \
    unzip -q phabricator.zip && rm phabricator.zip && mv ./phabricator-$phabricator_hash/ ./phabricator/
RUN curl -o libphutil.zip -J -L https://github.com/phacility/libphutil/archive/$libphutil_hash.zip && \
    unzip -q libphutil.zip && rm libphutil.zip && mv ./libphutil-$libphutil_hash/ ./libphutil/
RUN curl -o arcanist.zip -J -L https://github.com/phacility/arcanist/archive/$arcanist_hash.zip && \
    unzip -q arcanist.zip && rm arcanist.zip && mv ./arcanist-$arcanist_hash/ ./arcanist/

ADD ./phabricator.conf /etc/nginx/conf.d/default.conf
ADD ./init.sh ./
ADD ./preamble.php /home/local/phabricator/support/

CMD ["/home/local/init.sh"]
