# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def CeasersCypher(Currword):
    # Use a breakpoint in the code line below to debug your script.
    import array
    alphabet = ['a' , 'b', 'c' , 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cypher = ""

    for i in range(len(Currword)):
        letter = Currword[i]
        for j in range(len(alphabet)):
            if (letter == alphabet[j]):
                cypher += alphabet[j+3]
    print (cypher)

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('sentence.txt')
    text = file.read()
    CeasersCypher(text)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
