from login import login_page

def test_login():
    assert(login_page("admin","1234")) == "Login successful!"
    assert(login_page("ancy","2222")) == "Invalid credentials."


if __name__ == "__main__":
    test_login()
    print("All login tests passed!")

