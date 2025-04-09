# PythonProject

ModelDataAgent 是一个基于阿里云大模型 API 构建的智能数据处理项目。它通过 Plan 智能体对任务进行智能分配，协调 QueryAgent、DataQualityAgent、ViewExpansionAgent 等多个智能体协同工作，实现了智能问数、智能数据质量校验和智能修改报表(视图)等功能，为数据处理和分析提供了高效、智能的解决方案。

## 功能特点
- 智能问数：通过自然语言描述需求，自动生成 SQL 查询语句。
- 智能数据质量校验：对查询结果进行数据质量校验，确保准确性和完整性。

## 安装步骤
1. 克隆项目到本地：
```bash
git clone https://github.com/yourusername/PythonProject.git
cd PythonProject