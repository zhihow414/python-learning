def convert(text):
    text= text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text
def main():
    text = input("Text: ")        # 可自訂提示文字
    converted = convert(text)     # 呼叫你已定義的函式
    print(converted)              # 印出結果

main()
