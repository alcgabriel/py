def countdown_to_start():
    countdown = 11
    for i in range(10, 1, -1):
        countdown -= 1
        print(f"{countdown}...")
        if countdown == 2:
            countdown = 1
            print(f"{countdown}...Fight!")
            continue
    return

# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()
