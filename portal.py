import sys

def main():
    n = len(sys.argv)

    for arg in sys.argv:
        if (',' in arg or ':' in arg):
            print("Error: please do not use a comma or colon in any arguments")
            return
    if (n < 3):
        print("Error: not enough arguments")
    elif (n > 5):
        print("Error: too many arguments")
    elif (sys.argv[1] == 'AddUser' and n == 4):
        AddUser(sys.argv[2], sys.argv[3])
    elif (sys.argv[1] == 'Authenticate' and n == 4):
        Authenticate(sys.argv[2], sys.argv[3])
    elif (sys.argv[1] == 'SetDomain' and n == 4):
        SetDomain(sys.argv[2], sys.argv[3])
    elif (sys.argv[1] == 'DomainInfo' and n == 3):
        DomainInfo(sys.argv[2])
    elif (sys.argv[1] == 'SetType' and n == 4):
        SetType(sys.argv[2], sys.argv[3])
    elif (sys.argv[1] == 'TypeInfo' and n == 3):
        TypeInfo(sys.argv[2])
    elif (sys.argv[1] == 'AddAccess' and n == 5):
        AddAccess(sys.argv[2], sys.argv[3], sys.argv[4])
    elif (sys.argv[1] == 'CanAccess' and n == 5):
        CanAccess(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Error: Invalid Input")

    return




def AddUser(user, password):
    if (not user):
        print("Error: username missing")
    elif (user_exists(user)):
        print("Error: user exists")
    else:
        with open('users.txt', 'a') as writer:
            writer.write(user + ":" + password + "\n")
        print("Success")
    return


def Authenticate(user, password):
    try:
        with open('users.txt', 'r') as reader:
            for line in reader.readlines():
                name = line.split(":")[0]
                if (name == user):
                    passw = line.split(":")[1].strip()
                    if (passw == password):
                        print("Success")
                        return
                    else:
                        print("Error: bad password")
                        return
    except:
        print("Error: no such user")
        return
    print("Error: no such user")
    return





def SetDomain(user, domain):
    if (user_exists(user) is False):
        print("Error: no such user")
        return
    elif (len(domain) == 0):
        print("Error: missing domain")
        return
    else:
        if (domain_exists(domain)):
            f = open("domains.txt", "r")
            data = f.readlines()
            for i in range(0, len(data)):
                line = data[i]
                dom = line.split(":")[0]
                if (dom == domain):
                    names = "".join(line.split(":")[1]).split(",")
                    for name in names:
                        if (name == user):
                            print("Error: user in domain already")
                            return
                    data[i] = data[i].strip() + user + ",\n"
                    f = open("domains.txt", "w")
                    f.writelines(data)
                    f.close()
                    print("Success")
                    return               
        else:
            f = open("domains.txt", "a")
            f.write(domain + ":" + user + ",\n")
            f.close()
            print("Success")
            return
    return




def DomainInfo(domain):
    if (len(domain) == 0):
        print("Error: missing domain")
        return
    else:
        if (domain_exists(domain)):
            f = open("domains.txt", "r")
            for line in f.readlines():
                dom = line.split(":")[0]
                if (dom == domain):
                    names = "".join(line.split(":")[1]).split(",")
                    for name in names[:-1]:
                        print(name)
                    f.close()
                    return
    return


def SetType(objectname, type):
    if (len(objectname) == 0 or len(type) == 0):
        print("Error: objectname or type is empty")
        return
    elif (type_exists(type)):
        f = open("types.txt", "r")
        data = f.readlines()
        for i in range(0, len(data)):
            line = data[i]
            typ = line.split(":")[0]
            if (typ == type):
                names = "".join(line.split(":")[1]).split(",")
                for name in names:
                    if (name == objectname):
                        print("Error: objectname in type already")
                        return
                data[i] = data[i].strip() + objectname + ",\n"
                f = open("types.txt", "w")
                f.writelines(data)
                f.close()
                print("Success")
                return               
    else:
        f = open("types.txt", "a")
        f.write(type + ":" + objectname + ",\n")
        f.close()
        print("Success")
        return
    return


def TypeInfo(type):
    if (len(type) == 0):
        print("Error: missing type")
        return
    else:
        if (type_exists(type)):
            f = open("types.txt", "r")
            for line in f.readlines():
                typ = line.split(":")[0]
                if (typ == type):
                    names = "".join(line.split(":")[1]).split(",")
                    for name in names[:-1]:
                        print(name)
                    f.close()
                    return
    return


def AddAccess(operation, domain_name, type_name):
    if (not operation):
        print("Error: mising operation")
        return
    elif (not domain_name):
        print("Error: missing domain")
        return
    elif (not type_name):
        print("Error: missing type")
        return
    else:
        if (domain_exists(domain_name) is False):
            f = open('domains.txt', "a")
            f.write(domain_name + ":\n")
            f.close()
        if (type_exists(type_name) is False):
            f = open("types.txt", "a")
            f.write(type_name + ":\n")
            f.close()
        
        f = open("access.txt", "a")
        f.write(operation + ":" + domain_name + ":" + type_name + "\n")
        f.close()
        print("Success")
    return


def CanAccess(operation, user, object):
    f = open("access.txt", "r")
    for line in f.readlines():
        op = line.split(":")[0]
        if (operation == op):
            domain = line.split(":")[1]
            if (user_exists_in_domain(user, domain)):
                type = line.split(":")[2].strip()
                if (object_exists_in_type(object, type)):
                    print("Success")
                    return
    print("Error: access denied")
    return



# Helper Functions
def user_exists_in_domain(user, domain):
    
    try:
        f = open("domains.txt", "r")
    except:
        return False
    
    for line in f.readlines():
        dom = line.split(":")[0]
        if (dom == domain):
            names = "".join(line.split(":")[1]).split(",")
            for name in names[:-1]:
                if (name == user):
                    return True
    return False

def object_exists_in_type(object, type):
    try:
        f = open("types.txt", "r")
    except:
        return False
    
    for line in f.readlines():
        typ = line.split(":")[0]
        if (typ == type):
            names = "".join(line.split(":")[1]).split(",")
            for name in names[:-1]:
                if (name == object):
                    return True
    return False
            
def user_exists(username):
    try:
        with open('users.txt', 'r') as reader:
            for line in reader.readlines():
                name = "".join(line.split(":")[0]).strip()
                if (name == username):
                    return True
    except:
        return False
    return False

def domain_exists(domain):
    try:
        with open('domains.txt', 'r') as reader:
            for line in reader.readlines():
                dom = line.split(":")[0]
                if (dom == domain):
                    return True
    except:
        return False
    return False

def type_exists(type):
    try:
        with open('types.txt', 'r') as reader:
            for line in reader.readlines():
                typ = line.split(":")[0]
                if (typ == type):
                    return True
    except:
        return False
    return False

if __name__ == "__main__":
    main()