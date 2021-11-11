FROM debian:testing
# This installs the vim "plasticbox" plugin for Markdown
ADD getplastic.py /root/getplastic.py
ADD vimrc /root/.vimrc
# ca-certificates must be installed in order not to be cleaned out
# by apt-get autoremove
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
	git \
        ca-certificates \
        vim-nox \
	python-pip \
	python-sqlalchemy \
	python-html2text \
	python-thrift \
	python-oauth \
    && git clone git://github.com/VitaliyRodnenko/geeknote.git /opt/geeknote \
    && cd /opt/geeknote  \
    && python setup.py install \
    && cd /root \
    && python /root/getplastic.py \
    && rm -f /root/getplastic.py \
    && rm -rf /opt/geeknote \
    && apt-get remove -y git python-pip \
    && apt-get autoremove -y \
    && apt-get clean
ENTRYPOINT ["geeknote"]
