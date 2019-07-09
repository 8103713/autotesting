#coding:utf-8
card_list = []
card_menu = ["姓名", "年龄", "性别"]
tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:^10}"

def display_menu():

	"""显示菜单"""
	print("*" * 50)
	print("欢迎使用【名片管理系统】V1.0")
	print("1.新增名片")
	print("2.显示全部")
	print("3.搜索名片")
	print("\n")
	print("0.退出系统")
	print("*" * 50)


def new_card():

	print("新增名片")
	for menu in card_menu:
		info = input("请输入%s： "% menu)
		card_list.append({menu:info})
	print(card_list)

	pass


# TODO(johney) 格式化显示问题未做
def show_card():
	#val = []
	print("显示所有名片")
	print(tplt.format("姓名","年龄","性别",chr(12288)))
	for info in card_list:
		val = [value for key,value in info.items()]
		#val.append(a)
	    print("".join(val), end="\t" * 2)
	#print(tplt.format(val[0],val[1],val[2],chr(12288)))




	pass


def find_card():
	print("搜索名片")
	pass
