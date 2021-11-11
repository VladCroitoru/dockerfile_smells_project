FROM pandoc/core
MAINTAINER blackgamer@mbj.nifty.com

RUN apk --update add python3 make && \
  pip3 install --upgrade pip && \
  pip3 install tornado
RUN mkdir -p /opt/markdown-diary
ADD . /opt/markdown-diary
WORKDIR /opt/markdown-diary
EXPOSE 8001
CMD ["sh", "./run.sh"]
