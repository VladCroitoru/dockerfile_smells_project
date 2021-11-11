FROM invenfantasy/scala

# 4 caching
RUN git clone -b master https://github.com/invenfantasy/cosmos && cd /cosmos && sbt one-jar
WORKDIR /cosmos
