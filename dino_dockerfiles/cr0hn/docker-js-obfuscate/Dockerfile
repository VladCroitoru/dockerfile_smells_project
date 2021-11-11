FROM python:2.7-jessie

RUN pip install unidecode slimit awscli && \
    wget https://raw.githubusercontent.com/adamyork/garble/master/src/garble.py && \
    echo '#!/usr/bin/env python' | cat - garble.py > temp && mv temp /usr/bin/garble.py && \
    cd /usr/bin && chmod -x garble.py && cd /

ADD ./obfuscate.sh /usr/bin/obfuscate
RUN chmod +x /usr/bin/obfuscate