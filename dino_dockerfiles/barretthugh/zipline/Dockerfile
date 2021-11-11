FROM python:3.5.2

ENV TZ=Asia/Shanghai


COPY requirement.txt /requirement.txt
#COPY pip.conf /root/.pip/pip.conf 				for mirror in China
#COPY source.list /etc/apt/sources.list			for mirror in China
COPY jupyter_notebook_config.py /root/.jupyter/


RUN apt-get update \
	&& yes | apt-get install libatlas-base-dev gfortran pkg-config libfreetype6-dev unzip \
	&& wget https://downloads.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz \
	&& tar xvf ta-lib-0.4.0-src.tar.gz \
	&& cd ta-lib \
	&& ./configure --prefix=/usr \
	&& make \
	&& make install \
	&& cd .. \
	&& rm -rf ta-lib \
	&& rm ta-lib-0.4.0-src.tar.gz \
	&& pip install -r /requirement.txt \
	&& pip install Tushare \
	&& pip install -U setuptools \
	&& pip install zipline \
	&& curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb \
	&& dpkg -i /chrome.deb || apt-get install -yf \
	&& rm /chrome.deb \
	&& curl https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip -o /usr/local/bin/chromedriver.zip \
	&& unzip /usr/local/bin/chromedriver.zip \
	&& mv /chromedriver /usr/local/bin/ \
	&& rm /usr/local/bin/chromedriver.zip \
	&& chmod +x /usr/local/bin/chromedriver



EXPOSE 8888

CMD ["jupyter", "notebook", "--allow-root"]
