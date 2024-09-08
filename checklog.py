import os

# bazel run onos-local -- clean debug 2>&1 | tee -a ~/output.log first
log_file = os.path.expanduser('~/output.log')
with open(log_file,'w') as file:
    file.writelines('test\n')
