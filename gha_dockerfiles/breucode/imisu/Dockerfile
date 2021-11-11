FROM gcr.io/distroless/base-debian11
COPY build/native-image/imisu /imisu
ENTRYPOINT [ "/imisu", "-XX:MaximumHeapSizePercent=80" ]
