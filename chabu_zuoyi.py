
#插补左移规格化，对于第一象限的逆圆，起点为A(i,0)，终点为B(0,i)
#有bug是正常的，本人码代码时间有限，可能来不及考虑各种情况。目前点坐标只限于4到7
import turtle as t

def draw_axis():
        t.speed(0)
        t.pencolor("purple")
        t.pensize(2)#画笔速度和大小
 
        t.penup()
        t.goto(-250, -250)
        t.pendown()
        t.forward(500)#画X轴
        t.right(135)
        t.forward(10)
        t.backward(10)
        t.left(270)
        t.forward(10)#画X轴箭头

        t.penup()
        t.home()
        t.goto(-250, -250)
        t.pendown()
        t.left(90)
        t.forward(500)#画y轴
        t.right(135)
        t.forward(10)
        t.backward(10)
        t.left(270)
        t.forward(10)
        t.backward(10)#画y轴箭头

        t.penup()
        t.goto(-255,-270)
        t.write('O',align='center')#原点
        
        for i in range(-200,250,50):
                t.penup()
                t.goto(i, -260)
                t.pendown()
                t.goto(i, -250)#画线

                t.penup()
                t.goto(i, -275)
                t.write(int((i+200)/50+1),align='center')#标注刻度
        for i in range(-200,250,50):
                t.penup()
                t.goto(-260, i)
                t.pendown()
                t.goto(-250, i)#画线

                t.penup()
                t.goto(-275, i)
                t.write(int((i+200)/50+1),align='center')#标注刻度

def draw_move_X():
        t.setheading(180)
        t.forward(50)#走一步-△X
        t.right(135)
        t.forward(10)
        t.backward(10)
        t.left(270)
        t.forward(10)
        t.backward(10)#画X轴箭头

def draw_move_Y():

        t.setheading(90)
        t.forward(50)#走一步-△Y
        t.right(135)
        t.forward(10)
        t.backward(10)
        t.left(270)
        t.forward(10)
        t.backward(10)#画Y轴箭头

def draw_move_XY():

        t.setheading(135)
        t.forward(50*pow(2,0.5))#走一步△Y和△X的和
        t.right(135)
        t.forward(10)
        t.backward(10)
        t.left(270)
        t.forward(10)
        t.backward(10)#画Y轴箭头
        
def draw_banyuan():#参考圆曲线
        t.pencolor("blue")
        t.penup()
        t.home()
        t.goto(qi_dian*50-250,-250)
        t.pendown()
        t.left(90)
        t.circle(qi_dian*50,90)
        t.penup()

def to_bin(value, num):
	bin_chars = ""
	temp = value
	for i in range(num):
		bin_char = bin(temp % 2)[-1]
		temp = temp // 2
		bin_chars = bin_char + bin_chars
	return bin_chars.upper()

def main():
        jrx = 0b0000
        jvx = 0b0000
        jex = qi_dian
        
        jry = 0b0000
        jvy = [qi_dian,qi_dian]
        jey = qi_dian
        
        num=1

        yx="0"
        yy="0"          #数据输入及初始化
        
        while jex>0:      #开始插补
            jrx=jvx+jrx
            if jrx>15:
                yx="-△X"
                jrx=jrx-16
                jex=jex-1
                jvy[1]=jvy[0]-1
            else:
                yx="0  "
            print('{:02d}'.format(num),to_bin(jvx,4)," ",to_bin(jrx,4)," ",yx," ",to_bin(jex,3),end=" ")#输出
            num=num+1
            if jey>0:
                jry=jvy[0]+jry
                if jry>15:
                    yy="+△Y"
                    jry=jry-16
                    jey=jey-1
                    jvx=jvx+1
                else:
                    yy="0  "
            print(to_bin(jvy[0],4)," ",to_bin(jry,4)," ",yy," ",to_bin(jey,3))#输出
            jvy[0]=jvy[1]
            if yy == "+△Y" and yx == "-△X":
                    draw_move_XY()
            else:
                    if yx=="-△X":
                            draw_move_X()
                    else:
                            if yy=="+△Y":
                                    draw_move_Y()
            if jey == 0:
                    jry=0
                    yy="0  "
if __name__ == '__main__':
        print("插补左移规格化，对于第一象限的逆圆，起点为A(i,0)，终点为B(0,i)\n下面输入",end="")
        qi_dian = int(input("起点横坐标:"))
        draw_axis()
        t.home()
        draw_banyuan()
        t.penup()
        t.home()
        t.goto(qi_dian*50-250,-250)
        t.pendown()#从起点开始
        main()
    

