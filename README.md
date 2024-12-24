# 文件上传组件示例

这是一个前端使用Vue 3、Tailwind CSS和shadcn风格实现的文件上传组件示例，后端使用python fastapi框架编写的前后端分析的文件上传demo。

## 功能特点
- 支持拖拽上传
- 支持点击上传
- 文件类型限制为jpg/png
- 文件大小限制为500kb
- 上传区域视觉反馈
- 错误提示

## 技术栈
- Vue 3
- Tailwind CSS
- shadcn UI风格
- python fastapi

## 使用方法
1. 将FileUpload组件导入到您的项目中
2. 在template中使用组件 
3. 使用uvicorn main:app --reload --host 0.0.0.0 --port 8000运行后端服务
4. 不要迁移venv环境直接使用依赖文件安装新的程序