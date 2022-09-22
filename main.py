print('    ___       __       ________      ___      ')
print('   |\  \     |\  \    |\   ____\    |\  \     ')
print('   \ \  \    \ \  \   \ \  \___|    \ \  \    ')
print('    \ \  \  __\ \  \   \ \  \        \ \  \   ')
print('     \ \  \|\__\_\  \   \ \  \____    \ \  \  ')
print('      \ \___________\    \ \____ _\    \ \ _\ ')
print('       \|____________|    \|_______|    \|__| ')
print(' ')
print('Wci 1.0.0 (Sep 22 2022, 9:17:52) [64 bit (AMD64)] on win32')
#引用库
import time
while 1 == 1:#大循环，维持程序运行，只要不break就不会退出
    live=1
    while live == 1:
        x=input('>>>')
        live=2
    if x == 'version':#版本命令
        print('Wci 1.0.0 (Sep 22 2022, 9:17:52) [64 bit (AMD64)] on win32')
    elif 'exit' in x:
        print('exit......')
        time.sleep(1)
        break
    elif 'printf' in x:
        toremove="printf"
        toremove2="'" #删除printf(''),留输入文字
        toremove3="{"
        toremove4="}"
        toremove5='"'
        x=x.replace(toremove,'')
        x=x.replace(toremove2,'')
        x=x.replace(toremove3,'')
        x=x.replace(toremove4,'')
        x=x.replace(toremove5,'')
        print(x)
    else:
        print('"',x,'"','not a legal syntax.')
 
