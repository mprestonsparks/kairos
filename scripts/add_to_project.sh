#!/bin/bash

# Add all issues to the project
for i in {1..20}
do
    gh project item-add 5 --owner mprestonsparks --url "https://github.com/mprestonsparks/kairos/issues/$i"
    echo "Added issue #$i to project"
    sleep 1
done
