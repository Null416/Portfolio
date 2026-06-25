from turtle import*

def show_logo():
    speed(0.5)
    pensize(5)

    # Круг
    begin_fill()
    penup()
    goto(0, -150)
    pendown()
    circle(150)
    end_fill()

    #цвет
    color("lime")

    # Буква N
    pensize(12)

    # Левая линия
    penup()
    goto(-50, -40)
    pendown()
    goto(-50, 80)

    # Диагональ
    goto(50, -40)

    # Правая линия
    goto(50, 80)

    # Линия над ником
    pensize(3)
    penup()
    goto(-90, -60)
    pendown()
    goto(90, -60)

    # Ник
    penup()
    goto(-60, -120)
    write("Null416", font=("Arial", 24, "bold"))

    hideturtle()
    done()