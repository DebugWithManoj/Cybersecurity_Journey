

Simple File Management Utility

Hey there! Ever needed to quickly create a bunch of empty files for a project? Or clean up a folder full of temporary logs without having to click a million times? This little Python script is here to help!

It's a simple, colorful, command-line tool that handles a few common file tasks so you don't have to. No complicated commands to remember, just a straightforward menu.

(A little preview of what the menu looks like!)

✨ What Can It Do?

This script bundles a few handy features into one place:

📂 Create Multiple Files: Instantly generate any number of files with a custom name and extension (e.g., test_0.log, test_1.log, test_2.log...).

🗑️ Bulk Delete Files: Safely remove files from a folder based on a pattern. You can choose to delete files that start with or end with a specific name. Don't worry, it asks for confirmation before deleting anything!

🎲 Inspect a Random File: Point it at a folder, and it will pick a random file and show you its details, like its full path and size (in a nice, human-readable format like KB or MB).

🚀 Getting Started

Getting this up and running is super easy. You just need Python and one small library.

1. Prerequisites

You'll need Python 3 installed on your system.

The script uses the colorama library to make the text colorful and easy to read. You can install it with pip:


pip install colorama
2. How to Use

Save the code as a Python file (e.g., file_manager.py).

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script with Python:


python file_manager.py

That's it! The menu will appear, and you can choose what you want to do.

A Closer Look at the Options
1. Create New Files

Perfect for setting up a new project or creating dummy files for testing. The script will ask you:

How many files you want.

The base name for the files (like document).

The file extension (like txt).

It will then create document0.txt, document1.txt, and so on, right in the same folder where you're running the script.

2. Remove Files by Name Pattern

This one is powerful, so use it with care! It helps you clean up folders quickly.

First, you'll provide the path to the folder you want to clean up.

Then, you'll choose whether to match files that start with a certain pattern or end with one.

It will show you a list of all the files it's about to delete and ask for a final confirmation. You have to type YES to proceed. If you type anything else, the operation is safely cancelled.

⚠️ Be careful! File deletion is permanent. Always double-check the list of files before confirming.

3. Get Details of a Random File

A fun little utility feature. Just give it a folder path, and it will randomly select one file and tell you all about it. It's great for when you just need to quickly inspect any file in a crowded directory.

Hope you find this little tool useful. Happy file managing
