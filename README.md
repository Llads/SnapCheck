# SnapCheck
Snapchat name checker written in Python 3.9 with multithreading

# Files:
ToCheck.txt - Names the script will check.
Available.txt - Names the script finds to be available and writes to this text file.

#How It Works:
The script opens ToCheck.txt and makes each separate line into the "names" array. Then, the script enteres a loop where it appends and makes the get request to the Snapchat API where it returns if the name is available or not. If the name is unavailable it is printed in red. If the name is available, it is printed in green and saved to the Available.txt file on its own line.
