from datetime import datetime

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

# Example usage:
if __name__ == "__main__":
    # Create some authors
    author1 = Author("Alice")
    author2 = Author("Bob")

    # Create some books
    book1 = Book("Book One")
    book2 = Book("Book Two")

    # Create some contracts
    contract1 = author1.sign_contract(book1, "2023-01-01", 10)
    contract2 = author1.sign_contract(book2, "2023-02-01", 15)
    contract3 = author2.sign_contract(book1, "2023-03-01", 20)

    # Get contracts for author1
    print(author1.contracts())  # Output: [contract1, contract2]

    # Get books for author1
    print(author1.books())  # Output: [book1, book2]

    # Get total royalties for author1
    print(author1.total_royalties())  # Output: 25

    # Get contracts by date
    print(Contract.contracts_by_date("2023-01-01"))  # Output: [contract1]

    # Get contracts for book1
    print(book1.contracts())  # Output: [contract1, contract3]

    # Get authors for book1
    print(book1.authors())  # Output: [author1, author2]
