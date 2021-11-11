FROM ubuntu:20.04 as builder

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata ca-certificates build-essential cmake make golang git sudo curl gnupg \
    && echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" > /etc/apt/sources.list.d/coral-edgetpu.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends libedgetpu-dev

WORKDIR /build
COPY . .

RUN make

FROM ubuntu:20.04

WORKDIR /app

COPY --from=builder /usr/local/lib/libopencv*         /usr/local/lib/
COPY --from=builder /build/lib                        /app/lib
COPY --from=builder /build/models                     /app/models
COPY --from=builder /build/static                     /app/static
COPY --from=builder /build/gin-tflite                 /app

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ca-certificates ffmpeg libgtk2.0-0 curl gnupg \
    && echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" > /etc/apt/sources.list.d/coral-edgetpu.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends libedgetpu1-std \
    && apt clean

ENTRYPOINT [ "./gin-tflite" ]
