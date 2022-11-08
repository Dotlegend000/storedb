import mysql.connector as c
from prettytable import from_db_cursor


cnx = c.connect(
    host="localhost",
    user="root",
    password="",
    database="store",
    charset="utf8"
)

cr = cnx.cursor()


def empmod():
    src = int(input("Which Employee no is to be modified: "))
    neno = int(input("Enter new Employee no: "))
    nename = input("Enter new Employee name: ")
    nsal = int(input("Enter new Salary: "))

    cr.execute("update emp set eno={},ename='{}',sal={} where eno={}".format(
        neno, nename, nsal, src))

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

    cr.execute('''update item set itemno={},
        itemname='{}',
        price={}
        where itemno={}'''
               .format(nino, niname, np, src)
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

    cr.execute("insert into emp values({},'{}',{})".format(
        eno, ename, sal))

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

    cr.execute("insert into item values({},'{}',{})"
               .format(ino, iname, price))

    if cr.rowcount == 0:
        print("Not Added !!!")
    else:
        print("Successfully Added")
        cr.execute("select * from item where itemno={}".format(ino))
        print(cr.fetchall())

    cnx.commit()


def itemremove():
    cr.execute("select * from item")
    
    i=from_db_cursor(cr)
    print(i)
    
    src = int(input("Enter the item no to remove: "))
    
    cr.execute("delete from item where ino={}"
               .format(src))

    if cr.rowcount == 0:
        print("Not Deleted !!!")
    else:
        print("Successfully Deleted")
        cr.execute("select * from item where ino={}".format(src))
        print(cr.fetchall())

    cnx.commit()


def empremove():
    cr.execute("select * from emp")
    e=from_db_cursor(cr)
    print(e)
    src = int(input("Enter the emp no to remove: "))

    cr.execute("delete from emp where eno={}"
               .format(src))

    if cr.rowcount == 0:
        print("Not Deleted !!!")
    else:
        print("Successfully Deleted")
        cr.execute("select * from emp where eno={}".format(src))
        print(cr.fetchall())

    cnx.commit()


def itemquery():
    cr.execute(
                '''create table bill(
                ino int(3),
                inm varchar(20),
                qty int(2),
                price int(5))'''
            )
    while True:
        src = input("Enter Item name: ")
        cr.execute("select * from item where itemname='{}'".format(src))
        q = cr.fetchone()

        if cr.rowcount == 0:
            print("Item not Found")
        else:
            print("Item no:", q[0], "Item name:", q[1], "Price:", q[2])
            h = int(input("Enter quantity of item: "))
            cr.execute("insert into bill values({},'{}',{},{})".format(
                q[0], q[1], h, q[2]))

            print("Do you have more items ? (Y/N)")
            k = input('Yes(Y) or No(N): ')
            if k not in 'Yy':
                print("Added to Bill")
                cnx.commit()
                cr.execute('select * from bill')
                b = from_db_cursor(cr)
                print(b)
                break
            else:
                continue


# empmod()
# itemmod()
# empadd()
# itemadd()
itemremove()
# empremove()
# itemquery()
# cr.execute('drop table bill')
cnx.close()
