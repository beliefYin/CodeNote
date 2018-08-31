# Tkinter
---
## Text
- Text()  

## Label
- Label(owner, ...)
> @param
> @param string text  --显示的字符串
> @param string bg --背景颜色
> @param string fg --前景颜色
> @param string padx --
> @param string pady --

## Python
#####strip([chars]) 
方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
> @param chars -- 移除字符串头尾指定的字符序列。
> e.g. 
> task_text = self.task_create.get(1.0,tk.END).strip()
> 如果用户是按回车，那么self.task_create.get(1.0,tk.END)这个获取的字符串后面会有个换行符，strip()会返回去掉换行符的字符串