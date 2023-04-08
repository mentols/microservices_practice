#!/bin/bash
# workdir /
set -o errexit

source ./scripts/set-env.sh
# todo: makefile
echo " =============================> Build start <============================= "
echo " =============================[ Building image ]============================= "
mvn spring-boot:build-image
echo " =============================> Build end <============================= "