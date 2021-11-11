
FROM openjdk:7

LABEL maintainer="Temples of Syrinx (John Chambers-Malewig)"

ENV DEBIAN_FRONTEND noninteractive

ENV LIBSWT_GTK_3_JAVA_VERSION 3.8.2-3

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            libswt-gtk-3-java="$LIBSWT_GTK_3_JAVA_VERSION" && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

COPY [ \
       "resources/Gallifreyan.zip", "/tmp" \
     ]

RUN [ \
      "unzip", "/tmp/Gallifreyan.zip" \
    ]

ENTRYPOINT [ \
             "/application.linux/Gallifreyan" \
           ]

