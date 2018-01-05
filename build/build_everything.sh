#!/usr/bin/env bash

# TODO use a virtualenv to build the project; install the requirements there

echo "buiding the slides..."
./build_all_slides.sh
echo "built the slides."

echo "building the project..."
cd ../
make html
cd -
# TODO figure out pushd and popd
echo "built the project."

echo "DONE: Files are at ../_built/html/index.html"
