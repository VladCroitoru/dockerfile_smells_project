FROM spk121/gtk4-guile-sdk:latest

WORKDIR /usr/local/src/Guidance
COPY . /usr/local/src/Guidance
# RUN git clone https://github.com/spk121/Guidance.git
RUN meson --prefix=/app _build
RUN ninja -C _build
RUN ninja -C _build install
