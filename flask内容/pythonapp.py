from flask import Flask, render_template, request
import pandas as pd
import plotly as py

df1 = pd.read_csv("sum.csv",encoding = 'UTF-8')


app = Flask(__name__)

# 准备工作

regions_available = list(df1.province.dropna().unique())
# cf.set_config_file(offline=True, theme="ggplot")
# py.offline.init_notebook_mode()



@app.route('/',methods=['GET'])
def hu_run_2019():
    data_str = df1.to_html()
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_region=regions_available)

@app.route('/地区数据',methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region) # 检查用户输入
    dfs = df1.query("province=='{}'".format(the_region))

# 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="province", asFigure=True)
    py.offline.plot(fig, filename="example1.html",auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results2.html',
                            the_plot_all = plot_all,
							# the_plot_all = [],
                            the_res = data_str,
                            the_select_region=regions_available,
                           )
@app.route('/年度结婚数图',methods=['POST'])
def entry_page1() -> 'html':
    return render_template('09和18年结婚数对比.html',
                           the_title='09和18年结婚数对比',
                           )
@app.route('/09与18年分省GDP与房价',methods=['POST'])
def entry_page2() -> 'html':
    return render_template('09与18年分省GDP与房价.html',
                           the_title='09与18年分省GDP与房价',
                           )
@app.route('/09与18年平均工资与房价对比',methods=['POST'])
def entry_page3() -> 'html':
    return render_template('09与18年平均工资与房价对比.html',
                           the_title='09与18年平均工资与房价对比',
                           )
@app.route('/09与18年结婚人数与毕业人数对比',methods=['POST'])
def entry_page4() -> 'html':
    return render_template('09与18年结婚人数与毕业人数对比.html',
                           the_title='09与18年结婚人数与毕业人数对比',
                           )
@app.route('/举例山东和宁夏的数据分析',methods=['POST'])
def entry_page5() -> 'html':
    return render_template('举例山东和宁夏的数据分析.html',
                           the_title='举例山东和宁夏的数据分析',
                           )
if __name__ == '__main__':
    app.run(debug=True,port=8000)
