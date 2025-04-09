# main.py
import os
import time
from config.load_key import load_key
from openai import OpenAI
from agents import PlanAgent, QueryAgent, DataQualityAgent, ViewExpansionAgent
from services.database import connect, get_table_schemas

def main():
    load_key()
    api_key = os.getenv("DASHSCOPE_API_KEY")
    client = OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )

    connection = connect()
    if not connection:
        print("数据库连接失败")
        return

    # 初始化所有Agent
    query_agent = QueryAgent(client, connection)
    data_quality_agent = DataQualityAgent(connection)
    view_agent = ViewExpansionAgent(connection)
    plan_agent = PlanAgent(
        query_agent=query_agent,
        data_quality_agent=data_quality_agent,
        view_agent=view_agent
    )

    # 获取表结构信息
    schema_info = get_table_schemas(connection)
    print("当前数据库表结构：\n", schema_info)

    while True:
        prompt = input("请输入问题（按回车键结束）：")
        if prompt == "":  # 判断输入是否为空，即用户按了回车键
            break

        try:
            start_time = time.time()
            # 调用Plan Agent决策
            result = plan_agent.execute(prompt, schema_info)
            end_time = time.time()

            print("生成内容：", result.get("sql", ""))
            print("执行结果：", result.get("result", ""))
            print(f"耗时：{end_time - start_time:.2f}秒")
        except Exception as e:
            print(f"错误：{str(e)}")

    connection.close()

if __name__ == "__main__":
    main()