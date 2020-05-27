import os
import time
import shutil


# Order
def remain_update(contents, n):
    file = open('menu.txt', 'w')
    for i in range(len(contents)):
        if i == n - 1:
            file.write(contents[i][0] + '\t' + contents[i][1] + '\t' + str(int(contents[i][2]) - 1) + '\n')
        else:
            file.write(contents[i][0] + '\t' + contents[i][1] + '\t' + str(int(contents[i][2])) + '\n')
    file.close()


def process_order():
    if os.stat("menu.txt").st_size == 0:
        print("Please Go to Number 2")
    menu_file = open('menu.txt', 'r')
    lines = menu_file.readlines()
    contents = []
    i = 1
    for line in lines:
        content = line.split()
        name = content[0]
        value = content[1]
        remain = content[2]
        print("Menu ", i, ":", name, '\t', "Value :", value, '\t', "Remain :", remain)
        i += 1
        in_contents = []
        for k in range(3):
            in_contents.append(content[k])
        contents.append(in_contents)
    menu_file.close()

    n = input("Select Menu :")
    remain_update(contents, int(n))

    bill = open('bills.txt', 'a')
    bill.write(str(time.strftime('%c', time.localtime(time.time()))) + '\n')
    bill.close()


# Admin
def login_id(old_id, old_password):
    id_file = open('list.txt', 'r')
    lines = id_file.readlines()
    contents = []
    result = False
    result_id = False
    result_password = False

    for line in lines:
        content = line.split()
        id = content[0]
        password = content[1]
        if id == old_id:
            print("id ok")
            result_id = True
            if password == old_password:
                print("password ok")
                result_password = True
            else:
                result_id = False
                result_password = False
        if result_id == True and result_password == True:
            result = True
        else:
            result = False
    return result


def make_id():
    id_list = open('list.txt', 'a')
    new_id = input("ID :")
    new_password = input("Password :")
    id_list.write(new_id + '\t' + new_password + '\n')
    id_list.close()


def order_add():
    file = open('menu.txt', 'a')
    menu_name = input('Name :')
    menu_price = input('Price :')
    menu_remain = input('Remain :')
    file.write(menu_name.replace(" ", "") + '\t' + menu_price + '\t' + menu_remain + '\n')
    file.close()


def income_print():
    new_file = open('menu.txt', 'r')
    old_file = open('menu_backup.txt', 'r')

    new_lines = new_file.readlines()
    old_lines = old_file.readlines()

    for new_line, old_line in zip(new_lines, old_lines):
        new_content = new_line.split()
        old_content = old_line.split()
        name = new_content[0]
        value = new_content[1]
        new_remain = new_content[2]
        old_remain = old_content[2]
        print("Menu :", name, '\t', "Sale :", int(old_remain) - int(new_remain), '\t', "Sale Value :",
              int(value) * (int(old_remain) - int(new_remain)))
    # for new_line in new_lines:
    #     new_content = new_line.split()
    #     # old_content = old_line.split()
    #     name = new_content[0]
    #     value = new_content[1]
    #     new_remain = new_content[2]
    #     # old_remain = old_content[2]
    #     print("Menu :", name, '\t', "Sale :", int(new_remain), '\t', "Sale Value :", int(value) * int(new_remain))

    new_file.close()
    old_file.close()


def end_print():
    menu_file = open('menu.txt', 'r')
    lines = menu_file.readlines()
    contents = []
    end_check = False
    i = 1
    for line in lines:
        content = line.split()
        remain = content[2]
        if remain == '0':
            print("Finish Sales")
            closed = True
            return closed
            break
        else:
            print("Keep Sales")
    menu_file.close()


def process_admin():
    select_id = input("1.Login, 2.Make ID" + '\n')
    if select_id == "1":
        n = 0
        result = False
        while result == False:
            old_id = input("ID: ")
            old_password = input("password: ")
            result = login_id(old_id, old_password)
            print(result)

            if result == False:
                n += 1
            if n == 2:  # Login 실패시 홈으로
                break

        # Login 성공
        if result == True:
            mode = input("1.Add Menu" + '\t' + "2.Income" + '\t' "3.END" + '\n')
            if mode == '1':
                order_add()
            elif mode == '2':
                income_print()
            elif mode == '3':
                closed = end_print()
                return closed
    elif select_id == "2":
        make_id()



closed = False
shutil.copy("menu.txt", "menu_backup.txt")

while not closed:
    print("Welcome to BME cafe...")
    print("*" * 65)
    print("1. Order")
    print("2. Admin")
    print("*" * 65)

    choice = input("Choose the number:")
    if int(choice) == 1:
        closed = process_order()
    elif int(choice) == 2:
        closed = process_admin()
    else:
        print('Wrong number.. Try again...')

print("closed 영업 종료..")