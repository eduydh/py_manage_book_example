books = [
    {"title": "파이썬 입문", "author": "홍길동", "rented": False},
    {"title": "Git 입문", "author": "김철수", "rented": False},
    {"title": "알고리즘 기초", "author": "이영희", "rented": False},
]


def show_books():
    print("=== 도서 목록 ===")

    for book in books:
        status = "대여중" if book["rented"] else "대여 가능"
        print(f'{book["title"]} - {book["author"]} ({status})')
