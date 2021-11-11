FROM python:3

RUN mkdir /srv/backtab/
#RUN apt-get -y update && apt-get install git mercurial
WORKDIR /usr/src/app

COPY requirements.txt  ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src src
COPY setup.py .
RUN python ./setup.py install

WORKDIR /srv/backtab
COPY config.yml.default /etc/backtab.yml
COPY docker-startup.sh /docker-startup.sh

VOLUME /srv/backtab

RUN mkdir /root/.ssh
RUN echo github.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ== >>/etc/ssh/ssh_known_hosts
RUN git config --global user.name "Backtab server" && git config --global user.email "backtab@example.com"

CMD ["/bin/bash", "/docker-startup.sh"]
EXPOSE 4903