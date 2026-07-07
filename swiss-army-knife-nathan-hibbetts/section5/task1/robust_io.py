
try:
    f = open("file.txt")
    f.write("Lorem ipsum dolor sit amet");
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception:
    print("Something bad happened")
finally:
    print("Operation Attempted")