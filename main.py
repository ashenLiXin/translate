import tkinter as tk
from googletrans import Translator
from tkinter import messagebox
import keyboard  # 导入keyboard库

def detect_language(text):
    # 使用googletrans的语言检测功能来确定输入文本的语言
    translator = Translator()
    detected_lang = translator.detect(text).lang
    return detected_lang

def translate_selected_text():
    try:
        # 使用keyboard库获取选中的文本
        selected_text = root.clipboard_get()
        if selected_text.strip():  # 检查选中的文本是否为空
            detected_language = detect_language(selected_text)
            dest_language = 'en' if detected_language == 'zh-CN' else 'zh-CN'
            translator = Translator()
            translated_text = translator.translate(selected_text, dest=dest_language).text
            # 将翻译结果显示在输出文本框中
            output_text.delete("1.0", "end")
            output_text.insert("1.0", translated_text)
    except Exception as e:
        messagebox.showerror("Error", "Translation failed: {}".format(str(e)))

# 创建主窗口
root = tk.Tk()
root.title("自动翻译")

# 输入文本框
input_label = tk.Label(root, text="输入文本:")
input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_entry = tk.Text(root, height=5, width=50)
input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# 输出文本框
output_label = tk.Label(root, text="翻译结果:")
output_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# 监听键盘事件
keyboard.add_hotkey('ctrl+f10', translate_selected_text)

root.mainloop()
