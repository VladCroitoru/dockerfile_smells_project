FROM ragetti/alpine-poco

MAINTAINER ragetti

WORKDIR /app

RUN   \
  mkdir -p /app/log && \
  apk --no-cache --no-progress update && \
  apk --no-cache --no-progress upgrade && \
  apk --no-cache --no-progress add libstdc++ libgcc openssl && \
  apk --no-cache --no-progress --virtual .build-deps add cmake g++ make openssl-dev glib git linux-headers && \
  git clone https://github.com/ragetti/creepMiner.git creepMiner.git && \
  cd creepMiner.git && \
  cmake CMakeLists.txt -DCMAKE_BUILD_TYPE=RELEASE -DNO_GPU=ON -DUSE_CONAN=OFF && \
  make && \
  cp -r ./bin/* /app/ && \
  cp -r resources/public /app && \
  cd .. && \
  rm -r creepMiner.git && \
  apk --no-cache --no-progress del .build-deps && \
  echo "Build complete"

EXPOSE 8126
CMD ["/app/creepMiner"]


