# seek() and tell() functions as alternative for f.read() or f.write()
# seek() - Just moves the current cursor position to the specific bytes, from which further read() will performed
# tell() - It just returns tells the position of seek (how many bytes are skipped)
# truncate() - Select only specific bytes from starting (Note: Only works with "w" or "a" mode)

with open("F:/100 Days of Python/Data/Day 2/Hello.txt", "r") as f:
    text_without_seek = f.read()
    f.seek(10) # Start reading from 10th byte of the file (or character)
    print(f.tell())
    text_with_seek = f.read()
    # truncate = f.truncate(4)
    print(text_without_seek)
    print(text_with_seek)
    # print(truncate) # Return error (Needs only "w" or "a" mode)
