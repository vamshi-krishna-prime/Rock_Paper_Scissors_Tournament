import time

class text():
    def blink(self, string, num):
        self.blank_list = []

        for letter in message:
            self.blank_list.append(" ")
            self.blank_string = "".join(self.blank_list)

        for _ in range(num):
            self.clear = "\b" * len(string)
            print(string, end='', flush=True)
            time.sleep(0.1)
            print(self.clear, end='', flush=True)
            print(self.blank_string, end='', flush=True)
            time.sleep(0.1)
            print(self.clear, end='', flush=True)
        print(string)


    def spin(self, string, num):
        self.clear = "\b"*(4 + len(string))
        for _ in range(num):
            for ch in '-\\|/':
                print(ch + ch + string + ch + ch, end='', flush=True)
                time.sleep(0.1)
                print(self.clear, end='', flush=True)
                # example of print statement for string = " Game start "
                # print('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b', end='', flush=True)


class Game():
    def print_blink(self, message, num):
        self.blink = text.blink(message, num)


    def print_spin(self, message, num):
        self.spin = text.spin(message, num)


    message = input("Enter the text > ")
    num = int(input("No.of times to repeat > "))

    print_blink(message, num)
    print_spin(message, num)

game = Game()

# if __name__ == '__main__':
#     message = input("Enter the text > ")
#     num = int(input("No.of times to repeat > "))
#     print_blink(message, num)
#     print_spin(message, num)
