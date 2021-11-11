FROM monostream/apache-ant
MAINTAINER Jesus Carpintero

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

RUN set -ex \
	&& apt-get install python2.7 git \
	&& wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python \
	&& curl -fSL https://pypi.python.org/packages/source/b/beatbox/beatbox-32.1.zip -o beatbox-32.1.zip \
	&& unzip beatbox-32.1.zip \
	&& cd beatbox-32.1 \
	&& python setup.py install \
	&& cd .. && rm -r beatbox* \
	&& git clone https://github.com/solenopsis/Solenopsis.git \
	&& cd Solenopsis && ./install.sh \
	&& curl -fSL https://eu4.salesforce.com/dwnld/SfdcAnt/salesforce_ant_36.0.zip -o sf.zip \
	&& mkdir -p /usr/share/ant/lib \
	&& unzip sf.zip ant-salesforce.jar -d /usr/share/ant/lib \
	&& rm *.zip
