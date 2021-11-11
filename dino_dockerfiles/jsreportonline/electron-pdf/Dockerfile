FROM ubuntu:xenial
MAINTAINER Jan Blaha
EXPOSE 8000

RUN apt-get update && apt-get install -y curl sudo && \
    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \
    apt-get install -y nodejs libgtk2.0-dev libxtst-dev libxss1 libgconf2-dev libnss3-dev libasound2-dev libnotify4 xvfb dbus-x11 && \
    apt-get install -y fonts-dejavu-core fonts-dejavu-extra fonts-droid-fallback fonts-guru fonts-guru-extra fonts-horai-umefont fonts-kacst fonts-kacst-one fonts-khmeros-core  fonts-lao fonts-liberation fonts-lklug-sinhala fonts-lohit-guru fonts-nanum fonts-noto-cjk fonts-opensymbol fonts-roboto fonts-roboto-hinted fonts-sil-abyssinica fonts-sil-padauk fonts-stix fonts-symbola fonts-takao-pgothic fonts-thai-tlwg fonts-tibetan-machine fonts-tlwg-garuda fonts-tlwg-kinnari fonts-tlwg-laksaman fonts-tlwg-loma fonts-tlwg-mono fonts-tlwg-norasi fonts-tlwg-purisa fonts-tlwg-sawasdee fonts-tlwg-typewriter fonts-tlwg-typist fonts-tlwg-typo fonts-tlwg-umpush fonts-tlwg-waree fonts-unfonts-core

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install --production

COPY . /usr/src/app

COPY patch /usr/src/app

HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

# exporting the display env var for use in the electron process
ENV DISPLAY :99
ENV DEBUG electron-html-to,electron-html-to:*
ENV ELECTRON_ENABLE_STACK_DUMPING true
ENV ELECTRON_ENABLE_LOGGING true
ENV ELECTRON_HTML_TO_STDSTREAMS true

# startup script to launch dbus and xvfb correctly along with our app:
# - we ensure that lock files created by Xvfb server (stored at /tmp/ with file names like /tmp/.X99-lock)
#   are cleanup correctly on each container run (rm -f /tmp/.X*lock),
#   the lock file created by the Xvfb server is a signal that xvfb uses to determine if the server is already running.
#   this step is important because the `workers` service is constantly restarting the container (docker restart -t 0) in a "hard" way,
#   which does not let the Xvfb server to clean up its lock files correctly, we are cleaning up those lock files manually when the container
#   runs to avoid errors like "Fatal server error: Server is already active for display 99 If this server is no longer running, remove /tmp/.X99-lock and start again"
#   after restarting the container
# - we ensure that temp folders and files created by xvfb-run (stored at /tmp/ with folder names like /tmp/xvfb-run.4dsfx)
#   are cleanup correctly on each container run (rm -rfd /tmp/xvfb-run*)
#   this step is important because the `workers` service is constantly restarting the container (docker restart -t 0) in a "hard" way,
#   which does not let xvfb-run to clean up its temp files correctly, we are cleaning up those files manually when the container runs
#   to avoid having stale folders after restarting the container
# - we use xvfb-run command instead of manually configuring Xvfb server because xvfb-run has a built-in mechanism that waits until the Xvfb server
#   its already started before trying to start our app (xvfb-run --server-num=99 --server-args='-screen 0 1024x768x24 -ac' node index.js),
#   in case that errors from xvfb needs to be printed to stdout for debugging purposes just pass -e /dev/stdout option (xvfb-run -e /dev/stdout .......)
#   the important part of this command is the -ac option in --server-args, -ac disables host-based access control mechanisms in Xvfb server,
#   which prevents the connection to the Xvfb server from our app
CMD rm -f /tmp/.X*lock && rm -rfd /tmp/xvfb-run* && xvfb-run --server-num=99 --server-args='-screen 0 1024x768x24 -ac' node index.js
