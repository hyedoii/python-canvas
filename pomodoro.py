import tkinter

def getNum():
    x = int(entry.get())
    for i in range(x):
        arc = canvas.create_arc(120, 40, 520, 420, start=90, extent=-(x-i)*6, fill="red", width=3)
        canvas.create_oval(300, 210, 340, 250, fill="black")
        w.update()
        w.after(1000)
        canvas.delete(arc)

w = tkinter.Tk()
w.title("Pomodoro")

canvas = tkinter.Canvas(w, width=640, height=480)
canvas.pack()

canvas.create_oval(120, 40, 520, 420, fill="white", width=3)
arc = canvas.create_arc(120, 40, 520, 420, start=90, extent=0, fill="red", width=3)
canvas.create_oval(300, 210, 340, 250, fill="black")

frame = tkinter.Frame(w)
frame.pack()

entry = tkinter.Entry(canvas)
canvas.create_window(200,140,window=entry)

button = tkinter.Button(text="submit",command=getNum)
canvas.create_window(200,180,window=button)
