#!/bin/bash

function runHadolint() {
  local pwd="$(pwd)/$1"
  local dockerfiles=$(find "$pwd" -type f -name Dockerfile)
  local count=$(echo "$dockerfiles" | wc -l)
  echo "running hadoling in $pwd"
  echo "dockerfiles count: $count"
  echo ""
  for dockerfile in $dockerfiles; do
    echo "hadolint $dockerfile"
    hadolint "$dockerfile" --format json > "$dockerfile.hadolint.json"
  done
}

function main() {
  if [ -n "$1" ];
  then
    runHadolint "$1"
  else
    echo 'no target folder provided'
  fi
} 

main "$@"