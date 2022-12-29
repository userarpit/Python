fo = open("foo.txt","r")
try:
        fo.write("Arpit")
except IOError:
        print("can't write! file is open in read only mode")
else:
        print("end")
finally:
        print("finally")
fo.close()