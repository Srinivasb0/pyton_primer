
def main():
    #open the file and read contents
    f = open("entreprenure.txt", "r")
    #use the read() function to read the content
    content = f.read()
    print(content)

if __name__ == "__main__":
    main()



def read_lines():
    #open the file and read contents
    #f = open("entreprenure.txt", "r")

    #readline reads the individual lines
    #content = f.readlines()
    #print(content)

    #open file with
    with open("entreprenure.txt", "r") as f:
        print(f.readlines())
        #to check wether file is closed are not
    print(f.closed)

    # for i in content:
    #     print(i)
    

if __name__ == "__main__":
    read_lines()


# binary mode
"""
The data is read and written in the form of bytes objects. 
This mode should be used for all files that don’t contain text
"""













