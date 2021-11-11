FROM testbed/vim:8

RUN install_vim -tag v7.3.429 -py -name vim73 -build \
                -tag v7.4.052 -py2 -py3 -ruby -lua -name vim74 -build \
                -tag v8.0.0027 -py2 -py3 -ruby -lua -name vim8 -build \
                -tag master -py2 -py3 -ruby -lua -name vim -build \
                -tag neovim:v0.2.0 -py2 -py3 -ruby -name nvim2 -build \
                -tag neovim:v0.2.2 -py2 -py3 -ruby -name nvim22 -build \
                -tag neovim:v0.3.0 -py2 -py3 -ruby -name nvim3 -build \
                -tag neovim:master -py2 -py3 -ruby -name nvim -build
