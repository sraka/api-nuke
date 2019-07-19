# This wrapper is to launch NUKE for Testing in dev-zone

set -e
script_dir=`dirname $0`
platform=`uname`
echo "Current platform =  ${platform}"


export SELF_PATH=$script_dir
echo "SELF_PATH = ${SELF_PATH}"

export CORE_LIBRARY=$script_dir/../../python-corelib/core-lib/
echo "CORE_LIBRARY = ${CORE_LIBRARY}"

export NUKE_PATH=${script_dir}/load/
echo "NUKE_PATH = ${NUKE_PATH}"

# Launch NUKE
/usr/bin/VGLrun /usr/bin/env foundry_LICENSE=4101@ws05.hyd.taufilms.com:4101@ws188.kul.taufilms.com "/usr/local/Nuke11.3v2/Nuke11.3" -b










# Need to add ENV Variables at Launch
# SELF_PATH
# CORE_LIB
# Need to replace the use of .replace("\\","/") in config file
