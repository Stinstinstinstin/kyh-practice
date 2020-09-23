"""
20200923
Kristin
Uppgift 16

Uppgift: Som en del i en polisutredning har ni fått i uppgift att hitta rader i en loggfil som innehåller
texten “BEAR” eller “X-RAY”. Ladda ner bifogad fil, och skriv ett program som listar alla sådana rader.
Vilken mening hittar ni?
"""


def read_file(file_name):
    # Open file
    f = open(file_name, "r")
    return f


def find_words(f, keywords):
    # Takes a file object and a list of key words csv as input
    # Prints all rows that contain a keyword

    number_of_rows_with_keyword = 0
    secret_message = ""
    for row in f:
        for key_word in keywords:
            if key_word in row or key_word in row.upper():
                print(row.replace("\n", ""))
                split_row = row.split(':')
                secret_message += split_row[len(split_row)-1].replace("\n", "")
                number_of_rows_with_keyword += 1
    print("****************************************************************")
    print(f"Found {number_of_rows_with_keyword} rows with suspicious words!")
    print(secret_message.lstrip())
    print("****************************************************************")


def main():
    f = read_file("ex16_system.log")
    find_words(f, ["BEAR", "X-RAY"])
    f.close()


if __name__ == '__main__':
    main()
