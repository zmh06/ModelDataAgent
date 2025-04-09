# agents/plan_agent.py
import re

class PlanAgent:
    def __init__(self, query_agent, data_quality_agent, view_agent):
        self.agents = {
            "query": query_agent,
            "data_quality": data_quality_agent,
            "view": view_agent
        }

    def determine_agent(self, prompt):
        """根据用户输入选择Agent"""
        prompt_lower = prompt.lower()
        print("prompt_lower:", prompt_lower)
        if "数据质量" in prompt_lower or "校验" in prompt_lower:
            return "data_quality"
        elif "视图" in prompt_lower or "创建视图" in prompt_lower:
            return "view"
        else:
            return "query"

    def execute(self, prompt, *args):
        agent_key = self.determine_agent(prompt)
        print("agent_key:", agent_key)
        agent = self.agents[agent_key]
        print("agent:", agent)
        print("handle:", agent.handle(prompt, *args))
        return agent.handle(prompt, *args)