# MyTool

MyTool is a simple command-line utility for processing text files. It can measure the length of a text in words, count characters, and estimate the length of a speech in seconds based on an average speaking rate.

## Features

- Measure the length of a text in words.
- Count the number of characters in a text.
- Estimate the length of a speech in seconds.

## Installation

To install MyTool, follow these steps:

1. Clone the repository or download the files to your local machine.

2. Navigate to the directory containing the files:

   ```bash
   cd /usr/local/bin
   ```

3. Make the installer script executable:

   ```bash
   chmod +x install_mytool.sh
   ```

4. Run the installer script:

   ```bash
   ./install_mytool.sh
   ```

   If you encounter permission issues, use:

   ```bash
   sudo ./install_mytool.sh
   ```

## Usage

Once installed, you can use MyTool from anywhere in the terminal. Here are some examples:

- Measure the length of a text in words:

  ```bash
  mytool -l path/to/speech.txt
  ```

- Count the number of characters in a text:

  ```bash
  mytool -ch path/to/speech.txt
  ```

- Estimate the length of a speech in seconds:

  ```bash
  mytool -t path/to/speech.txt
  ```

## Examples

Here are some example commands and their expected outputs:

- **Word Count**: `mytool -l speech.txt`  
  Output: `Word count: 123`

- **Character Count**: `mytool -ch speech.txt`  
  Output: `Character count: 456`

- **Length in Seconds**: `mytool -t speech.txt`  
  Output: `Length in seconds: 49.20`

## Contributing

If you would like to contribute to MyTool, please fork the repository and submit a pull request. We welcome all improvements and bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Kruszewski at franciszek.kruszewski@gmail.com
