FROM ubuntu
COPY .git /.git
RUN apt-get update -y && \
    apt-get install -y git curl xz-utils && \
    release_name="$(git describe)" && \
    repo_url="$(git config --get remote.origin.url)" && \
    repo_url="${repo_url%.git}" && \
    mkdir rumprun-package-binaries && \
    curl -L "$repo_url/releases/tag/$release_name" | \
        grep -o '[^/]*\.tar\.xz"' | tr -d '"' | tr '\n' '\0' | \
        xargs -0 -n 1 -I % sh -c "curl -L $repo_url/releases/download/$release_name/% | tar -C rumprun-package-binaries -Jx" && \
    rm -rf .git
