import keyboard
import pyperclip
import time
import googleAPI
from plyer import notification
from win10toast import ToastNotifier

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
    toaster.show_toast("翻译结果", translated_text, duration=5)

# 其余代码保持不变


def get_selected_text_on_hotkey(hotkey):
    def on_hotkey_pressed():
        selected_text = get_selected_text()
        print("选中的文本:", selected_text)
        target_language = detect_language(selected_text)
        translated_text = googleAPI.translate(selected_text, target_language)
        print("翻译结果:", translated_text)
        # 显示通知
        show_translation_notification(translated_text)
    # 添加热键监听
    keyboard.add_hotkey(hotkey, on_hotkey_pressed)
    print("程序已启动，请按下 {} 来获取选中的文本。".format(hotkey))
    global running
    while running:
        time.sleep(1)  # 每隔一秒检查一次是否继续运行
    print("程序已关闭。")


get_selected_text_on_hotkey('ctrl+f10')
