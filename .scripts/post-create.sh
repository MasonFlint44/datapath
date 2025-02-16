#!/bin/bash

mamba shell init --shell bash

mamba install conda-merge -y

.scripts/update-bashrc.sh
.scripts/build-environment.sh
