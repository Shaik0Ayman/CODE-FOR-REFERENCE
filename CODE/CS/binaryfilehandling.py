import pickle
def writebinaryfile(data):
    with open("abc.dat","wb") as f:
        try:
            pickle.dump(data,f)
            print("Data written to file")
        except(EOFError):
            print("END OF FILE")
        except(FileNotFoundError):
            print("FILE NOT FOUND")
        except:
            print("ERROR UNABLE TO WRITE IN BINARY FILE")
def readbinaryfile():
    with open("abc.dat","rb") as f:
        try:
            while True:
                s=pickle.load(f)
                print(s)
        except(EOFError):
            print("END OF FILE")
        except(FileNotFoundError):
            print("FILE NOT FOUND")
        except:
            print("ERROR UNABLE TO READ FROM BINARY FILE")