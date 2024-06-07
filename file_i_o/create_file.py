#Read and write files using the built-in python methods



def main():
#open file for writing and create it if it doesnot exist    
    f = open("entreprenure.txt", "w")

    #write some lines of data to the file
    for i in range(1, 10):
        f.write("This line number is %d\r\n" % (i+1))
        print("Testing the main variable")
    f.close()

if __name__ == "__main__":
    main()


# 


