MYSELF=`pwd`/$0
MYDIR="${MYSELF%/*}"

image_name_full="j-apps-pstocky"

project_dir=`dirname ${MYDIR}`
real_project_dir=`readlink -f ${project_dir}`

docker run \
    -v ${real_project_dir}:${real_project_dir} \
    -v ${real_project_dir}:/code \
    -p 8899:8899 \
    -t ${image_name_full}
