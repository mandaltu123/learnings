try:
    f = open('testfile.txt', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("There was an OSError")
finally:
    print("I always run")
