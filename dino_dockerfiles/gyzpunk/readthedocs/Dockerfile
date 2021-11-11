FROM python:2

MAINTAINER  gyzpunk "http://github.com/gyzpunk"

ENV RTD_PATH="/usr/src/app" \
	RTD_PRODUCTION_DOMAIN="localhost:8000" \
	RTD_SLUMBER_PASSWORD="docbuilder" \
	DJANGO_SETTINGS_MODULE="readthedocs.settings.sqlite"

# Install necessary system packages
RUN export DEBIAN_FRONTEND="noninteractive" \
	&& curl -sL https://deb.nodesource.com/setup_4.x | bash - \
	&& apt-get update && apt-get install --no-install-recommends -y \
		locales \
		unzip \
		libxml2-dev \
		libxslt1-dev \
		libevent-dev \
		build-essential \
		zlib1g-dev \
		doxygen \
		texlive-latex-base \
		texlive-fonts-recommended \
		doxygen-latex \
		dvipng \
		graphviz \
		nodejs \

	&& export LANGUAGE=en_US.UTF-8 \
	&& export LANG=en_US.UTF-8 \
	&& export LC_ALL=en_US.UTF-8 \
	&& locale-gen en_US.UTF-8 \
	&& dpkg-reconfigure locales \

	# Install modules for pdflatex
	&& for i in cmap fancybox titlesec framed fancyvrb threeparttable mdwtools wrapfig parskip upquote float multirow; do \
		curl -L -o /tmp/$i.zip http://mirrors.ctan.org/macros/latex/contrib/$i.zip && unzip -d /usr/share/texmf/tex/latex/ /tmp/$i.zip; \
	done \
	&& cd /usr/share/texmf/tex/latex/fancyvrb && latex fancyvrb.ins && cd - \
	&& cd /usr/share/texmf/tex/latex/float && latex float.ins && cd - \
	&& texhash \

	&& npm install -g bower gulp \

	# Install application
	&& mkdir -p ${APP_DATA_PATH} ${APP_LOGS_PATH} ${RTD_PATH} \
	&& cd ${RTD_PATH} \
	&& curl -L -o /tmp/rtfd.zip https://github.com/rtfd/readthedocs.org/archive/master.zip \
	&& unzip -d . /tmp/rtfd.zip && mv readthedocs.org-master/* . && rm -r readthedocs.org-master \
	&& pip install --no-cache-dir sphinx \
	&& pip install --no-cache-dir -r requirements.txt \

	# Clean up everything
	&& rm -rf /tmp/* \
	&& apt-get purge -y unzip \
	&& apt-get purge -y $(dpkg-query -f '${binary:Package} ' -W '*-doc') \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \

	# Create user
	&& groupadd -r rtfd \
	&& useradd -m -r -g rtfd rtfd

WORKDIR /${RTD_PATH}

COPY files/local_settings.py ./readthedocs/settings/
COPY files/rtfd-start.sh ./
RUN chown -R rtfd:rtfd .

USER rtfd

RUN npm install \
	&& bower install \
	&& gulp build \
	&& gulp vendor \
	&& chmod +x rtfd-start.sh

EXPOSE 8000
ENTRYPOINT ["./rtfd-start.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
