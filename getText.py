import keyboard
import pyperclip
import time


def get_selected_text():
    # 模拟按下 Ctrl + C 复制选中的文本
    keyboard.send('ctrl+c')
    # 等待一小段时间，以确保剪贴板内容已经更新
    time.sleep(0.1)
    # 获取剪贴板中的文本
    selected_text = pyperclip.paste()
    return selected_text


def get_selected_text_on_hotkey(hotkey):
    def on_hotkey_pressed():
        selected_text = get_selected_text()
        print("选中的文本:", selected_text)

    # 添加热键监听
    keyboard.add_hotkey(hotkey, on_hotkey_pressed)

    print("程序已启动，请按下 {} 来获取选中的文本。".format(hotkey))
    # 让程序保持运行
    keyboard.wait('esc')


# 调用这个函数并传入所需的热键

