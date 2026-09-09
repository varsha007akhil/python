
header = """BOOKSTORE RECEIPT
------------------"""

book1 = "Book: {}\tPrice: ₹{}".format("Python Basics", 450)
book2 = "Book: {}\tPrice: ₹{}".format("Data Science Intro", 600)

total = 450 + 600
total_line = "Total: ₹{}".format(total)

receipt = header + "\n" + book1 + "\n" + book2 + "\n" + total_line
receipt = receipt + "\nThank you for shopping!"

print(receipt.upper())