# <div align="center">SOURCE CODE

```python
import os
import mysql.connector as c
from prettytable import from_db_cursor
from pyfiglet import Figlet

cnx = c.connect(host="localhost", user="root", password="", database="store")

cr = cnx.cursor()

cr.execute("DROP TABLE IF EXISTS emp")
cr.execute("drop table if exists item")
cr.execute("drop table if exists bill")

e = "CREATE TABLE emp (eno int(5),ename varchar(20),sal int(10))"
cr.execute(e)
cr.execute(
    """INSERT INTO emp VALUES (1,'Aryan',99999),(2,'Bhagath',30000),(3,'Chinmay',70000)"""
)

i = "CREATE TABLE `item` (itemno int(5),itemname varchar(20),price float)"
cr.execute(i)
cr.execute(
    """INSERT INTO `item` VALUES(101,'Apple',10),(102,'Banana',20),(103,'Pen',40)"""
)

s = """create table bill (inm varchar(20),
    qty int(2),
    price int(5))"""
cr.execute(s)


def empmod():
    cr.execute("select * from emp")

    i = from_db_cursor(cr)
    print(i)
    src = int(input("Which Employee no is to be modified: "))
    neno = int(input("Enter new Employee no: "))
    nename = input("Enter new Employee name: ").capitalize()
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
    cr.execute("select * from item")

    i = from_db_cursor(cr)
    print(i)
    src = int(input("Which Item no is to be modified: "))
    nino = int(input("Enter new Item no: "))
    niname = input("Enter new Item name: ").capitalize()
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
    cr.execute("select * from emp")

    i = from_db_cursor(cr)
    print(i)
    eno = int(input("Enter Employee no: "))
    ename = input("Enter Employee name: ").capitalize()
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
    cr.execute("select * from item")

    i = from_db_cursor(cr)
    print(i)
    ino = int(input("Enter new Item no: "))
    iname = input("Enter new Item name: ").capitalize()
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

    cr.execute("delete from item where itemno={}".format(src))

    if cr.rowcount == 0:
        print("Not Deleted !!!")
    else:
        print("Successfully Deleted")
        cr.execute("select * from item where itemno={}".format(src))
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
    while True:
        cr.execute("select * from item")
        i = from_db_cursor(cr)
        print(i)
        src = input("Enter Item name: ").capitalize()
        k = "select itemname,price from item where itemname='{}'".format(src)
        cr.execute(k)
        q = cr.fetchone()

        if cr.rowcount == 0:
            print("Item not Found")
        else:
            print("Item name:", q[0], "Price:", q[1])
            h = int(input("Enter quantity of item: "))
            cr.execute("insert into bill values('{}',{},{})".format(q[0], h, q[1]))

            print("Do you have more items ? (Y/N)")
            k = input("Yes(Y) or No(N): ")
            if k in "Nn":
                print("Added to Bill")
                cnx.commit()
                cr.execute("select *,qty*price as tot_price from bill")
                b = from_db_cursor(cr)
                print(b)
                with open("test.csv", "w", newline="") as f_output:
                    f_output.write(b.get_csv_string())
                cr.execute("drop table bill")
                break
            elif k in "Yy":
                os.system("cls")
                continue
            else:
                ici()


def ici():
    print(
        """                         ╔═════════════════════════════╗
                         ║                             ║
                         ║     ~ Incorrect Input ~     ║
                         ║                             ║
                         ╚═════════════════════════════╝"""
    )


os.system("cls")

while True:
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
    os.system("cls")
    log = input("\t\t\tEnter username: ")
    pas = input("\t\t\tEnter password: ")
    os.system("cls")
    if log == "admin" and pas == "user":
        while True:
            print(
                """                          ╔════════════════════════════╗
                          ║          1.Add             ║
                          ║          2.Remove          ║
                          ║          3.Modify          ║
                          ║          4.Exit            ║
                          ╚════════════════════════════╝"""
            )
            ch = input("\t\t\tEnter your choice: ")
            os.system("cls")
            if ch == "1":
                print(
                    """                             ╔═════════════════════╗
                             ║     1.Items         ║
                             ║     2.Employees     ║
                             ╚═════════════════════╝"""
                )
                cho = input("\t\t\tEnter your choice: ")
                os.system("cls")
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
                os.system("cls")
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
                os.system("cls")
                if cho == "1":
                    itemmod()
                elif cho == "2":
                    empmod()
                else:
                    ici()
            elif ch == "4":
                cnx.close()
                exit()
            else:
                ici()

    elif log == "cashier" and pas == "cash":
        while True:
            itemquery()
            ch = input("Do you want to exit (Y/N) : ")
            if ch in "Yy":
                cnx.close()
                exit()
            elif ch in "Nn":
                continue
            os.system("cls")
```