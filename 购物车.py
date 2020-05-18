salary = input("请输入您的薪水：")
things = [["1、iphone","5000"],
          ["2、macpro","12000"],
          ["3、coffee","31"],
          ["4、book","81"],
          ["5、bike","800"]]
shopping_car = []
balance = int(salary)
while True:
        print(things)
        buy = input("输入您想购买的商品号（如1），如果退出直接输入“out”：")
        if buy == "out":
            print("您已经购买的商品为：")
            print(shopping_car)
            print("你剩下的余额为{ba}".format(ba=balance))
            break
        else:
            number = int(buy) - 1
            if number > 4 or number < 0:
                print("您的输入有错误，请重新输入")
                continue
            if balance >= int(things[number][1]):
                balance = balance - int(things[number][1])
                print("{things}已加入您的购物车，你剩下的余额为{ba}".format(things=things[number][0],ba = balance))
                add = things[number]
                shopping_car.append(add)
            else:
                print("您的余额不足！")
                print("您已经购买的商品为：")
                print(shopping_car)
                print("你剩下的余额为{ba}".format( ba=balance))
                break