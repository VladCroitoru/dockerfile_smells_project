FROM marcelmaatkamp/gnuradio:3.7.1

RUN git clone https://github.com/MalcolmRobb/dump1090.git
WORKDIR dump1090
RUN make

EXPOSE 8080 
EXPOSE 30003

ENTRYPOINT ["./dump1090", "--interactive","--aggressive","--net", "--net-sbs-port", "30003"]
