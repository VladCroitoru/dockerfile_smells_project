FROM 1and1internet/ubuntu-16
MAINTAINER brian.wojtczak@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files/ /
# The chrome installation commands are commented out because we need to reintroduce them
# later date. Chrome is the browser of choice for the new version of watir, with Firefox
# not being fully supported. However running chrome in our infrastructure doesn't work
# at the moment. So we're sticking to an old version of watir and Firefox for the time
# being. At some point soon we will need to switch to Chrome.
RUN \
	cd /root && \
	#curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub --output google-chrome-gpg-key && \
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg --output docker-gpg-key && \
	curl -fsSL http://pub.pki.1and1.org/pukirootca1.crt --output pukirootca1.crt && \
	curl -fsSL http://pub.pki.1and1.org/pukiissuingca1.crt --output pukiissuingca1.crt && \
	curl -fsSL http://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip --output chromedriver_linux64.zip && \
	sha1sum -c sha1sums.txt && \
	#verify_gpg_key_fingerprint.sh /root/google-chrome-gpg-key 'EB4C 1BFD 4F04 2F6D DDCC  EC91 7721 F63B D38B 4796' && \
	verify_gpg_key_fingerprint.sh /root/docker-gpg-key '9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88' && \
	verify_x509_certificate_fingerprint.sh pukirootca1.crt "6B:DE:2B:46:BA:BF:52:1E:09:45:41:16:AE:CD:73:65:DE:79:EB:D9:49:FE:B3:9C:E9:F1:1C:2B:46:60:C0:CD" && \
	verify_x509_certificate_fingerprint.sh pukiissuingca1.crt "E1:99:91:7B:7F:DE:02:AF:00:AC:D0:65:0D:7B:E0:42:2A:A6:8E:E4:C1:53:BA:12:EF:15:3D:DB:62:A2:9A:DC" && \
	apt-get update -q && \
	apt-get install -y software-properties-common python-software-properties apt-transport-https openssl ca-certificates && \
	# apt-key add /root/google-chrome-gpg-key && \
	apt-key add /root/docker-gpg-key && \
	# add-apt-repository "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" && \
	add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
	apt-get update -q && \
	apt-get install -q -y build-essential make git wget unzip locales xvfb libav-tools && \
	# apt-get install -q -y chromium-chromedriver google-chrome-stable libnss3 libgconf-2-4 && \
	apt-get install -q -y firefox=45.0.2+build1-0ubuntu1 && \
	apt-get install -q -y docker-ce && \
	apt-get install -q -y ruby ruby-dev ruby-rspec ruby-test-unit ruby-ffi bundler rant && \
	apt-get install -q -y python-pkg-resources yamllint python-demjson jsonlint && \
	curl https://bootstrap.pypa.io/pip/3.5/get-pip.py -o get-pip.py && \
	python3 get-pip.py && \
	mkdir -p /usr/share/ca-certificates/1and1/ && \
	mv /root/pukirootca1.crt /usr/share/ca-certificates/1and1/ && \
	mv /root/pukiissuingca1.crt /usr/share/ca-certificates/1and1/ && \
	cd /usr/share/ca-certificates/ && \
	ls -1 1and1/* >>  /etc/ca-certificates.conf && \
	update-ca-certificates && \
	apt-get clean -q -y && \
	rm -rf /var/lib/apt/lists/* /root/sha1sums.txt /root/chromedriver_linux64.zip && \
	cd /root && \
	bundler
ENV TESTS_DIR=/tmp/tests
WORKDIR /mnt
CMD /bin/bash
