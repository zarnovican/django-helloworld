#!/bin/bash

# move version tags after rebase
git tag -f v1.0 $(git log --grep='version bump to v1.0' --format=%H)
git tag -f v2.0 $(git log --grep='version bump to v2.0' --format=%H)
