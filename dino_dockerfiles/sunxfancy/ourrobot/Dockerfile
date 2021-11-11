FROM kaixhin/torch:latest
RUN mkdir /app
WORKDIR /app
RUN luarocks install torch
RUN luarocks install nn
RUN luarocks install rnn
RUN luarocks install async
RUN luarocks install penlight
VOLUME /app
EXPOSE 8082
CMD ./run_server.sh
