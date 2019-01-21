import os
import getpass

user = getpass.getuser()
salt_run = "salt '*' shadow.set_password"
passwd = getpass.getpass()

os.system(salt_run + user + passwd)


