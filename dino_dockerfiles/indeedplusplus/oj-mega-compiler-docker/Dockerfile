FROM ubuntu

RUN apt-get update && \
  apt-get install -y openjdk-8-jdk-headless && \
  apt-get install -y gcc g++ fp-compiler && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*
  
