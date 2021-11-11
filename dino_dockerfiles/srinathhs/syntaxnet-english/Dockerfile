FROM brianlow/syntaxnet


ADD http://download.tensorflow.org/models/parsey_universal/English.zip /root/models/syntaxnet/syntaxnet/models/
RUN unzip /root/models/syntaxnet/syntaxnet/models/English.zip -d /root/models/syntaxnet/syntaxnet/models/
ENV MODEL_DIR=/root/models/syntaxnet/syntaxnet/models/syntaxnet/English/

WORKDIR /root/models/syntaxnet
