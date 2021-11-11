FROM		logstash:5.1.1
MAINTAINER	phirov@163.com

RUN		echo "alias ls='ls --color=auto'" >> $HOME/.bashrc && \
		#
		# install crontab, but the cron service should be started manually
		# install supervisor
		apt-get update && \
		apt-get install -y cron supervisor python-pip && \
		mkdir -p /var/log/supervisor && \
		#
		# install additional offical plugins but not installed in standard release
		#echo 'gem "logstash-output-mongodb"' >> /usr/share/logstash/Gemfile && \
		logstash-plugin install logstash-output-mongodb && \
		#./bin/logstash-plugin install logstash-filter-environment && \
		#
		# prepare for my patched plugin
		# use buildin jruby && gem to install new plugin
                echo 'PATH=/usr/share/logstash/vendor/jruby/bin:/usr/share/logstash/vendor/bundle/jruby/1.9/bin/:$PATH' >> $HOME/.bashrc && \
                export PATH=/usr/share/logstash/vendor/jruby/bin:/usr/share/logstash/vendor/bundle/jruby/1.9/bin/:$PATH && \
		mkdir -p /opt/logstash/src && \
		#
		# input-s3: v3.1.1-p1
		wget -P /opt/logstash https://github.com/phirov/logstash-input-s3/archive/v3.1.2.tar.gz && \
		cd /opt/logstash && \
		tar xzf v3.1.2.tar.gz && \
		cd /usr/share/logstash && \
		sed -i 's/gem "logstash-input-s3"/gem "logstash-input-s3", :path => "\/opt\/logstash\/logstash-input-s3-3.1.2"/g' Gemfile && \
		gem build /opt/logstash/logstash-input-s3-3.1.2/logstash-input-s3.gemspec && \
		#
		# filter-environment: v3.0.0-p1
		cd /opt/logstash && \
		wget -O src/logstash-filter-environment-3.0.0-p1.tar.gz https://github.com/phirov/logstash-filter-environment/archive/v3.0.0-p1.tar.gz && \
		tar xzf src/logstash-filter-environment-3.0.0-p1.tar.gz && \
		cd /usr/share/logstash && \
		echo 'gem "logstash-filter-environment", :path => "/opt/logstash/logstash-filter-environment-3.0.0-p1"' >> Gemfile && \
		#sed -i 's/gem "logstash-filter-environment"/gem "logstash-filter-environment", :path => "\/opt\/logstash\/logstash-filter-environment-3.0.0-p1"/g' Gemfile && \
		gem build /opt/logstash/logstash-filter-environment-3.0.0-p1/logstash-filter-environment.gemspec && \
		#
		# final install all patched plugin
		./bin/logstash-plugin install --no-verify
		#./bin/logstash-plugin update --no-verify
		#./bin/logstash-plugin install logstash-filter-environment

ENTRYPOINT	["/docker-entrypoint.sh"]
CMD		["-e", ""]
