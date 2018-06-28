#!/bin/bash
set -e

for file in yamls/*; do
    rancher kubectl create -f $file
done;
