# Sharelatex Community Edition (sharelatex/sharelatex)

FROM sharelatex/sharelatex-base:v1.0.0

ENV baseDir .

# Install sharelatex settings file
ADD ${baseDir}/settings.coffee /etc/sharelatex/settings.coffee
ENV SHARELATEX_CONFIG /etc/sharelatex/settings.coffee

# Install TexLive
RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz; \
	mkdir /install-tl-unx; \
	tar -xvf install-tl-unx.tar.gz -C /install-tl-unx --strip-components=1

RUN echo "selected_scheme scheme-basic" >> /install-tl-unx/texlive.profile; \
	/install-tl-unx/install-tl -profile /install-tl-unx/texlive.profile

RUN rm -r /install-tl-unx; \
	rm install-tl-unx.tar.gz

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/texlive/2016/bin/x86_64-linux/
RUN tlmgr install latexmk texcount beamer polski nag microtype scheme-full

RUN npm install -g grunt-cli

# Set up sharelatex user and home directory
RUN adduser --system --group --home /var/www/sharelatex --no-create-home sharelatex; \
	mkdir -p /var/lib/sharelatex; \
	chown www-data:www-data /var/lib/sharelatex; \
	mkdir -p /var/log/sharelatex; \
	chown www-data:www-data /var/log/sharelatex; \
	mkdir -p /var/lib/sharelatex/data/template_files; \
	chown www-data:www-data /var/lib/sharelatex/data/template_files;


ADD ${baseDir}/runit            /etc/service

RUN rm /etc/nginx/sites-enabled/default
ADD ${baseDir}/nginx/nginx.conf /etc/nginx/nginx.conf
ADD ${baseDir}/nginx/sharelatex.conf /etc/nginx/sites-enabled/sharelatex.conf

ADD ${baseDir}/logrotate/sharelatex /etc/logrotate.d/sharelatex

COPY ${baseDir}/init_scripts/  /etc/my_init.d/

# Install ShareLaTeX
RUN git clone https://git.iiet.pl/iiet/sharelatex.git /var/www/sharelatex #random_change

ADD ${baseDir}/services.js /var/www/sharelatex/config/services.js
ADD ${baseDir}/package.json /var/www/package.json
ADD ${baseDir}/git-revision.js /var/www/git-revision.js
RUN cd /var/www && npm install

RUN cd /var/www/sharelatex; \
	npm install; \
	grunt install; \
	cd web/modules; \
	git clone https://bitbucket.org/sharelatex/launchpad-webmodule.git launchpad; \
	grunt compile;

RUN cd /var/www && node git-revision > revisions.txt
	
# Minify js assets
RUN cd /var/www/sharelatex/web; \
	grunt compile:minify;

RUN cd /var/www/sharelatex/clsi; \
	grunt compile:bin

EXPOSE 80

WORKDIR /

ENTRYPOINT ["/sbin/my_init"]

