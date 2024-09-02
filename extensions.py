#implement a program that prompts the user for the name of a file and then outputs that file’s media type
#The output should be for files ending with the following suffixes(case-insensitive):
#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip
#If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead.

filename = input("Enter a filename: ").lower()

if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")