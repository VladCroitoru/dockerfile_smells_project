FROM python:3.6

LABEL Author="River Yang (river.yang@outlook.com)"

ENV SLACK_BOT_TOKEN="" \
    quoteAsset="BTC" \
    apikey="apikey" \
    apisecret="apisecret"
RUN mkdir /workfolder

COPY requirements.txt /workfolder/.
COPY binance-bot.py /workfolder/.
RUN pip install -r /workfolder/requirements.txt
ENTRYPOINT python /workfolder/binance-bot.py
