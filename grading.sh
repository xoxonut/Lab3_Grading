#!/bin/bash

# Function to test HW3
grading_learning_bridge(){
    local result=$(sudo mn --controller=remote,127.0.0.1:6653 \
        --topo=tree,depth=2 \
        --switch=ovs,protocols=OpenFlow14 \
        --test=pingall 2>&1 | grep "Results"| \
        grep -o '[0-9]*%')

    if [[ "$result" = "0%" ]]; then
        return 0
    else
        return 1
    fi
}
grading_proxyarp(){
    local result=$(sudo mn --controller=remote,127.0.0.1:6653 \
        --topo=tree,depth=2 \
        --switch=ovs,protocols=OpenFlow14 \
        --test arpingall \
        --custom mn_test.py 2>&1 | grep "unanswered" | \
        grep -v 0%)
    if [[ -z "$result" ]]; then
        return 0
    else 
        return 1
    fi
}

grading_learning_bridge
if [[ $? -eq 0 ]]; then
    echo "success"
else
    echo "fail"
fi
grading_proxyarp
if [[ $? -eq 0 ]]; then
    echo "success"
else
    echo "fail"
fi