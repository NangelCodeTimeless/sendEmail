import clsEmail

if __name__ == "__main__":
    gmail = clsEmail.Email("smtp.gmail.com", 587)
    gmail.send_email("correatorresn.90@gmail.com", "llllll", "creo que bien")