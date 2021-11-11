FROM danielperezr88/apache2-php-python3

MAINTAINER danielperezr88 <danielperezr88@gmail.com>

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

# Download Observatory
RUN curl -fSL "https://github.com/danielperezr88/ObservatorioHF/archive/v1.7.11.tar.gz" -o observatorio.tar.gz && \
	tar -xf observatorio.tar.gz -C . && \
	rm /var/www/html/* && \
	mv ObservatorioHF-1.7.11/* /var/www/html/ && \
	rm observatorio.tar.gz && \
	rm -rf ObservatorioHF-1.7.11 && \
	cp /var/www/html/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
	
# Download Unix Python Cron
RUN curl -fSL "https://github.com/danielperezr88/unixpythonservicelauncher/archive/v0.0.5.tar.gz" -o upservlaunch.tar.gz && \
	tar -xf upservlaunch.tar.gz -C . && \
	mkdir UnixPythonServiceLauncher && \
	mv unixpythonservicelauncher-0.0.5/* UnixPythonServiceLauncher/ && \
	rm upservlaunch.tar.gz && \
	chmod -R 755 UnixPythonServiceLauncher

# Download Script Gists and Setup Crontab for Python Cron
RUN curl -fSL "https://gist.githubusercontent.com/danielperezr88/45c9bc93c268758b2584babb48640db3/raw/ce82c038bde56e8a0019a0125249aba1137185e6/FreqCounterSvc.py" -o UnixPythonServiceLauncher/services/FreqCounterSvc.py && \
	curl -fSL "https://gist.githubusercontent.com/danielperezr88/81d22993957795668259cae3af65f555/raw/eea5e2990949e2de040f6d2c9bdfb811ccd2ce4b/HeartBeaterSvc.py" -o UnixPythonServiceLauncher/services/HeartBeaterSvc.py && \
	echo "*/5 * * * * HeartBeater" > UnixPythonServiceLauncher/services/serviceCron.tab && \
	echo "0 3 * * * FreqCounter" >> UnixPythonServiceLauncher/services/serviceCron.tab && \
	rm UnixPythonServiceLauncher/services/LogWriterSvc.py
	
RUN curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh -o install-logging-agent.sh && \
	echo "07ca6e522885b9696013aaddde48bf2675429e57081c70080a9a1364a411b395  install-logging-agent.sh" | sha256sum -c -
	
# Install main python packages
RUN pip install --upgrade pip && \
	pip install tweepy==3.5.0 && \
	pip install python-crontab && \
	pip install croniter && \
	pip install matplotlib && \
	pip install nltk

# Download and apply tweepy patch
RUN curl -fSL "https://gist.githubusercontent.com/danielperezr88/fe0c17e4e9039c815e9ca21508dd628b/raw/7fbbed4e4a04be0572c145012d5f9e9c7a1686e3/streaming.py" -o streaming.py && \
	cp streaming.py /usr/local/lib/python3.4/site-packages/tweepy/streaming.py && \
	rm streaming.py

EXPOSE 80
EXPOSE 443
EXPOSE 8888

CMD ["/usr/bin/supervisord"]
