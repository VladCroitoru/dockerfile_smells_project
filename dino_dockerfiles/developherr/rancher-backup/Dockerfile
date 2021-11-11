FROM webcenter/rancher-backup
MAINTAINER David Seibert <d.seibert@s-v.de>

# Upgrade Duplicity & Proto
RUN apt-get update && apt-get purge -y duplicity && apt-get install -y software-properties-common && add-apt-repository -y ppa:duplicity-team/ppa && apt-get update && apt-get install -y duplicity && pip install --upgrade boto

WORKDIR "/app"
CMD ["/usr/bin/supervisord"]
