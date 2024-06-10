def count_chars(text):
    res = {}
    for c in text.lower():
        if c.isalpha():
            if c in res:
                res[c] += 1
            else:
                res[c] = 1
    return res


def main(filename="books/frankenstein.txt"):
    with open(filename) as f:
        file_contents = f.read()
        words = file_contents.split()
        chars = count_chars(file_contents)
        sorted_chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)

        print(f"--- Begin report of {filename} ---")
        print(f"{len(words)} words found in the document")
        for char, count in sorted_chars:
            print(f"The {char} character was found {count} times")
        print("--- End of report ---")


main()
