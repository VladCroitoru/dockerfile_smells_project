FROM hseeberger/scala-sbt

RUN apt-get update
RUN apt-get install git

RUN git clone --depth 1 --single-branch https://github.com/cliftbar/AkkaDisaster.git

WORKDIR AkkaDisaster

RUN sbt compile

EXPOSE 9001

CMD sbt -J-Xmx2048M run