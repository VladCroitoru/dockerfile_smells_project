FROM python:3
RUN apt-get update
RUN apt-get -y install bash git openssl curl
RUN pip install dns-lexicon cryptography
ADD https://raw.githubusercontent.com/AnalogJ/lexicon/master/examples/dehydrated.default.sh lexicon.dehydrated.sh
RUN chmod +x lexicon.dehydrated.sh
RUN git clone https://github.com/lukas2511/dehydrated.git
WORKDIR /dehydrated
ENTRYPOINT ["/dehydrated/dehydrated"]
#RUN ln -sf /certs/domains.txt /domains.txt
