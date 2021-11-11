FROM python:3.9-slim

MAINTAINER Hollow Man <hollowman@hollowman.ml>

LABEL version="1.2.10"
LABEL repository="https://github.com/HollowMan6/LZU-Auto-COVID-Health-Report"
LABEL homepage="https://hollowman.ml/"
LABEL maintainer="Hollow Man <hollowman@hollowman.ml>"

COPY entrypoint.sh /entrypoint.sh
COPY LZU-Auto-COVID-Health-Report.py /LZU-Auto-COVID-Health-Report.py
COPY Notify-Result.py /Notify-Result.py
COPY cover.jpg /cover.jpg
COPY requirements-run.txt /requirements.txt

ENV TZ Asia/Shanghai

RUN pip install --upgrade --no-cache-dir pip && if [ "x86_64" = "`arch`" ] || [ "aarch64" = "`arch`" ] || [ "i386" = "`arch`" ]; then \
    pip install --no-cache-dir -r /requirements.txt; if [ ! "$?" = "0" ]; then apt-get update \
    && apt-get install -y \
      rustc \
      libffi-dev \
      libssl-dev \
    && pip install --no-cache-dir -r /requirements.txt \
    && apt-get --purge remove -y \
      rustc \
      libffi-dev \
    && apt-get autoremove -y \
    && apt-get clean; fi; else \
    apt-get update \
    && apt-get install -y \
      libxml2 \
      libxslt1-dev \
      gcc \
      zlib1g-dev \
      libffi-dev \
      libssl-dev \
      rustc \
    && pip install --no-cache-dir -r /requirements.txt \
    && apt-get --purge remove -y \
      libxml2 \
      libxslt1-dev \
      gcc \
      zlib1g-dev \
      manpages \
      libffi-dev \
      rustc \
    && apt-get autoremove -y \
    && apt-get install -y \
       libxslt1.1 \
    && apt-get clean; fi
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
