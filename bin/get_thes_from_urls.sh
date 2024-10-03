#! /usr/bin/env bash

# where is this
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


# allow injection of env
ENV=${SCRIPT_DIR}/../.env
if [ -f ${ENV} ]; then
  source $ENV
fi


# where is the data to work on
DATA_DIR=${DATA_DIR:-${SCRIPT_DIR}/../data} 
URLS=${URLS:-${SCRIPT_DIR}/../urls.txt}


# the urls to get
if [ ! -f ${URLS} ] ; then
  echo "missing input urls.txt at ${URLS}"
  exit 1
fi
urls=$(cat ${URLS})


#process the urls
for url in $urls; do
  file="${DATA_DIR}/${url##*/}"
  echo "$url --> $file";
  curl -sL --url "$url" -o $file 2>/dev/null
done
