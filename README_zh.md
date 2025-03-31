# 清理 Artifactory 文件和镜像的脚本

## 项目简介

本项目提供了一组脚本，旨在帮助用户高效清理 JFrog Artifactory 中的冗余文件和镜像。通过使用 JFrog Client，用户可以轻松管理和维护其 Artifactory 实例，确保存储空间的合理利用。

## 安装 JFrog Client

在使用清理脚本之前，请确保您已安装 JFrog Client。可以按照以下步骤进行安装：

1. **下载 JFrog Client**:
   - 您可以从 [JFrog 官网](https://jfrog.com/getcli/) 下载最新版本的 JFrog Client。

2. **安装 JFrog Client**:
   - 在终端中运行以下命令进行安装（以 macOS 为例）：
     ```bash
     curl -fL https://getcli.jfrog.io | sh
     ```

3. **验证安装**:
   - 安装完成后，您可以通过以下命令验证安装是否成功：
     ```bash
     jfrog --version
     ```

## 下载和使用清理脚本

1. **克隆本仓库**:
   - 使用 Git 克隆本仓库到您的本地机器：
     ```bash
     git clone https://github.com/adamwoo/artifactory-cleanup-script.git
     ```

2. **进入项目目录**:
   - 切换到克隆下来的项目目录：
     ```bash
     cd artifactory-cleanup-script
     ```

3. **运行清理脚本**:
   - 请根据您的需求修改脚本中的配置，并通过以下命令运行清理脚本：
     ```bash
     bash clean_artifactory.sh
     ```

## 注意事项

- 在运行清理脚本之前，请确保您已备份重要数据，以防意外删除。
- 请根据 Artifactory 的具体配置调整脚本中的参数。

## 贡献

欢迎提交问题、功能请求或贡献代码！请遵循贡献指南。

## 许可证

本项目采用 MIT 许可证，详细信息请参见 LICENSE 文件。

---

感谢您使用本项目！如有任何问题，请随时联系我。
