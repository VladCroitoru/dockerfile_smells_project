FROM python:3.6.4
LABEL maintainer="info@blockbrothers.io"

RUN apt-get update && apt-get -y install cron ntp

WORKDIR /usr/src/votebot

COPY ./requirements.txt ./
COPY ./settings.example.py ./
COPY ./votebot.py ./
COPY ./run.sh ./
RUN chmod +x ./run.sh
COPY ./LICENSE ./
COPY ./README.md ./
COPY ./crontab /etc/cron.d/votebot
RUN chmod 0640 /etc/cron.d/votebot

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r ./requirements.txt

RUN sed -i 's/toml==0\.9\.3\.1/toml==0\.9\.3/' $(find /usr/local/lib/python3.6/site-packages/steem-* -name requires.txt)

RUN steempy set nodes https://api.steemit.com,https://steemd.minnowsupportproject.org,https://gtg.steem.house:8090,https://steemd.privex.io,https://steemd.pevo.science,https://rpc.steemliberator.com

CMD ["/bin/bash", "run.sh"]
