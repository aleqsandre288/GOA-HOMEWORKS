def list_info(nums):
    if len(nums) >= 5:
        print(f"მაქსიმალური რიცხვი: {max(nums)}")
        print(f"მინიმალური რიცხვი: {min(nums)}")
        print(f"რიცხვების ჯამი: {sum(nums)}")
        print(f"list-ის სიგრძე: {len(nums)}")
    else:
        print("გთხოვთ შეიყვანოთ მინიმუმ 5 რიცხვი!")


user_list = [3, 6, 9, 12, 15]
list_info(user_list)
