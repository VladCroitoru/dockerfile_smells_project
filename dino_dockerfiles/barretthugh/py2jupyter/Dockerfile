FROM python:2.7.13-jessie

ENV TZ=Asia/Shanghai


COPY requirement.txt /requirement.txt
# COPY pip.conf /root/.pip/pip.conf	only for mirror in China
# COPY source.list /etc/apt/sources.list	only for mirror in China
COPY jupyter_notebook_config.py /root/.jupyter/


RUN wget https://downloads.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz \
	&& tar xvf ta-lib-0.4.0-src.tar.gz \
	&& cd ta-lib \
	&& ./configure --prefix=/usr \
	&& make \
	&& make install \
	&& pip install -r /requirement.txt \
	&& cd .. \
	&& rm -rf ta-lib \
	&& rm ta-lib-0.4.0-src.tar.gz

EXPOSE 8888

CMD ["jupyter", "notebook", "--allow-root"]
