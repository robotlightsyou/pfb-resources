#! /usr/bin/env python3

'''
diary1 = "Dear Diary, today was a good day."
diary2 = "Dear Diary, it's Rex Manning Day."
diary = []
diary.append("Dear Diary, I still haven't found an optimized method.")
diary.insert(0, diary2)
diary.insert(0, diary1)
print(diary)
print("\n".join(diary))
'''

def main():
    diary1 = "Dear Diary, today was a good day."
    diary2 = "Dear Diary, it's Rex Manning Day."
    diary = []
    diary.append("Dear Diary, I still haven't found an optimized method.")
    diary.insert(0, diary2)
    diary.insert(0, diary1)

    diary = add_entry(diary)
    print_diary(diary)

    new_diary = []
    add_entry(new_diary)
    save_diary(new_diary)
    newer_diary = load_diary()
    print_diary(newer_diary)

def add_entry(my_diary):
    print("What would you like to add to your diary?")
    entry = input(">")
    my_diary.append(entry)
    return my_diary

def print_diary(my_diary):
    print("First with a for loop.")
    for line in my_diary:
        print(line)
    # Here I need an escape character so that my \n print as "\n" and
    # not as a new line.
    print("Now with '\\n'.join().")
    print("\n".join(my_diary))

def save_diary(my_diary):
    with open("sample_diary.txt", "a") as writefile:
        for line in my_diary:
           writefile.write(line + "\n") 

def load_diary():
    with open("sample_diary.txt", "r") as readfile:
        my_diary = readfile.readlines()
        return my_diary


if __name__ == "__main__":
    main()
    