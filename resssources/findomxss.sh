#!/bin/bash

#This code is taken from https://github.com/dwisiswant0/findom-xss Do check it out.

PATTERN="(document|location|window)\.(URL|documentURI|href|search|hash|referrer|location\.href|name)"
BODY=$(curl -sL ${1})
SCAN=($(echo ${BODY} | grep -Eoin ${PATTERN}))
if [[ ! -z "${SCAN}" ]]; then
        echo -en "---\n\033[0;32m[!] ${1}\033[0m\n${SCAN}\n"
        echo -e "---\n${1}\n${SCAN}" >> domxss_scan.txt
fi