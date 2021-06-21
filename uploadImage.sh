#!/bin/zsh

source ~/.zshrc

conda activate python3.8

project_path=$(cd `dirname $0`; pwd)

cd $project_path
result=()

function upload() {
    t=`python qiniuUpload.py $1`
    result=(${result[@]} "${t}")
}
while [ $# -gt 0 ]; do
    upload "$1" $index
    shift
done

echo "Upload Success:"
for i in ${result[*]}; do
echo $i;
done
