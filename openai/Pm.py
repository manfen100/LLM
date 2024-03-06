# 廊坊市燕郊镇的平结线圈设计
# 导入绘图库
import turtle

# 定义颜色列表
colors = ["green", "blue", "white"]

# 定义线圈的半径
radius = 50

# 定义平结的数量
knots = 8

# 定义线的粗细
turtle.pensize(5)

# 隐藏海龟
turtle.hideturtle()

# 加速绘图
turtle.speed(0)

# 画线圈
turtle.circle(radius)

# 移动到线圈上方
turtle.penup()
turtle.sety(radius)
turtle.pendown()

# 旋转一定角度
turtle.left(90 / knots)

# 画平结
for i in range(knots):
    # 选择颜色
    turtle.color(colors[i % len(colors)])
    # 画左边的线
    turtle.forward(radius)
    turtle.right(180 - 360 / knots)
    turtle.forward(radius * 2)
    turtle.backward(radius)
    turtle.left(180 - 360 / knots)
    # 画右边的线
    turtle.forward(radius)
    turtle.left(180 - 360 / knots)
    turtle.forward(radius * 2)
    turtle.backward(radius)
    turtle.right(180 - 360 / knots)
    # 回到线圈上
    turtle.backward(radius)
    # 旋转一定角度
    turtle.right(360 / knots)

# 结束绘图
turtle.done()