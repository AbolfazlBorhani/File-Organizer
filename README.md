File Organizer (Qt GUI Application)
===================================

Overview
========
The File Organizer is a Qt-based graphical user interface (GUI) application designed to help users organize files in a directory. It provides functionalities such as displaying files, categorizing them into folders based on their extensions, renaming files, and deleting files. The application is built using C++ and leverages the Qt framework for its user interface.

Features
========
Display Files:
- Lists all files in the specified directory.
- Groups files by their extensions (.txt, .png, .jpg, etc.).
- Displays the number of files in each category.

Categorize Files:
- Automatically creates subdirectories based on file extensions.
- Moves files into their respective folders (.txt files into a TXT folder).
- Logs the creation of new directories and the movement of files.

Rename Files:
- Renames files in a selected category with a sequential numbering scheme (1.txt, 2.txt).
- Logs the renaming process and displays the results.

Delete Files:
- Deletes files in a selected category or all files in the directory.
- Logs the deletion process and confirms the operation.

Error Handling:
- Provides warnings for invalid inputs, non-existent directories, or empty directories.
- Logs errors and exceptions during file operations.

How It Works
============
1. Path Handling:
- The application retrieves the directory path from the user input.
- Converts backslashes (\\) to forward slashes (/) for compatibility.
   Ensures the path ends with a trailing slash (/).

2. File Operations:
- File Listing: Scans the directory and categorizes files based on their extensions.
- Categorization: Creates subdirectories for each file type and moves files into them.
- Renaming: Renames files in a selected category with sequential numbers.
- Deletion: Deletes files in a selected category or all files in the directory.

3. Logging:
- All operations are logged in a text area within the GUI.
- Logs include warnings, errors, and success messages.

Requirements
============
- C++ Compiler: Supports C++17 or higher.
- Qt Framework: Version 6 or higher.
- CMake: For building the project.
