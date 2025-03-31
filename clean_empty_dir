#!/bin/bash

# 设置仓库和目录
REPO="generic-demo"
CUSTOM_DIR="custom-folder"

# 查询指定目录下的所有子目录
custom_all_folder=$(jfrog rt curl "api/storage/$REPO/$CUSTOM_DIR")
# 提取子目录列表
custom_folder_uri=($(echo "$custom_all_folder" | jq -r '.children[] | select(.folder == true) | .uri'))

for custom_sub_folder in "${custom_folder_uri[@]}"; do

    DIR_PATH=$CUSTOM_DIR$custom_sub_folder
    # 查询指定目录下的所有子目录
    subdirectories_response=$(jfrog rt curl "api/storage/$REPO/$DIR_PATH?list&deep=1")

    # 提取文件列表
    files=($(echo "$files_response" | jq -r '.files[].uri'))
    # 创建一个空数组来存储空目录
    empty_directories=()
    # 遍历所有子目录
    for subdir in "${subdirectories[@]}"; do
    # 检查该子目录是否包含文件
    contains_file=false
    for file in "${files[@]}"; do
        if [[ "$file" == "$subdir"* ]]; then
        contains_file=true
        break
        fi
    done
    # 如果不包含文件，则认为是空目录
    if [ "$contains_file" = false ]; then
        empty_directories+=("$subdir")
    fi
    done
    echo ${empty_directories[1]}
    # 删除空目录
    for empty_dir in "${empty_directories[@]}"; do
        #  仅验证删除列表，注释jrog 行
        echo "Deleting empty directory: $REPO/$DIR_PATH$empty_dir"
        jfrog rt del "$REPO/$DIR_PATH$empty_dir" --quiet
    done
done
