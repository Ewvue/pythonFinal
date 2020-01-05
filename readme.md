# PYTHON期末作业技术文档
> github仓库：* [github](https://github.com/PAN-XUE-JIE/pythonFinal)<br/>
> python档链接：* [pythonanywhere](http://panxuejie.pythonanywhere.com)<br/>
> 这个python期末项目我一个做了两个web，一个是Flask，一个是dash。<br/>
> flask在pythonanywhere上已经部署成功，dash的部署经过多次尝试，发现pythonanywhere比较难部署dash，现在在找另外的方法去部署（云服务器），正在努力ing。
##### dash页面的截图
![dash页面截图](https://github.com/PAN-XUE-JIE/pythonFinal/blob/master/dash.png?raw=true)
## HTML档描述
* 一、flask的描述
### 一、flask的描述
* 1、html档的文件分为：可视化数据图html和result响应的html。
* 2、result响应html中：{% for item in the_select_region %}，应用了集合的for循环嵌套，通过for循环来回应py端发起的请求，for循环在数据表中寻找我们输入选择的省份，通过我们选择的省份值，做出回应，给出改省份的全部数据，并且通过和py的交互式画图，实现了数据的可视化，让我们直观的了解到每个省的相关数据。
> <form method="POST" action="地区数据">
>     <select name="the_region_selected">
>         {% for item in the_select_region %}
>             <option value="{{ item }}">{{ item }}</option>
>         {% endfor %}
>     </select>
> <p><input value='点击查看城市数据!' type='SUBMIT'></p>
> </form>

## Python档描述
* 一、flask的描述
* 二、dash的描述
### 一、flask的描述
根据我们自己要做的web应用使用了jinja2，我们为web应用调用了一些已有的函数，然后读取数据df1 = pd.read_csv("sum.csv",encoding = 'UTF-8')，因为想做出一个可交互式的画图，就定义函数，再调用定义的函数去提取数据表中的“province”指标，根据我们自己选择的值，我们可以进一步实现实时交互，放回我们选的省份的所以可视化图。<br/>
在其中使用了数据结构嵌套：
> fig = dfs.iplot(kind="bar", x="province", asFigure=True)
> py.offline.plot(fig, filename="example1.html",auto_open=False)
* 再者，增加了路径，并且定义了函数和返回的路径和值做了推导式，通过POST的方法去发起请求：
> @app.route('/年度结婚数图',methods=['POST'])
> def entry_page1() -> 'html':
>     return render_template('09和18年结婚数对比.html',
>                            the_title='09和18年结婚数对比',
>                            )
这样可以根据我们的主题一步一步引导我们去了解我们分析的主题内容，并且通过可交互式和可视化图来提高我们的互动性，更能全面的让我们了解我们研究的主题。
### 二、dash的描述
首先调用了dash和pandas模块，然后读取数据，通过for的循环遍历来提取数据：
> dcc.Dropdown(
>                 id='xaxis-column',
>                 options=[{'label': i, 'value': i} for i in available_indicators],
>                 value='职位、房价、身份'
>             ),
* 定义x、y轴，提取数据表的数据,和进行了函数的嵌套dff = df[df['Year'] == year_value]：
> @app.callback(
>     Output('indicator-graphic', 'figure'),
>     [Input('xaxis-column', 'value'),
>      Input('yaxis-column', 'value'),
>      Input('xaxis-type', 'value'),
>      Input('yaxis-type', 'value'),
>      Input('year--slider', 'value')])
* 定义数据表的指标，调用定义的x、y轴，进行数据的交互实现，加入了html样式：
> return {
>         'data': [dict(
>             x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
>             y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
>             text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
>             mode='markers',
>             marker={
>                 'size': 15,
>                 'opacity': 0.5,
>                 'line': {'width': 0.5, 'color': 'white'}
>             }
>         )],
## Web App动作描述
* 一、flask的描述
* 二、dash的描述
### 一、flask的描述
在web页面，我们首先可以很直观的看到数据表，刚开始，我们可以通过我们自己对省份的筛选得出筛选省份的全部数据，通过这个可以先了解到我们想要关注的省份的数据情况，并通过了可视化绘图完成了图表的制作，更能全面的了解数据。再者在下面可以在我们的引导下，通过交互式的操作，先一步一步引导我们去了解数据，给我们讲述我们主题的故事，先是通过交互式的体验，可以在数据可视化图上进行交互式操作，给我们讲述了年度省份的结婚数，并涵盖有数据的总结，后一步一步的引导我们去深入主题，通过四个交互式的体验，我们先是可以了解我们的主题故事，最后通过举例分析两省份的数据进行故事的结尾，增强了说服性。
### 二、dash的描述
