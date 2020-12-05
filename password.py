# 密碼重試程式
# 先在程式碼中 設定好密碼 password = 'a123456'
# 先讓使用者【最多輸入3次密碼】
# 不對的話，就印出'密碼錯誤！還有_次機會'
# 對的話，就印出'登入成功！'
password = 'a123456'
x = 1
while True:
    ans = input('請輸入密碼：')
    if ans != password:
        if x == 1:
            print('密碼錯誤！還有2次機會')
        if x == 2:
            print('密碼錯誤！還有1次機會')
        if x == 3:
            print('密碼錯誤！還有0次機會')
            break
        x = x + 1
    elif ans == password:
        print('登入成功！')
        break