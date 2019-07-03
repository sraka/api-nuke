set -e
script_dir=`dirname $0`
platform=`uname`
echo "Current script dir =  ${script_dir}/load/"
echo "Current platform =  ${platform}" 
export NUKE_PATH=${script_dir}/load/:$NUKE_PATH
echo env | grep NUKE_PATH




# Need to add ENV Variables at Launch
# SELF_PATH
# CORE_LIB
# Need to replace the use of .replace("\\","/") in config file
