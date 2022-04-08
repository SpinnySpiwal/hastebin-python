# hastebin-python
A standalone Python program to handle HTTP GET and POST requests to https://hastebin.app/

# This project refers to [Hastebin.app](https://hastebin.app/), NOT [Hastebin.com](https://hastebin.com/) - the first being a variation of the latter!

**Installation**

This program must be run via a command line interface, and does not require specific installation.

**Use**

To upload a file, use the following syntax:

`python Hastebin.py -u name_of_file.txt`

To download a file, use the following syntax:

`python Hastebin.py -d end_string_for_website optional_name_to_save_to.txt`

Currently, there isn't support for multi-file upload. I plan to implement this in the future - hang tight!

I've only tested text files, not other formats, so please email me bugs. I promise I'll check my email at some point... probably.
