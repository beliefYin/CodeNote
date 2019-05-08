1. 下载lua源码
2. vs新建空的解决方案
3. 创建项目Lualib，Lualib项目中添加lua源码中src里除了lua.c和luac.c的其他c++文件，然后把LuaLib项目属性页中常规里的配置类型改成**静态库(.lib)**,然后生成
4. 创建Lua项目，Lua项目中添加添加lua源码中src里除了luac.c的其他c++文件
5. 创建Luac项目，Luac项目中添加添加lua源码中src里除了lua.c的其他c++文件
6. 设置Lua和Luac项目，如下：打开项目属性页->链接器->常规，添加库目录里加上该解决方案路径下的Debug目录，然后打开链接器->输入,添加附加依赖项Lualib.lib，然后生成Lua和Luac