FROM archlinux:latest
RUN useradd --uid 1000 user --create-home
WORKDIR /home/user
USER user
COPY PKGBUILD .
