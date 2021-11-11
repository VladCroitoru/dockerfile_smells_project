FROM openjdk:8

# RUN apt --fix-broken install -y

# Upgrade the os to latest versions
RUN  apt-get update -y && \
     apt-get install -y wget zip && \
     apt-get clean

# Get Current Version
# https://github.com/taniman/profit-trailer/releases/
# RUN wget https://github.com/taniman/profit-trailer/releases/download/2.0.4/ProfitTrailer-2.0.4.zip && \
# RUN wget https://grandmore.com/trading/ProfitTrailer.zip && \
#  unzip ProfitTrailer.zip
RUN wget https://github.com/taniman/profit-trailer/releases/download/2.1.10/ProfitTrailer-2.1.10.zip && \
  unzip -d ProfitTrailer ProfitTrailer-2.1.10.zip && \
  mv ProfitTrailer/ProfitTrailer-2.1.10/* ProfitTrailer && \
  rm -rf ProfitTrailer/ProfitTrailer-2.1.10
