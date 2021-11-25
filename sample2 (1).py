import os
import pickle
import stdiomask
import getpass
def fun(name,password,getpass,stdiomask):

    s = {"username : ", name}
    t = {"password :", password}
    safecode = pickle.dumps([s,t])
    with open("users.json","wb") as f:
        f.write(safecode)
    return safecode

if __name__ == '__main__':
    u = input("Username : ")
    p = stdiomask.getpass("password : ")
    yo_fun = fun(u,p,getpass,stdiomask)
    print (yo_fun)