import os

import mariadb as c
from prettytable import from_db_cursor
from pyfiglet import Figlet

cnx = c.connect(host="localhost", user="root", password="", database="store")

cr = cnx.cursor()




def empmod():
    src = int(input("Which Employee no is to be modified: "))
    neno = int(input("Enter new Employee no: "))
    nename = input("Enter new Employee name: ")
    nsal = int(input("Enter new Salary: "))

    cr.execute(
        "update emp set eno={},ename='{}',sal={} where eno={}".format(
            neno, nename, nsal, src
        )
    )

    if cr.rowcount == 0:
        print("Not Updated !!!")
    else:
        print("Successfully Updated")
        cr.execute("select * from emp where eno={}".format(neno))
        print(cr.fetchall())

    cnx.commit()


def itemmod():
    src = int(input("Which Item no is to be modified: "))
    nino = int(input("Enter new Item no: "))
    niname = input("Enter new Item name: ")
    np = int(input("Enter new Price: "))

    cr.execute(
        """update item set itemno={},
        itemname='{}',
        price={}
        where itemno={}""".format(
            nino, niname, np, src
        )
    )

    if cr.rowcount == 0:
        print("Not Updated !!!")
    else:
        print("Successfully Updated")
        cr.execute("select * from item where itemno={}".format(nino))
        print(cr.fetchall())

    cnx.commit()


def empadd():
    eno = int(input("Enter Employee no: "))
    ename = input("Enter Employee name: ")
    sal = int(input("Enter Salary: "))

    cr.execute("insert into emp values({},'{}',{})".format(eno, ename, sal))

    if cr.rowcount == 0:
        print("Not Added !!!")
    else:
        print("Successfully Added")
        cr.execute("select * from emp where eno={}".format(eno))
        print(cr.fetchall())

    cnx.commit()


def itemadd():
    ino = int(input("Enter new Item no: "))
    iname = input("Enter new Item name: ")
    price = int(input("Enter new Price: "))

    cr.execute("insert into item values({},'{}',{})".format(ino, iname, price))

    if cr.rowcount == 0:
        print("Not Added !!!")
    else:
        print("Successfully Added")
        cr.execute("select * from item where itemno={}".format(ino))
        print(cr.fetchall())

    cnx.commit()


def itemremove():
    cr.execute("select * from item")

    i = from_db_cursor(cr)
    print(i)

    src = int(input("Enter the item no to remove: "))

    cr.execute("delete from item where ino={}".format(src))

    if cr.rowcount == 0:
        print("Not Deleted !!!")
    else:
        print("Successfully Deleted")
        cr.execute("select * from item where ino={}".format(src))
        print(cr.fetchall())

    cnx.commit()


def empremove():
    cr.execute("select * from emp")
    e = from_db_cursor(cr)
    print(e)
    src = int(input("Enter the emp no to remove: "))

    cr.execute("delete from emp where eno={}".format(src))

    if cr.rowcount == 0:
        print("Not Deleted !!!")
    else:
        print("Successfully Deleted")
        cr.execute("select * from emp where eno={}".format(src))
        print(cr.fetchall())

    cnx.commit()


def itemquery():
    s = """create table bill (inm varchar(20),
    qty int(2),
    price int(5))"""
    cr.execute(s)

    while True:
        cr.execute("select * from item")
        i = from_db_cursor(cr)
        print(i)
        src = input("Enter Item name: ")
        k = "select itemname,price from item where itemname='{}'".format(src)
        cr.execute(k)
        q = cr.fetchone()

        if cr.rowcount == 0:
            print("Item not Found")
            break
        else:
            print("Item name:", q[0], "Price:", q[1])
            h = int(input("Enter quantity of item: "))
            cr.execute("insert into bill values('{}',{},{})".format(q[0], h, q[1]))

            print("Do you have more items ? (Y/N)")
            k = input("Yes(Y) or No(N): ")
            if k not in "Yy":
                print("Added to Bill")
                cnx.commit()
                cr.execute("select *,qty*price as tot_price from bill")
                b = from_db_cursor(cr)
                print(b)
                with open("test.csv", "w", newline="") as f_output:
                    f_output.write(b.get_csv_string())
                cr.execute("drop table bill")
                break
            else:
                os.system("clear")
                continue


def ici():
    print(
        """                         ╔═════════════════════════════╗
                         ║                             ║
                         ║     ~ Incorrect Input ~     ║
                         ║                             ║
                         ╚═════════════════════════════╝"""
    )


os.system("clear")

f = Figlet(font="banner3", justify="center")
print(f.renderText("Store"))

print(
    """               ╔═════════════════════════════════════════════╗
               ║                                             ║
               ║          ~ Press Enter For Login ~          ║
               ║                                             ║
               ╚═════════════════════════════════════════════╝"""
)


difffff = input(" ")

os.system("clear")

log = input("\t\t\tEnter username: ")
pas = input("\t\t\tEnter password: ")

os.system("clear")

if log == "admin" and pas == "user":
    print(
        """                          ╔════════════════════════════╗
                          ║          1.Add             ║
                          ║          2.Remove          ║
                          ║          3.Modify          ║
                          ║          4.Exit            ║
                          ╚════════════════════════════╝"""
    )
    while True:
        ch = input("\t\t\tEnter your choice: ")
        os.system("clear")
        if ch == "1":
            print(
                """                             ╔═════════════════════╗
                             ║     1.Items         ║
                             ║     2.Employees     ║
                             ╚═════════════════════╝"""
            )
            cho = input("\t\t\tEnter your choice: ")
            if cho == "1":
                itemadd()
            elif cho == "2":
                empadd()
            else:
                ici()

        elif ch == "2":
            print(
                """                             ╔═════════════════════╗
                             ║     1.Items         ║
                             ║     2.Employees     ║
                             ╚═════════════════════╝"""
            )
            cho = input("\t\t\tEnter your choice: ")
            if cho == "1":
                itemremove()
            elif cho == "2":
                empremove()
            else:
                ici()

        elif ch == "3":
            print(
                """                             ╔═════════════════════╗
                             ║     1.Items         ║
                             ║     2.Employees     ║
                             ╚═════════════════════╝"""
            )
            cho = input("\t\t\tEnter your choice: ")
            if cho == "1":
                itemmod()
            elif cho == "2":
                empmod()
            else:
                ici()
        elif ch == "4":
            break
        else:
            ici()

elif log == "cashier" and pas == "cash":
    while True:
        itemquery()
        ch = input("Do you want to exit (Y/N) : ")
        if ch not in "Yy":
            break
cnx.close()
