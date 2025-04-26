"Latihan 8.6"
def AutoPass(teks=""):
    def generate_password(panjang=8):
        karakter = string.ascii_letters + string.digits
        print(karakter)
        return ''.join(random.choices(karakter, k=panjang))

    email_regex = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    email_list = re.findall(email_regex, teks)

    for email in email_list:
        username = email.split('@')[0]
        password = generate_password()
        print(f"""{email} username: {username} , 
              password: {password}""")