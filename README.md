# hastebin-python
A standalone Python program to handle HTTP GET and POST requests to https://hastebin.app/

# This project refers to https://hastebin.app/, NOT https://hastebin.com/ - the first being a lightweight alternative of the latter!

**Installation**
This program must be run via a command line interface, and does not require specific installation.

**Use**

To upload a file, use the following syntax:

`python Hastebin.py -u name_of_file.txt`

To download a file, use the following syntax:

`python Hastebin.py -d end_string_for_website optional_name_to_save_to.txt`

Currently, this doesn't support multi-file upload. I plan to implement this in the future - hang tight!

I've only tested text files, not other formats, so please do email or post any bugs on the Github.
