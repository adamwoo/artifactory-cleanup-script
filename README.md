# artifactory-cleanup-script
artifactory cleanup script 

# Artifactory Cleanup Script


## Project Overview

This project provides a set of scripts designed to help users efficiently clean up redundant files and images in JFrog Artifactory. By utilizing the JFrog Client, users can easily manage and maintain their Artifactory instances, ensuring optimal storage utilization.

## Installing JFrog Client

Before using the cleanup scripts, please ensure that you have the JFrog Client installed. Follow these steps for installation:

1. **Download JFrog Client**:
   - You can download the latest version of the JFrog Client from the [JFrog website](https://jfrog.com/getcli/).

2. **Install JFrog Client**:
   - Run the following command in your terminal to install (example for macOS):
     ```bash
     curl -fL https://getcli.jfrog.io | sh
     ```

3. **Verify Installation**:
   - After installation, you can verify that it was successful by running:
     ```bash
     jfrog --version
     ```

## Downloading and Using the Cleanup Script

1. **Clone this Repository**:
   - Use Git to clone this repository to your local machine:
     ```bash
     git clone https://github.com/adamwoo/artifactory-cleanup-script.git
     ```

2. **Navigate to the Project Directory**:
   - Change into the cloned project directory:
     ```bash
     cd your-repo-name
     ```

3. **Run the Cleanup Script**:
   - Modify the configuration in the script as per your requirements, and run the cleanup script using:
     ```bash
     # check the script params before process
     bash clean_artifactory.sh
     ```

## Notes

- Before running the cleanup script, please ensure you have backed up any important data to prevent accidental deletion.
- Adjust the script parameters according to your specific Artifactory configuration.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or code contributions. Follow the contribution guidelines.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Thank you for using this project! If you have any questions, feel free to reach out.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=adamwoo/artifactory-cleanup-script&type=Date)](https://www.star-history.com/#adamwoo/artifactory-cleanup-script&Date)
