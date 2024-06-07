
def main():
    f = open("entreprenure.txt", "a")
    for i in range(2):
        f.write("Append line %d\r\n" % (i + 1))

    f.close()

if __name__ == "__main__":
    main()
