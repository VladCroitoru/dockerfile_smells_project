FROM base/archlinux

RUN pacman -Sy --noconfirm python

EXPOSE 80
WORKDIR /srv
CMD ["python", "-m", "http.server", "80"]

