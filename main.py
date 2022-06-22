pattern1="password"
pattern2="pass"
pattern3="username"
pattern4="key"
pattern5="user"
pattern6="secret"
document=input("Please provide the file location: ")
fo=open(document,"r")
for line in fo.readlines():
    if pattern1 in line:
        print(line)
    elif pattern2 in line:
        print(line)
    elif pattern3 in line:
        print(line)
    elif pattern4 in line:
        print(line)
    elif pattern5 in line:
        print(line)
    elif pattern6 in line:
        print(line)