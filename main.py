import keyboard
import pyperclip
import os
import time
from win10toast import ToastNotifier
from googletrans import Translator

# 设置环境变量，指定 ToastNotifier 后端为 win10toast.uwp.ToastNotifier
os.environ["WIN10TOAST_BACKEND"] = "win10toast.uwp.ToastNotifier"

toaster = ToastNotifier()
# 全局变量，用于控制程序是否继续运行
running = True


def get_selected_text():
    # 模拟按下 Ctrl + C 复制选中的文本
    keyboard.send('ctrl+c')
    # 等待一小段时间，以确保剪贴板内容已经更新
    time.sleep(0.1)
    # 获取剪贴板中的文本
    selected_text = pyperclip.paste()
    return selected_text


def detect_language(text):
    # 判断文本中是否包含中文字符
    if any('\u4e00' <= char <= '\u9fff' for char in text):
        return 'en'  # 如果包含中文字符，则翻译为英文
    else:
        return 'zh-CN'  # 否则翻译为中文


def show_translation_notification(translated_text):
    # 在通知中不包含图标
    toaster.show_toast('', translated_text, duration=5, icon_path='p.ico')


def translate(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text


def get_selected_text_on_hotkey(hotkey):
    def on_hotkey_pressed():
        selected_text = get_selected_text()
        print("选中的文本:", selected_text)
        target_language = detect_language(selected_text)
        translated_text = translate(selected_text, target_language)
        print("翻译结果:", translated_text)
        show_translation_notification(translated_text)

    keyboard.add_hotkey(hotkey, on_hotkey_pressed)
    print("程序已启动，请按下 {} 来获取选中的文本。".format(hotkey))
    global running
    while running:
        time.sleep(1)  # 每隔一秒检查一次是否继续运行
    print("程序已关闭。")


get_selected_text_on_hotkey('ctrl+f10')
