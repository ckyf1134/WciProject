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
#定义异常函数
def error1():
    print('"',x,'"','not a legal syntax.')
def change():
    #等待开发
    print('Finished.')
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
        if "'" in x:
            toremove="printf"
            toremove2="'" #删除printf(''),留输入文字
            toremove3="{"
            toremove4="}"
            toremove5='"'
            x1=x.replace(toremove,'')
            x2=x1.replace(toremove2,'')
            x3=x2.replace(toremove3,'')
            x4=x3.replace(toremove4,'')
            x5=x4.replace(toremove5,'')
            if "'" in x5:#判断是否有无双引号，使用小括号等语法错误
                x6='0f'#数字置空，废弃进程
                error1()
            else:
                x6=x5
            if '(' in x6:
                error1()#用错括号抛出异常
            else:
                if x6 == '0f':
                    1 == 1#不做反应，下方else抛异常
                else:
                    print(str(x6))
        else:
            error1()#抛出所有上方异常
    elif x =='config':
        print('*********************************')#控制系统（包源调整等）
        print('   welcome to use Wci Config')
        print('*********************************')
        print('1.change packges download from')
        print('2.*')#等待开发
        num1=input('please choose number:')
        if num1 == str(1):
            from1=input('URL:')
            change()
        else:
            print('not a legal command')
    else:
        error1()
 
