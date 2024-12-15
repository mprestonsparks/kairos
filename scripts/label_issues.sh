#!/bin/bash

# Add epic label to epics
for i in 1 6 7 8
do
    gh issue edit $i --add-label "epic"
done

# Add phase labels
for i in {1..5}
do
    gh issue edit $i --add-label "phase-1"
done

for i in {6..12}
do
    gh issue edit $i --add-label "phase-2"
done

for i in {13..16}
do
    gh issue edit $i --add-label "phase-3"
done

for i in {17..20}
do
    gh issue edit $i --add-label "phase-4"
done

# Add type-feature to implementation tasks
for i in {2..5} {9..12} {13..16} {17..20}
do
    gh issue edit $i --add-label "type-feature"
done

# Add priorities
# High priority for core infrastructure
for i in {2..5}
do
    gh issue edit $i --add-label "priority-high"
done

# Medium priority for initial tasks in each phase
for i in 9 13 17
do
    gh issue edit $i --add-label "priority-medium"
done

# Low priority for later phase tasks
for i in {10..12} {14..16} {18..20}
do
    gh issue edit $i --add-label "priority-low"
done
