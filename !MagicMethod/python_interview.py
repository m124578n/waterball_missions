def main():
    first_number: str = input()
    try:
        first_number: int = int(first_number)
    except:
        main()
    number: str = input()
    numbers: list[str] = number.split(" ")
    if len(numbers) != first_number:
        main()
    else:
        print(numbers)



if __name__ == "__main__":
    main()
