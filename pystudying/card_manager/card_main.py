#coding:utf-8
import card_tool
while True:
    # TODO(johney) 显示功能菜单
    card_tool.display_menu()
    action_str = input("请输入想要执行的操作: ")
    print("您选择的操作是：【%s】" % action_str)

    #用户输入123表示相应操作
    if action_str in ["1","2","3"]:
        #新增
        if action_str == "1":
            card_tool.new_card()
            pass
        #显示全部
        elif action_str == "2":
            card_tool.show_card()
            pass
        #查询名片
        elif action_str =="3":
            card_tool.show_card()
            pass
        pass

    #用户输入0退出系统
    elif (action_str == "0"):
        print("欢迎再次使用【名牌管理系统】")
        break

    #输入其它内容，提示输入错误，重新选择
    else:
        print("输入有误，请重新选择")