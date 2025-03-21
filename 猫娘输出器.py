import tkinter as tk

#   运行脚本时，一个窗口会弹出，里面有一个文本输入框和一个发送按钮。
#   在输入框中输入你想要猫娘输出的句子，然后点击发送按钮。
#   猫娘输出器会在输入框下方显示你输入的句子，并在句子末尾加上“喵~”。
#   你还可以点击输出结果来复制它，这样你就可以将其粘贴到其他地方。

def on_submit(event):
    user_input = entry.get()
    catgirl_output = user_input + "-喵~"
    label.config(text=catgirl_output)
    entry.delete(0, tk.END)
    label.bind('<Button-1>', lambda event: on_click(event, catgirl_output))

def on_click(event, text):
    root.clipboard_clear()
    root.clipboard_append(text)

# 创建主窗口
root = tk.Tk()
root.title("猫娘输出器")

# 设置窗口背景颜色为粉色
root.config(bg='pink')

# 创建输入框
entry = tk.Entry(root, width=50, borderwidth=2, relief="solid")
entry.pack(pady=20)

# 创建提交按钮
submit_button = tk.Button(root, text="发送", command=lambda: on_submit(None))
submit_button.pack(pady=10)

# 创建输出标签
label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack(pady=20)

# 运行主循环
root.mainloop()
# 猫娘输出器

def catgirl_output(text):
    return text + "喵~"

# 用户输入
user_input = input("请输入一句话：")

# 输出结果
output = catgirl_output(user_input)
print(output)

# 允许用户复制输出内容
root = tk.Tk()
root.title("猫娘输出器")
root.geometry("200x100")

label = tk.Label(root, text=output, font=("Helvetica", 16))
label.pack()

root.mainloop()
