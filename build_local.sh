#!/usr/bin/env bash

# this script will only run if the build dir is available and there are at-least one previous build present
branch='master'
script_dir=`dirname $0 | xargs realpath`
tag_version=`git describe --tags`
module_name=`basename ${script_dir}`
echo ${script_dir} , ${module_name}

# import the studio env paths in terminal
source ~/studio/systems/pipe-env.sh
build_path_dir=${PIPELINE_BUILD_DIR}/${module_name}/${branch}/
echo "Build dir = ${build_path_dir}"

# get the latest build number to be built for
output_build_no=$(python ./get_build_no.py ${build_path_dir} 2>&1 >/dev/null)

# construct the build dir
build_path=${PIPELINE_BUILD_DIR}/${module_name}/${branch}/${tag_version}-${output_build_no}
echo ${build_path}

# sync to file to its latest
#git checkout origin ${branch}
rsync -avz --exclude '.*' ${script_dir}/ ${build_path}
echo ${build_path}








