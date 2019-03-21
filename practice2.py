a = "Life is too short, you need python"
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:  
    print('shirt')  #'shirt'가 출력되게 되어있음
elif 'need' in a:
    print('need')
else:
    print('none')