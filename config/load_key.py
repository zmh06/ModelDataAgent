def load_key():
    import os
    import dashscope
    # 仅从环境变量中获取密钥
    DASHSCOPE_API_KEY = os.getenv('DASHSCOPE_API_KEY')
    # 对密钥进行处理，只显示前6位和后2位，中间用**代替
    if DASHSCOPE_API_KEY:
        masked_key = DASHSCOPE_API_KEY[:6] + '**' + DASHSCOPE_API_KEY[-2:]
    else:
        masked_key = 'None'
    print(f"从环境变量中获取的 DASHSCOPE_API_KEY: {masked_key}")  # 添加调试信息
    if DASHSCOPE_API_KEY is None:
        # 提示用户输入密钥
        DASHSCOPE_API_KEY = input("未在环境变量中找到 DASHSCOPE_API_KEY，请输入该密钥：")
        # 设置环境变量
        os.environ['DASHSCOPE_API_KEY'] = DASHSCOPE_API_KEY
    dashscope.api_key = DASHSCOPE_API_KEY

if __name__ == '__main__':
    load_key()