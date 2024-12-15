#!/bin/bash

# Add Sprint 1 issues to project and set them as "In Progress"
for i in {1..5}
do
    gh issue edit $i --add-project "Kairos Development"
done
