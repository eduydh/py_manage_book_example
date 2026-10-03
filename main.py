from books import show_books


def main():
    while True:
        print()
        print("=== 도서 관리 프로그램 ===")
        print("1. 도서 목록")
        print("2. 종료")

        choice = input("선택: ")

        if choice == "1":
            show_books()
        elif choice == "2":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()
