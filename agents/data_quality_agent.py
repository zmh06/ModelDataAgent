# agents/data_quality.py
class DataQualityAgent:
    def __init__(self, connection):
        self.connection = connection

    def validate(self, table_name):
        # 后续实现：校验数据质量
        return f"数据质量校验成功：{table_name}"

    def handle(self, command, *args):
            return self.validate(*args)
