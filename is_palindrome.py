from collections import deque


def is_palindrome(s):
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    char_deque = deque(cleaned_string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


palindromes = ['Racecar',
               'Madam',
               'Level',
               'Noon',
               'Rotor',
               'Able was I, I saw Elba',
               'No lemon, no melon',
               'Hello',
               'Test',
               'Data',
               'Science']


def main():
    for item in palindromes:
        print("Homework 2 - Task 2 | Is this phrase/word `{}` a palindrome? | {}".format(item, is_palindrome(item)))
    else:
        print(f"Homework 2 - Task 2 | Done")


if __name__ == "__main__":
    print(f"Homework 2 - Task 2 | Starting... ")
    main()
