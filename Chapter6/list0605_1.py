import tkinter
root = tkinter.Tk()
root.title("おみくじソフト")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="/Users/takaya/Desktop/py_samples/Chapter6/miko.png")
canvas.create_image(400, 300, image=gazou)
root.mainloop()
