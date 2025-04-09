# agents/view_expansion.py
class ViewExpansionAgent:
    def __init__(self, connection):
        self.connection = connection

    def create_view(self, view_name, sql_definition):
        # 后续实现：创建视图
        return f"视图创建成功：{view_name}"

    def handle(self, command, *args):
        return self.create_view(*args)