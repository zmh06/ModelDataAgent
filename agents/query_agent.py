# agents/query_agent.py
from services.database import execute_query  # 直接通过项目根目录访问
from openai import OpenAI

class QueryAgent:
    def __init__(self, client, connection):
        self.client = client
        self.connection = connection

    def generate_sql(self, prompt, schema_info):
        """生成SQL语句"""
        response = self.client.chat.completions.create(
            model="qwen-max",
            messages=[
                {
                    "role": "system",
                    "content": f"你是一个NL2SQL工具，根据用户输入生成SQL查询，你的返回结果应当只包含SQL语句，以SELECT开头,以分号结尾，不能包含其他任何内容以下是表结构：\n{schema_info}"
                },
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def execute_and_fetch(self, sql_query):
        """执行SQL并返回结果"""
        return execute_query(self.connection, sql_query)

    def handle(self, prompt, schema_info):
        """完整流程：生成SQL+执行"""
        sql = self.generate_sql(prompt, schema_info)
        result = self.execute_and_fetch(sql)
        return {
            "sql": sql,
            "result": result
        }