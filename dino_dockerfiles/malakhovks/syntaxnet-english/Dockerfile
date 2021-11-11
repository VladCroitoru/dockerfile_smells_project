FROM saturnism/syntaxnet
ADD http://download.tensorflow.org/models/parsey_universal/English.zip /models/
RUN unzip /models/English.zip
ENV MODEL_DIR=/syntaxnet/models/syntaxnet/English/



# COMMANDS to build and run
# ===============================
# mkdir build && cp Dockerfile build/ && cd build
# docker build -t syntaxnet .
# docker run syntaxnet
