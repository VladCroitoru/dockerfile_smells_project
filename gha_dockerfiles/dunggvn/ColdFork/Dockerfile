FROM ghcr.io/elytra8/fedora-docker:main

RUN mkdir /ColdFork && chmod 777 /ColdFork && git clone https://github.com/dunggvn/ColdFork -b production /ColdFork
ENV PATH="/ColdFork/bin:$PATH"
WORKDIR /ColdFork

CMD ["python3","-m","userbot"]
