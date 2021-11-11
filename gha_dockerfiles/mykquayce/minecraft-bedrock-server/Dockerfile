FROM ubuntu:latest AS unzip
ARG version=1.17.41.01
RUN apt-get update && apt-get install --assume-yes curl unzip
RUN curl --output ./bedrock-server.zip --url https://minecraft.azureedge.net/bin-linux/bedrock-server-$version.zip
RUN unzip ./bedrock-server.zip -d ./bedrock-server -x *.debug

FROM ubuntu:latest AS run
EXPOSE 19132/tcp 19133/tcp
RUN apt-get update && apt-get install --assume-yes libcurl4
WORKDIR /bedrock-server
COPY --from=unzip /bedrock-server .
ENV LD_LIBRARY_PATH=.
CMD ./bedrock_server
