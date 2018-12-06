#coding=utf-8
from lxml import etree
import chardet
html = '''

<html><head>

<title>京东方Ａ 2.80(-1.41%)_个股资讯_新浪财经_新浪网</title>
<meta name="Keywords" content="京东方A个股资讯,000725个股资讯,新浪财经京东方A(000725)个股资讯">
<meta name="Description" content="新浪财经京东方A(000725)行情中心,为您提供京东方A(000725)个股资讯信息数据查询.">
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">

<link rel="Stylesheet" type="text/css" href="http://vip.stock.finance.sina.com.cn/corp/view/style/hangqing.css">
<link rel="Stylesheet" type="text/css" href="http://vip.stock.finance.sina.com.cn/corp/view/style/dadan.css">
<script src="http://www.sinaimg.cn/dy/js/jquery/jquery-1.7.2.min.js"></script>
<script type="text/javascript" src="http://finance.sina.com.cn/basejs/tool.js"></script>
<script type="text/javascript" src="http://finance.sina.com.cn/basejs/dataDrawer.js"></script>
<script src="http://i.sso.sina.com.cn/js/ssologin.js" type="text/javascript"></script>
<script src="http://finance.sina.com.cn/realstock/company/hotstock_daily_a.js"></script>

<script src="http://finance.sina.com.cn/realstock/company/sz000725/jsvar.js"></script>
<script type="text/javascript">
	var page_name = "个股资讯";
/* BHPsnK7Cm94I1m1LT9oBbUxsAQI/tgPKy65jyFVorJxI+1EIO93Qt424Ixf9wBWPIGXcpKaSbXdJW/qND1DBRMwXtjHUVq5WkIPxRu8dYiHSMhK2rd+G4J8fJTsDMDuXXBGaU/JHe5/+DqKHxzt6MVAozqAWiOvIC008Tg== */
    //HOTSTOCK
	var hq_str_CFF_LIST="IF1309,IF1310,IF1312,IF1403";
    var bkSymbol = '';
    var wbAppKey = '3202088101';
	var mrq_mgsy = 0;
    var flashURL = 'http://finance.sina.com.cn/flash/cn.swf';

	//相关期货
	var RS = {};
	RS.corr_future = [];

/* aakhGmE98ukLIEw8saxPDzCRA32ofQbuZSCS/mEhxJJ8CdDKeSGGpRS/XExuxlvKqKRGdT/GY7cRrGaiEZ4xY8usVStXHA/KsVBPkl4xJZFQW7O8TOLuJ91WOi+jpDPU/MIG4IYQIsfhE2uejazG4F8ciEd+qXI2XPf+h/InzRQvIq3PRXmVN0nl4xTmRk6g1iu8G0RvbF1iCxhOIjk9oQ== */


//综合评级级别
var gradeLevel = 0;
//综合评级研究报告数量 ( TODO PHP写进页面)
var gradeAmt = 0;
//新股发行 增发  配股 现金分红
var bonus=[0,0,0,0];

/* 9P9++LWbuYr1M5AvHjt577edAmFLWT46g9UKY8oyOFZyLqqWUi0c6CWojvDUP1G/VqWML1qq8CKzxAZMYJvZdkjLtMsntNqj2EQPRA2YCAl1KL/qm0X2I7Z1CyNUhRkVpccsindNuPvJQpN1T/GINn5v7hJaxHx9qVcnzwhbvWQptDhrcoow3tbUe752LxxKw9o4PspURwSf6P1rS1cc+ihj6O8rIeHxosuZ8Q== */
</script>

<!--环球市场滚动条，依赖jquery，tool，dataDrawer-->
<script type="text/javascript" src="http://finance.sina.com.cn/basejs/gloabal_index_scroller.js"></script>

<!--搜索建议，无依赖-->
<script type="text/javascript" src="http://finance.sina.com.cn/basejs/suggestServer.js"></script>

<!--登录层，无依赖-->
<script type="text/javascript" src="http://finance.sina.com.cn/basejs/loginLayer.js"></script>

<!--行情页JS，依赖tool,ssologin-->
<!--<script src="http://vip.stock.finance.sina.com.cn/corp/view/script/hangqing.js"></script>-->
<script type="text/javascript" src="http://n.sinaimg.cn/finance/66ceb6d9/20180326/hangqing.js?cn=1.2"></script>


<script type="text/javascript">
//symbol:股票代码，num:单页的数量，page:第几页，sort:排序方式，asc：升序，volume：大单的数量，type：筛选方式，day：日期
var globalFilter = {"symbol":"sz000725", "num": 60, "page":1, "sort":"ticktime", "asc":0, "volume":40000, "amount":0, "type":0, "day":""};
//获取标准北京时间
//var StandardBJTime = Math.round(new Date().getTime() / 1000);
//$.getScript('http://counter.sina.com.cn/time?fm=JS');
</script>
<iframe src="http://beacon.sina.com.cn/ckctl.html" id="ckctlFrame" scrolling="no" style="height: 0px; width: 1px; overflow: hidden;"></iframe></head>
<body>

<div class="wrap">
    <div class="secondaryHeader">
	    <div class="sHBorder">
		    <div class="sHLogo"><span><a href="http://finance.sina.com.cn/"><img src="http://i1.sinaimg.cn/dy/images/header/2009/standardl2nav_sina_new.gif" alt="新浪网"></a><a href="http://finance.sina.com.cn/"><img src="http://i2.sinaimg.cn/dy/images/header/2009/standardl2nav_finance.gif" alt="新浪财经"></a></span></div>
		    <div class="sHLinks"><a href="http://finance.sina.com.cn/">财经首页</a>&nbsp;|&nbsp;<a href="http://www.sina.com.cn/">新浪首页</a>&nbsp;|&nbsp;<a href="http://news.sina.com.cn/guide/">新浪导航</a></div>
	    </div>
    </div>
</div>
<!--end of 头部-->
<!--<div class="wrap topAD">
    <iframe src="http://finance.sina.com.cn/iframe/463/2008/0616/3.html" width="980" height="95" marginheight="0" marginwidth="0" scrolling="no" frameborder="0"></iframe>
</div>
--><!--顶部广告-->
<div class="tui">
	<div class="wrap">
		<script type="text/javascript">
		new GlobalIndexScroller(
			[
				[
					['sh000001','上证指数','cn','rup','http://biz.finance.sina.com.cn/suggest/lookup_n.php?q=sh000001&country=stock','','now,changeP,amount'],
					['sz399001','深证成指','cn','rup','http://biz.finance.sina.com.cn/suggest/lookup_n.php?q=sz399001&country=stock','','now,changeP,amount'],
					['sz399006','创业板指','cn','rup','http://biz.finance.sina.com.cn/suggest/lookup_n.php?q=sz399006&country=stock','','now,changeP,amount'],
					['HSI','恒生指数','hk','gup','http://biz.finance.sina.com.cn/suggest/lookup_n.php?q=HSI&country=hkstock']
				],
				[
					['.dji','道琼斯','us','gup','http://biz.finance.sina.com.cn/suggest/lookup_n.php?q=.dji&country=usstock'],
					['ixic','纳斯达克','us','gup','http://biz.finance.sina.com.cn/suggest/lookup_n.php?q=ixic&country=usstock'],
					['SX5E','斯托克50','b','gup',''],
					['UKX','英金融时报指数','b','gup',''],
					['NKY','日经指数','b','gup','']
				],
				[
					['CL','NYMEX原油','hf','gup','http://finance.sina.com.cn/money/future/CL/quote.shtml'],
					['GC','COMEX黄金','hf','gup','http://finance.sina.com.cn/money/future/quote_hf.html?GC'],
					['SI','COMEX白银','hf','gup','http://finance.sina.com.cn/money/future/quote_hf.html?SI'],
					['CAD','LME铜','hf','gup','http://finance.sina.com.cn/money/future/quote_hf.html?CAD']
				]
			]).stop();
		</script><link rel="stylesheet" href="http://finance.sina.com.cn/basejs/globalIndexScroller.css" type="text/css" id="globalIndexScrollerCss"><div class="global_index_scroller" id="globalIndexScroller0" style="visibility:hidden;"><div class="global_index_scroller_body"></div><div class="scroller_oper"><a href="javascript:void(0)" class="scroller_down"></a><a href="javascript:void(0)" class="scroller_up"></a><a href="http://finance.sina.com.cn/money/globalindex/" target="_blank">环球市场</a></div></div>
	</div>
</div>
<!--end of 环球市场滚动条-->
<div class="nav">
    <div class="wrap">
        <span class="a_right">
			<a href="http://vip.stock.finance.sina.com.cn/mkt/"><font color="#FAD00D">行情中心</font></a>
            <a href="https://gu.sina.cn/pc/feedback/"><font color="#FAD00D">意见反馈</font></a>
        </span>
        <a class="jxDown hideword" id="jxDown" suda-uatrack="key=nc2012_click&amp;value=jxgpc_on">精选股票池</a>
        <a href="http://finance.sina.com.cn/" class="index hideword" target="_blank">财经首页</a><a href="http://finance.sina.com.cn/stock/index.shtml" target="_blank">股票</a><a href="http://finance.sina.com.cn/fund/index.shtml" target="_blank">基金</a><a href="http://finance.sina.com.cn/stock/hkstock/index.shtml" target="_blank">港股</a><a href="http://finance.sina.com.cn/stock/usstock/index.shtml" target="_blank">美股</a><a href="http://finance.sina.com.cn/futuremarket/" target="_blank">期货</a><a href="http://finance.sina.com.cn/forex/" target="_blank">外汇</a><a href="http://finance.sina.com.cn/nmetal/" target="_blank">贵金属</a><a href="http://finance.sina.com.cn/bond/" target="_blank">债券</a><span class="spliter"></span><a href="http://finance.sina.com.cn/column/jsy.html" target="_blank">大盘</a><a href="http://finance.sina.com.cn/column/ggdp.html" target="_blank">个股</a><a href="http://finance.sina.com.cn/stock/newstock/index.shtml" target="_blank">新股</a><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vIR_CustomSearch/index.phtml" target="_blank">数据</a><span class="spliter"></span><a href="http://blog.sina.com.cn/lm/stock/" target="_blank">博客</a><a href="http://guba.sina.com.cn/" target="_blank">股吧</a><span class="spliter"></span><a href="http://vip.stock.finance.sina.com.cn/portfolio/main.php" target="_blank">自选股</a>
    </div>
</div>
<!--end of 导航-->
<div class="assistant">
	<div class="wrap clearfix">
		<div class="assistant-title">投资助手：</div>
        <div class="assistant-wrap">
        	<ul>
            	<li><a href="http://vip.stock.finance.sina.com.cn/moneyflow/" target="_blank" title="资金流向">资金流向</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml" target="_blank" title="业绩报表">业绩报表</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml" target="_blank" title="业绩预告">业绩预告</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/xsjj/index.phtml" target="_blank" title="限售解禁">限售解禁</a></li>
				<li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vRPD_NewStockIssue/page/1.phtml" target="_blank" title="新股申购">新股申购</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill_sum.php" target="_blank" title="实时大单">实时大单</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/fund_center/index.html#jjcczcg" target="_blank" title="基金重仓">基金重仓</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/rzrq/index.phtml" target="_blank" title="融资融券">融资融券</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lhb/index.phtml" target="_blank" title="龙虎榜">龙虎榜</a></li>
				<li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/dzjy/index.phtml" target="_blank" title="大宗交易">大宗交易</a></li>
				<li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/nbjy/index.phtml" target="_blank" title="内部交易">内部交易</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/mkt/#stock_hs_up" target="_blank" title="涨幅排行">涨幅排行</a></li>
				<li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/qgqp/index.phtml" target="_blank" title="千股千评">千股千评</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vPerformancePrediction/kind/eps/index.phtml" target="_blank" title="业绩预测">业绩预测</a></li>
				<li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vIR_RatingNewest/index.phtml" target="_blank" title="券商评级">券商评级</a></li>
                <li><a href="http://screener.finance.sina.com.cn/?f=stock" target="_blank" title="条件选股">条件选股</a></li>
                <li><a href="http://vip.stock.finance.sina.com.cn/datacenter/hqstat.html#jdgd" target="_blank" title="阶段统计">阶段统计</a></li>
                <li><a href="http://finance.sina.com.cn/money/globalindex/" target="_blank" title="环球股指">环球股指</a></li>
                <li><a href="http://finance.sina.com.cn/qizhi/hs300.html" target="_blank" title="沪深300">沪深300</a></li>
                <li><a href="http://biz.finance.sina.com.cn/company/compare/compare.php?stock_code=000001" target="_blank" title="财务对比">财务对比</a></li>
            </ul>
        </div>
        <a href="javascript:;" class="prevBtn" style="display: none;">上一组</a>
        <a href="javascript:;" class="nextBtn">下一组</a>
	</div>
</div>
<!--end of 投资助手-->
<style>
.assistant {background:url(http://www.sinaimg.cn/cj/realstock/2012/images/back_r_h.2.png) 0 -176px repeat-x;}
.assistant .wrap {position:relative;}
.assistant-title {float:left; width:80px; height:32px; text-align:right; line-height:32px; color:#0a227a;}
.assistant-wrap {float:left; _display:inline; position:relative; width:840px; height:32px; overflow:hidden; margin-left:30px;}
.assistant-wrap ul {width:9000px; position:absolute; left:0; top:0;}
.assistant-wrap li {float:left; width:60px; text-align:center; line-height:32px;}
.assistant-wrap li a,
.assistant-wrap li a:visited,
.assistant-wrap li a:hover {color:#0a227a;}
.assistant .prevBtn,
.assistant .nextBtn {position:absolute; top:0; height:32px; width:30px; line-height:99; overflow:hidden; background-image:url(http://vip.stock.finance.sina.com.cn/corp/view/images/icon.png);}
.assistant .prevBtn {left:80px; background-position:12px 9px;}
.assistant .nextBtn {right:0px; background-position:10px -21px;}
</style>
<script>
(function($){
	var $prevBtn = $(".assistant .prevBtn");
	var $nextBtn = $(".assistant .nextBtn");
	var $ul = $(".assistant-wrap ul");
	var $aLi = $(".assistant-wrap li");
	var wrapWidth = $(".assistant-wrap").width();
	var totalWidth = $aLi.width() * $aLi.length;
	
	$prevBtn.click(function(){
		var newLeft = $ul.position().left + 60 * 5;
		if(newLeft > 0) {
			$ul.stop().animate({"left":0},function(){
				$nextBtn.show();
				$prevBtn.hide();
			})
			return;
		}
		$ul.stop().animate({"left":newLeft},function(){
			$nextBtn.show();
		});
	})
	
	$nextBtn.click(function(){
		var newLeft = $ul.position().left - 60 * 5;
		if(newLeft < wrapWidth - totalWidth) {
			newLeft = wrapWidth - totalWidth;
			$ul.stop().animate({"left":newLeft},function(){
				$prevBtn.show();
				$nextBtn.hide();
			})
			return;
		}
		$ul.stop().animate({"left":newLeft},function(){
			$prevBtn.show();	
		});
	})
	
	$prevBtn.hide();
	if(totalWidth <= wrapWidth) {
		$nextBtn.hide();	
	}
})(jQuery)
</script>
<div class="topbar">
    <div class="wrap clearfix">
        <div class="crumbs a_blue_d_all">
            <a href="http://finance.sina.com.cn/">新浪财经</a> &gt; <a href="http://finance.sina.com.cn/stock/">新浪股票</a> &gt; <a href="http://finance.sina.com.cn/realstock/company/sz000725/nc.shtml">京东方A</a> &gt; <span>个股资讯</span>
        </div>
        <div class="search">
            <form action="http://biz.finance.sina.com.cn/suggest/lookup_n.php" method="get">
                <input type="text" id="suggest_top" name="q" autocomplete="off" class="txt" onfocus="this.style.color='#333';" onblur="if(this.value == '')this.style.color='';"><input type="submit" class="btn" value="">
                <input type="hidden" name="country" value="stock">
            </form>
            <script type="text/javascript">
                var suggest0 = new SuggestServer();
                suggest0.bind({
                    "input": "suggest_top", //*(必选) 指定suggest绑定的对象 [string|HTMLElement.input]
                    "value": "@2@",
                    //~  "loader": "suggest_loader", // 可指定js读取用的公共容器 [string|HTMLElement]
                    "default": "拼音/代码/名称", // 可指定input默认值 [string] 默认空
                    "type": "stock", // 类型 [string] 例如"stock"、"23"、"11,12"
                    "link": "http://biz.finance.sina.com.cn/suggest/lookup_n.php?country=@type@&q=@code@", // 备选项点击的url 不设置则不可点击 [string]
                    "target" : "_self",
                    "callback": null // 选定提示行时的回调方法，回调该方法时传入当前input内value [function|null]
                });
            </script>
        </div>
        <style>
        #HOTSTOCK_SHOW_DIV {width:360px; height:32px; line-height:32px;}
		#HOTSTOCK_SHOW_DIV h4 {float:left; font-size:12px;}
		#HOTSTOCK_SHOW_DIV ul {float:left;}
		#HOTSTOCK_SHOW_DIV ul li {float:left; width:75px;}
		#HOTSTOCK_SHOW_DIV li a {float:left;}
		#HOTSTOCK_SHOW_DIV li span {float:left; width:20px; height:32px; background-image:url(http://vip.stock.finance.sina.com.cn/corp/view/images/icon.png);}
		#HOTSTOCK_SHOW_DIV li .hot_stock_operator_up {background-position:6px -50px;}
		#HOTSTOCK_SHOW_DIV li .hot_stock_operator_fair {background-position:6px -78px;}
		#HOTSTOCK_SHOW_DIV li .hot_stock_operator_down {background-position:6px -109px;}
        </style>
        <div class="promot a_blue_l_all blue_l">
            <div id="HOTSTOCK_SHOW_DIV">
            	<h4>实时热点：</h4>
            	<ul><li><a href="http://finance.sina.com.cn/realstock/company/sz002288/nc.shtml">超华科技</a><span data-code="sz002288" class="hot_stock_operator_down"></span></li><li><a href="http://finance.sina.com.cn/realstock/company/sz000063/nc.shtml">中兴通讯</a><span data-code="sz000063" class="hot_stock_operator_down"></span></li><li><a href="http://finance.sina.com.cn/realstock/company/sh600635/nc.shtml">大众公用</a><span data-code="sh600635" class="hot_stock_operator_down"></span></li><li><a href="http://finance.sina.com.cn/realstock/company/sh601668/nc.shtml">中国建筑</a><span data-code="sh601668" class="hot_stock_operator_down"></span></li></ul>
            </div>
            <!--end of #HOTSTOCK_SHOW_DIV-->
        </div>
        <!--end of .promot-->
        <script>
        (function(){
			var src = "http://finance.sina.com.cn/realstock/company/hotstock_daily_a.js";
			getScript(src,function(){
				var hotStockDiv = document.getElementById("HOTSTOCK_SHOW_DIV")
				var oUl = hotStockDiv.getElementsByTagName("ul")[0];
				var aSpan = hotStockDiv.getElementsByTagName("span");
				var innerHtmlStr = "";
				var aHot = [];
				var codeStr = "";
				for(var i=0; i<4; i++) {
					aHot.push("s_" + hotstock_daily_a[i][0]);
					innerHtmlStr += '<li><a href="http://finance.sina.com.cn/realstock/company/'+ hotstock_daily_a[i][0] +'/nc.shtml">'+ hotstock_daily_a[i][1] +'</a><span  data-code="' + hotstock_daily_a[i][0] + '"></span></li>';
				}
				oUl.innerHTML = innerHtmlStr;
				codeStr = aHot.join(",");
				checkHotStork();
				setInterval(checkHotStork,6000);

				function checkHotStork() {
					var src = "http://hq.sinajs.cn/list=" + codeStr;
					getScript(src,function(){
						for(var i=0; i<4; i++) {
							var arr = window['hq_str_'+aHot[i]].split(",");
							if(parseFloat(arr[2]) > 0) {
								aSpan[i].className = "hot_stock_operator_up";
							}
							else if(parseFloat(arr[2]) < 0) {
								aSpan[i].className = "hot_stock_operator_down";
							}
							else {
								aSpan[i].className = "hot_stock_operator_fair";
							}
						}
					})
				}
			});
		})()
        </script>
    </div>
</div>
<!--end of .topbar-->

<div class="wrap main_wrap clearfix">

	<div class="L">
        <div class="v_p data_table" id="tcVP">
            <div class="tabs">
                <div class="tab on">最近访问股</div>
                <div class="tab last"><a href="http://watchlist.finance.sina.com.cn/portfolio/view/main.php" target="_blank">自选股</a></div>
            </div>
            <div class="cont a_blue_d_all" style="display:block;">
                <table cellpadding="0" border="0" cellspacing="0">
                    <thead>
                        <tr>
                            <th>名称</th>
                            <th>价格(元)</th>
                            <th><a href="javascript:void(0)" id="sortBtnV" class="">涨跌幅</a></th>
                        </tr>
                    </thead>
                    <tbody id="tbodyVisited"></tbody>
                    <tbody id="tbodyHot">
                        <tr>
                            <td colspan="3" class="hot_title">以下为热门股票</td>
                        </tr>
                    <tr class="row_0"><th><a href="http://finance.sina.com.cn/realstock/company/sz002288/nc.shtml">超华科技</a></th><td>5.63</td><td><span class="down">-9.92%</span></td></tr><tr class="row_1"><th><a href="http://finance.sina.com.cn/realstock/company/sz000063/nc.shtml">中兴通讯</a></th><td>21.09</td><td><span class="down">-0.85%</span></td></tr><tr class="row_0"><th><a href="http://finance.sina.com.cn/realstock/company/sh600635/nc.shtml">大众公用</a></th><td>5.02</td><td><span class="down">-8.23%</span></td></tr><tr class="row_1"><th><a href="http://finance.sina.com.cn/realstock/company/sh601668/nc.shtml">中国建筑</a></th><td>6.00</td><td><span class="down">-0.83%</span></td></tr><tr class="row_0"><th><a href="http://finance.sina.com.cn/realstock/company/sh600518/nc.shtml">康美药业</a></th><td>11.54</td><td><span class="up">1.94%</span></td></tr><tr class="row_1"><th><a href="http://finance.sina.com.cn/realstock/company/sz000622/nc.shtml">恒立实业</a></th><td>7.26</td><td><span class="down">-10.04%</span></td></tr><tr class="row_0"><th><a href="http://finance.sina.com.cn/realstock/company/sz000735/nc.shtml">罗 牛 山</a></th><td>9.41</td><td><span class="up">4.44%</span></td></tr><tr class="row_1"><th><a href="http://finance.sina.com.cn/realstock/company/sh600309/nc.shtml">万华化学</a></th><td>32.79</td><td><span class="down">-0.46%</span></td></tr><tr class="row_0"><th><a href="http://finance.sina.com.cn/realstock/company/sh600604/nc.shtml">市北高新</a></th><td>7.61</td><td><span class="down">-9.94%</span></td></tr><tr class="row_1"><th><a href="http://finance.sina.com.cn/realstock/company/sh601319/nc.shtml">中国人保</a></th><td>6.43</td><td><span class="down">-2.28%</span></td></tr><tr class="row_0"><th><a href="http://finance.sina.com.cn/realstock/company/sh600519/nc.shtml">贵州茅台</a></th><td>610.10</td><td><span class="up">1.31%</span></td></tr><tr class="row_1"><th><a href="http://finance.sina.com.cn/realstock/company/sh600895/nc.shtml">张江高科</a></th><td>14.10</td><td><span class="down">-9.96%</span></td></tr><tr class="row_0"><th><a href="http://finance.sina.com.cn/realstock/company/sh600030/nc.shtml">中信证券</a></th><td>17.45</td><td><span class="down">-0.85%</span></td></tr></tbody>
                </table>
            </div>
            <div class="cont a_blue_d_all">
                <div class="blue_d" id="portLoginFalse">
                    查看自选股请先
                    <a href="javascript:void(0)" id="port_show_login" class="login_btn_s">登录</a>
                </div>
                <div class="" id="portLoginTrue">
                    <div class="port_hq">
                        <table cellpadding="0" border="0" cellspacing="0">
                            <thead>
                                <tr>
                                    <th>名称</th>
                                    <th>价格(元)</th>
                                    <th><a href="javascript:void(0)" id="sortBtnP">涨跌幅</a></th>
                                </tr>
                            </thead>
                            <tbody id="tbodyPort"></tbody>
                        </table>
                    </div>
                    <div class="port_m_link">
                        <a href="http://watchlist.finance.sina.com.cn/portfolio/view/main.php" target="_blank" class="a_blue_d_all">管理自选股</a>
                    </div>
                    <div class="port_nick clearfix a_blue_l_all blue_l">
                        <span id="portNick" title="我是谁？">^_^</span>
                        <a href="javascript:void(0)" id="portLogoutBtn">退出</a>
                    </div>
                </div>
            </div>
        </div>
        <script type="text/javascript">
            visitedAndPort.init();
        </script>
        <div class="spliter_15"></div>

        <div class="title_blue">
            <h2>热点栏目</h2>
        </div>
        <div class="hot_column a_blue_d_all" id="hotColumn">
            <ul class="clearfix li_point"><li data-hot-column="0"><a href="http://finance.sina.com.cn/focus/jyts/index.shtml" target="_blank">交易提示</a></li>
                
                <li data-hot-column="1"><a href="http://finance.sina.com.cn/stock/cpbd/" target="_blank">操盘必读</a></li>
                <li data-hot-column="2"><a href="http://roll.finance.sina.com.cn/finance/zq1/gsjsy/index.shtml" target="_blank">大市评论</a></li>
                <li data-hot-column="3"><a href="http://finance.sina.com.cn/column/ggdp.shtml" target="_blank">个股点评</a></li>
                <li data-hot-column="4"><a href="http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllMemordDetail.php?stockid=000725" target="_blank">公司公告</a></li>
                <li data-hot-column="5"><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/search/index.phtml?symbol=000725&amp;t1=all" target="_blank">研究报告</a></li>
                <li data-hot-column="6"><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vRPD_NewStockIssue/page/1.phtml" target="_blank">新股申购</a></li>
                <li data-hot-column="7"><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/qgqp/index.phtml" target="_blank">千股千评</a></li>
                <li data-hot-column="8"><a href="http://vip.stock.finance.sina.com.cn/moneyflow/#!ssfx!sz000725" target="_blank" style="color:Red">资金流向</a></li>
                <li data-hot-column="9"><a href="http://finance.sina.com.cn/focus/zqbjh/" target="_blank">证券报</a></li>
            </ul>
        </div>
        <script>
        (function(){
			var $aLi = $("#hotColumn li");
			var $ul = $("#hotColumn ul");
			$aLi.click(function(){
				Cookie.set("hotColumn",$(this).data("hotColumn"),{
					expires:30
				});
			})
			var index = Cookie.get("hotColumn");
			$aLi.eq(index).prependTo($ul);
		})()
        </script>
		<div class="spliter_15"></div>

        <div class="louver a_blue_d_all" id="louver">
            <div class="top_oper">
                <a href="javascript:void(0)" id="louverAllUnfold">展开全部</a>
                <a href="javascript:void(0)" id="louverAllFold">收起全部</a>
            </div>
            <div class="louver_sec">
                <div class="sec_title">
                    <h3>投资工具</h3>
                </div>
                <div class="sec_cont">
                    <ul>
                        <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lhb/index.phtml" target="_blank">数据中心</a></li>
						<li style="display: none;"><a href="http://screener.finance.sina.com.cn/?from=cnstock" target="_blank">条件选股</a></li>
                        <li><a href="http://biz.finance.sina.com.cn/company/compare/compare.php?stock_code=000725" target="_blank">财务对比</a></li>
						<li style="display: none;"><a href="http://finance.sina.com.cn/stock/message/gxq/sz000725/ggzd.html" target="_blank">个股诊断</a></li>
                    </ul>
                </div>
                <div class="sec_btn"><!--<a></a>--></div>
            </div>
            <div class="louver_sec">
                <div class="sec_title">
                    <h3>行情走势</h3>
                </div>
                <div class="sec_cont row_num_5">
                    <ul>
                        <li><a href="http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill.php?symbol=sz000725" target="_blank">大单追踪</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradedetail.php?symbol=sz000725" target="_blank">成交明细</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_price.php?symbol=sz000725" target="_blank">分价统计</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_price_history.php?symbol=sz000725" target="_blank">持仓分析</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/000725.phtml" target="_blank">历史交易</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/stockid/000725.phtml" target="_blank">复权交易</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/rzrqstock/index.phtml?symbol=sz000725&amp;bdate=2018-01-01&amp;edate=2018-12-05" target="_blank">融资融券</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/dzjy/index.phtml?symbol=sz000725&amp;bdate=2018-01-01&amp;edate=2018-12-05" target="_blank">大宗交易</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/nbjy/index.phtml?symbol=sz000725&amp;bdate=2018-01-01&amp;edate=2018-12-05" target="_blank">内部交易</a></li>
						<li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/lhbstock/index.phtml?symbol=sz000725&amp;bdate=2018-01-01&amp;edate=2018-12-05" target="_blank">龙虎榜</a></li>
                    </ul>
                </div>
                <div class="sec_btn"></div>
            </div>
            <div class="louver_sec">
                <div class="sec_title">
                    <h3><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/000725.phtml" target="_blank" class="a_blue_d_s">公司资料</a></h3>
                </div>
                <div class="sec_cont">
                    <ul>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/000725.phtml" target="_blank">公司简介</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpManager/stockid/000725.phtml" target="_blank">公司高管</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/000725/menu_num/2.phtml" target="_blank">所属行业</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/000725/menu_num/5.phtml" target="_blank">所属概念</a></li>

                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpRule/stockid/000725.phtml" target="_blank">公司章程</a></li><!--
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/000725/menu_num/0.phtml" target="_blank">证券资料</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/000725.phtml" target="_blank">相关资料</a></li>
                        --><li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpXiangGuan/stockid/000725.phtml" target="_blank">相关证券</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpXiangGuan/stockid/000725.phtml#SSZS" target="_blank">所属指数</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpXiangGuan/stockid/000725.phtml#SSX" target="_blank">所属系别</a></li>
                    </ul>
                </div>
                <div class="sec_btn"><a></a></div>
            </div>
            <div class="louver_sec">
                <div class="sec_title">
                    <h3><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/000725.phtml" target="_blank" class="a_blue_d_s">发行分配</a></h3>
                </div>
                <div class="sec_cont row_num_2">
                    <ul>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/000725.phtml" target="_blank">分红送配</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_NewStock/stockid/000725.phtml" target="_blank">新股发行</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/xsjj/index.phtml?symbol=sz000725" target="_blank">限售解禁</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_AddStock/stockid/000725.phtml" target="_blank">增发</a></li>

<!--                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_TransferableBond/stockid/--><!--.phtml" target="_blank">可转债</a></li>-->
<!--                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_CollectFund/stockid/--><!--.phtml" target="_blank">募资投向</a></li>-->
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_RaiseExplanation/stockid/000725.phtml" target="_blank">招股说明书</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_MarketBulletin/stockid/000725.phtml" target="_blank">上市公告</a></li>
                    </ul>
                </div>
                <div class="sec_btn"><a></a></div>
            </div>
            <div class="louver_sec">
                <div class="sec_title">
                    <h3><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockStructure/stockid/000725.phtml" target="_blank" class="a_blue_d_s">股本股东</a></h3>
                </div>
                <div class="sec_cont">
                    <ul>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockStructure/stockid/000725.phtml" target="_blank">股本结构</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockHolder/stockid/000725/displaytype/30.phtml" target="_blank">主要股东</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/000725/displaytype/30.phtml" target="_blank">流通股东</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_FundStockHolder/stockid/000725/displaytype/30.phtml" target="_blank">基金持股</a></li>
                    </ul>
                </div>
                <div class="sec_btn"><!--<a></a>--></div>
            </div>
            <div class="louver_sec">
                <div class="sec_title">
                    <h3><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/000725.phtml" target="_blank" class="a_blue_d_s">公司公告</a></h3>
                </div>
                <div class="sec_cont row_num_3">
                    <ul>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/000725.phtml" target="_blank">最新公告</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/000725/page_type/ndbg.phtml" target="_blank">年报</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/000725/page_type/zqbg.phtml" target="_blank">半年报</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/000725/page_type/yjdbg.phtml" target="_blank">一季报</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/000725/page_type/sjdbg.phtml" target="_blank">三季报</a></li>
                    </ul>
                </div>
                <div class="sec_btn"><!--<a></a>--></div>
            </div>
            <div class="louver_sec">
                <div class="sec_title">
                    <h3><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/000725/displaytype/4.phtml" target="_blank" class="a_blue_d_s">财务数据</a></h3>
                </div>
                <div class="sec_cont row_num_4">
                    <ul>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/000725/displaytype/4.phtml" target="_blank">财务摘要</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/000725/displaytype/4.phtml" target="_blank">财务指标</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet/stockid/000725/ctrl/part/displaytype/4.phtml" target="_blank">资产负债表</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_ProfitStatement/stockid/000725/ctrl/part/displaytype/4.phtml" target="_blank">利润表</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_CashFlow/stockid/000725/ctrl/part/displaytype/4.phtml" target="_blank">现金流量表</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_AchievementNotice/stockid/000725.phtml" target="_blank">业绩预告</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_DupontAnalysis/stockid/000725/displaytype/10.phtml" target="_blank">杜邦分析</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_BenifitChange/stockid/000725/displaytype/4.phtml" target="_blank">股东权益增减</a></li>
                        <!--
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet_Text/stockid/000725/type/1040.phtml" target="_blank">资产负债表附注</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet_Text/stockid/000725/type/1070.phtml" target="_blank">利润表附注</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet_Text/stockid/000725/type/1079.phtml" target="_blank">现金流量表附注</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FootNotes/stockid/000725.phtml" target="_blank">财务附注</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_BadAccount/stockid/000725/displaytype/4.phtml" target="_blank">坏账准备</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_AssetDevalue/stockid/000725/displaytype/4.phtml" target="_blank">资产减值准备</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_PayTax/stockid/000725/displaytype/4.phtml" target="_blank">应缴增值税</a></li>
                        -->
                    </ul>
                </div>
                <div class="sec_btn">
<!--                    <a></a>-->
                </div>
            </div>
            <div class="louver_sec">
                <div class="sec_title">
                    <h3><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vGP_StockHolderMeeting/stockid/000725.phtml" target="_blank" class="a_blue_d_s">重大事项</a></h3>
                </div>
                <div class="sec_cont row_num_1">
                    <ul>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vGP_StockHolderMeeting/stockid/000725.phtml" target="_blank">股东大会</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vGP_RelatedTrade/stockid/000725.phtml" target="_blank">关联交易</a></li>

                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vGP_Lawsuit/stockid/000725.phtml" target="_blank">诉讼仲裁</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vGP_GetOutOfLine/stockid/000725.phtml" target="_blank">违规记录</a></li>
                        <li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vGP_Assurance/stockid/000725.phtml" target="_blank">对外担保</a></li>
                    </ul>
                </div>
                <div class="sec_btn"><a></a></div>
            </div>
        </div>
    </div>    <!--end of 左侧-->


    <div class="R">
        <div class="block_hq clearfix">
            <div class="hq_L">
                <div class="hq_title">
                    <a href="http://i.finance.sina.com.cn/zixuan,stock" target="_blank" class="a_blue_d_all add_port" id="holdStatus" suda-uatrack="key=nc2012_click&amp;value=addPort">加入自选股</a>
                    <a href="http://stock.finance.sina.com.cn/shortcut.php" target="_blank" title="下载本页面的快捷方式，下次可以直接点击进入" class="a_blue_d_all add_port" onclick="this.href='http://stock.finance.sina.com.cn/shortcut.php?url=' + encodeURIComponent('http://finance.sina.com.cn/realstock/company/sh600376/nc.shtml?f=shortcut') + '&amp;name=' + encodeURIComponent('首开股份(600376)_新浪财经')" style="background-position:0px 5px;padding-left:20px;margin-right:20px;" id="getShortcut" suda-uatrack="key=nc2012_click&amp;value=shortcut">桌面快捷方式</a>
					<a href="http://m.sina.com.cn/m/finance.html" target="_blank" class="a_blue_d_all add_port" style="background-position:0px -27px;padding-left:20px;margin-right:20px;">客户端</a>
					<script type="text/javascript">
					if(/\((iPhone|iPad|iPod)/i.test(navigator.userAgent))
					{
						document.getElementById('getShortcut').style.display = 'none';
					}
					</script>
					<a href="http://finance.sina.com.cn/realstock/company/sz000725/nc.shtml">
                    <h1 id="stockName">京东方Ａ<span>(000725.SZ)</span></h1>
					</a>
					<span class="stock_tip">
											<a title="模拟交易 跟高手一起炒股" class="t_buy" href="http://jiaoyi.sina.com.cn/jy/stock/buy/" target="_blank"><img src="http://www.sinaimg.cn/cj/realstock/2012/images/buy.png" alt=""></a>
					</span>
                </div>

                <div class="hq_details has_limit" id="hq">
                    <div class="price_time">
                        <div class="price clearfix" id="trading">
                            <div class="change">
                                <div id="change" class="down">-0.04</div>
                                <div id="changeP" class="down">-1.41%</div>
                            </div>
                            <div id="arrow" class="arrow arrow_down"></div>
                            <div id="price" class="down">2.80</div>
                            <div class="ud_limit" id="ud_limie">
                                <div>涨停：3.12</div>
                                <div>跌停：2.56</div>
                            </div>
                        </div>
                        <div class="price" id="closed">
                            停牌
                        </div>
                        <div class="time" id="hqTime">
                            2018-12-05 15:26:03
                        </div>
                        <div class="time blue_l" id="hqPause">临时停牌</div>
                    </div>
                    <div class="other" id="hqDetails">
                        <table border="0" cellpadding="0" cellspacing="0">
                            <colgroup>
                                <col width="60">
                                <col width="50">
                                <col width="60">
                                <col width="70">
                                <col width="70">
                                <col width="40">
                            </colgroup>
                            <tbody>
                                <tr>
                                    <th>今&nbsp;&nbsp;开：</th>
                                    <td class="down">2.79</td>
                                    <th>成交量：</th>
                                    <td>227.21万手</td>
                                    <th>振&nbsp;&nbsp;幅：</th>
                                    <td>1.41%</td>
                                </tr>
                                <tr>
                                    <th>最&nbsp;&nbsp;高：</th>
                                    <td class="down">2.82</td>
                                    <th>成交额：</th>
                                    <td>6.36亿元</td>
                                    <th>换手率：</th>
                                    <td>0.67%</td>
                                </tr>
                                <tr>
                                    <th>最&nbsp;&nbsp;低：</th>
                                    <td class="down">2.78</td>
                                    <th>总市值：</th>
                                    <td>974.36亿</td>
                                    <th>市净率：</th>
                                    <td>1.14</td>
                                </tr>
                                <tr>
                                    <th>昨&nbsp;&nbsp;收：</th>
                                    <td>2.84</td>
                                    <th>流通市值：</th>
                                    <td>948.07亿</td>
									<th>市盈率<sup>TTM</sup>：</th>
									<td>21.79</td>
								</tr>
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>

            <div class="hq_R">
            	<a href="http://finance.sina.com.cn/realstock/company/sz000725/nc.shtml"><img id="imgHqImage" src="http://image.sinajs.cn/newchart/small/bsz000725.gif?1543999953097"></a>
            </div>
        </div>
        <script type="text/javascript">hq.init();</script>
		<script type="text/javascript">
			var imgSrc = "http://image.sinajs.cn/newchart/small/b" + window.globalFilter["symbol"] + ".gif?" + (new Date()).getTime();
			setInterval($("#imgHqImage").attr("src",imgSrc), 1 * 60 * 1000);
		</script><style type="text/css">
	#comInfo1 td,
	#comInfo1 th{border: 1px solid #DCE5F4;height: 26px;line-height: 22px;width:100px;}
	#comInfo1 .ct{color:#0A227A;padding-left:10px;}
	#comInfo1 .cc{color:#005CBF;padding-left:10px;}
	#comInfo1 .ccl{color:#005CBF;padding-left:10px;width:590px;}
    .ca{color:#0A227A;font-size:15px;}
</style>
<ul class="r-menu">
	<li class="label">资讯与公告</li>
	<li class="menu-select-on"><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllNewsStock/symbol/sz000725.phtml">个股资讯</a></li>
	<li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/stockIndustryNews/symbol/sz000725.phtml">行业资讯</a></li>
	<li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/000725.phtml">公司公告</a></li>
	<li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/000725/page_type/ndbg.phtml">年度报告</a></li>
	<li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_BulletinZhong/stockid/000725/page_type/zqbg.phtml">中期报告</a></li>
	<li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_BulletinYi/stockid/000725/page_type/yjdbg.phtml">一季度报告</a></li>
	<li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_BulletinSan/stockid/000725/page_type/sjdbg.phtml">三季度报告</a></li>
	<li><a href="http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_FinManDiv/symbol/sz000725.phtml">理财师解读</a></li>
</ul>
<div id="con02-7" class="tagmain" style="margin-top:20px;line-height: 23px;">


	    <table width="100%" border="0" align="center" cellpadding="0" cellspacing="1" class="table2">
      <tbody><tr>
    <td width="60" valign="top">&nbsp;&nbsp;<font style=" font-weight:bold">个股相关资讯:</font></td></tr>
        <tr>
        <td>
        <div class="datelist"><ul>
			&nbsp;&nbsp;&nbsp;&nbsp;2018-12-04&nbsp;00:36&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-12-04/doc-ihmutuec5934783.shtml">北京东方雨虹防水技术股份有限公司关于回购部分社会公众股份的进展公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-12-04&nbsp;00:35&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-12-04/doc-ihprknvs8921651.shtml">北京东方中科集成科技股份有限公司关于发行股份及支付现金购买资产事项获得中国证券监督管理委员会核准批复的公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-12-03&nbsp;07:49&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/chanjing/cyxw/2018-12-03/doc-ihprknvs7298266.shtml">大尺寸液晶面板价格下滑 2019年全球产能仍供过于求</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-12-03&nbsp;01:10&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-12-03/doc-ihprknvs7114651.shtml">揭秘华为核心供应商：比亚迪是后盖独家供应商</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-12-03&nbsp;01:01&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-12-03/doc-ihprknvs7101754.shtml">大尺寸液晶面板价格再下滑 2019年全球产能供过于求</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-12-02&nbsp;14:26&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-12-02/doc-ihmutuec5534270.shtml">合生创展再售北京东城一物业 ?回笼资金降风险？</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-29&nbsp;17:20&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/stock/ggzz/2018-11-29/doc-ihpevhcm3419436.shtml">京东方Ａ现1笔大宗交易 共成交201.45万元</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-28&nbsp;16:05&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-28/doc-ihpevhcm1550440.shtml">美国人发明了手机，中国人发明了手机购物节</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-28&nbsp;00:39&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-28/doc-ihpevhcm0443926.shtml">北京东方园林环境股份有限公司第六届董事会第二十九次会议决议公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-27&nbsp;09:19&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-27/doc-ihmutuec3972274.shtml">传三星找京东方生产新手机的Infinity-O屏幕</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-27&nbsp;01:41&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-27/doc-ihpevhck8534172.shtml">京东方发布 55英寸OLED显示屏 打破韩企垄断</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-27&nbsp;00:40&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-27/doc-ihmutuec3901846.shtml">北京东方园林环境股份有限公司关于重大资产重组的进展公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-26&nbsp;21:11&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-26/doc-ihpevhck8300672.shtml">京东方发布首款55英寸打印超高清OLED显示屏</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-26&nbsp;04:47&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-26/doc-ihmutuec3716441.shtml">京东方发布55寸打印4K OLED显示屏，打破韩企大尺寸OLED领域垄断</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-24&nbsp;01:09&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-24/doc-ihmutuec3090054.shtml">北京东方雨虹防水技术股份有限公司</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-24&nbsp;01:09&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-24/doc-ihpevhck3879757.shtml">北京东方园林环境股份有限公司</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-23&nbsp;13:30&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-23/doc-ihmutuec2915366.shtml">知识产权撬动金融资本同比增长将近400%  中关村知识产权质押贷款金额突破109亿元</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-23&nbsp;01:30&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-23/doc-ihmutuec2761159.shtml">北京东方园林环境股份有限公司关于部分高级管理人员增持公司股票计划实施完成的公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-22&nbsp;22:18&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/stock/hkstock/ggscyd/2018-11-22/doc-ihmutuec2735180.shtml">京东方精电(00710.HK)与京东方订立更新总分包及总采购协议</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-22&nbsp;20:51&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/stock/hyyj/2018-11-22/doc-ihpevhck1781442.shtml">你可能又要换手机 折叠屏A股产业链公司已在行动</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-22&nbsp;00:59&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-22/doc-ihmutuec2421681.shtml">北京东方中科集成科技股份有限公司第四届董事会第八次会议决议公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-20&nbsp;01:20&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-20/doc-ihmutuec1761719.shtml">北京东方中科集成科技股份有限公司2018年第四次临时股东大会决议公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-17&nbsp;04:26&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-17/doc-ihmutuec0960164.shtml">面板行业提前“入冬”  京东方重金健康产业欲破局</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-17&nbsp;03:16&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-17/doc-ihmutuec0955588.shtml">数字化医疗助推健康管理（医疗前沿）</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-17&nbsp;01:50&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-17/doc-ihmutuec0949466.shtml">北京东方雨虹防水技术股份有限公司关于公司股东进行股票质押式回购交易公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-16&nbsp;13:38&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-16/doc-ihmutuec0766299.shtml">大尺寸“中国屏” 占有率将再攀升</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-16&nbsp;04:49&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-16/doc-ihnvukff5863962.shtml">画屏挂客厅  艺术进万家</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-16&nbsp;02:46&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/chanjing/cyxw/2018-11-16/doc-ihnvukff5732390.shtml">面板厂商齐推折叠屏手机 炒作噱头还是产业趋势？</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-16&nbsp;02:34&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-16/doc-ihnvukff5718256.shtml">折叠屏手机明年面市 面板产业迎技术、市场换挡期</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-15&nbsp;21:47&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/stock/hyyj/2018-11-15/doc-ihnvukff5114765.shtml">折叠式屏幕明年大卖？这些A股公司屏幕商称已准备好</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-15&nbsp;08:26&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-15/doc-ihmutuec0294129.shtml">北京房山区将打造生命科技产业基地</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-14&nbsp;14:09&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-14/doc-ihmutuec0089448.shtml">华星光电11代线投产，中国大尺寸产能明年将占全球四成</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-14&nbsp;01:05&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-14/doc-ihmutuea9912425.shtml">山东新华医疗器械股份有限公司关于挂牌出售上海方承医疗器械有限公司股权进展情况的公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-14&nbsp;01:05&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-14/doc-ihmutuea9912418.shtml">北京东方园林环境股份有限公司关于公司员工持股计划存续期即将届满的提示性公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-13&nbsp;03:00&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/stock/s/2018-11-13/doc-ihnstwwr3302378.shtml">京东方董事长或将退休 员工感慨不知公司后续走向</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-13&nbsp;00:30&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-13/doc-ihmutuea9565180.shtml">北京东方园林环境股份有限公司关于重大资产重组的进展公告</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-12&nbsp;19:37&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-12/doc-ihnstwwr1986065.shtml">起底生命汇:靠干细胞赚钱中源协和卷入 投资大鳄参与</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-12&nbsp;19:37&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-12/doc-ihnstwwr1971269.shtml">起底生命汇：靠干细胞赚钱，中源协和卷入，多名投资大鳄参与</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-10&nbsp;09:28&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/chanjing/gsnews/2018-11-10/doc-ihnstwwp9745343.shtml">京东方大手笔投入健康产业 能为与面板业务比肩？</a> <br>&nbsp;&nbsp;&nbsp;&nbsp;2018-11-10&nbsp;00:44&nbsp;&nbsp;<a target="_blank" href="https://finance.sina.com.cn/roll/2018-11-10/doc-ihmutuea8713892.shtml">北京东方中科集成科技股份有限公司关于2018年第四次临时股东大会延期暨增加临时提案的公告</a> <br>		</ul>
		</div>
		<div style="clear: both;"></div>
		<div style="margin-top:10px;float:right;margin-right:100px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		    第1页&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol=sz000725&amp;Page=2">下一页</a>		    </div>
		</td>
      </tr>
    </tbody></table>
    </div>
  </div>
 </div>
 
  <div class="footer">
	<ul>
	    <li>客户服务热线：4006900000 　欢迎批评指正</li>
	    <li>
        	<a target="_blank" href="http://tech.sina.com.cn/focus/sinahelp.shtml">常见问题解答</a>
            <a target="_blank" href="http://net.china.cn/chinese/index.htm">互联网违法和不良信息举报</a>
            <a target="_blank" href="https://gu.sina.cn/pc/feedback/">新浪财经意见反馈留言板</a>
        </li>
        <li></li>
        <li><a href="http://corp.sina.com.cn/chn/">新浪简介</a> | <a href="http://corp.sina.com.cn/eng/">About Sina</a> | <a href="http://emarketing.sina.com.cn/">广告服务</a> | <a href="http://www.sina.com.cn/contactus.html">联系我们</a> | <a href="http://corp.sina.com.cn/chn/sina_job.html">招聘信息</a> | <a href="http://www.sina.com.cn/intro/lawfirm.shtml">网站律师</a> | <a href="http://english.sina.com">SINA English</a> | <a href="https://login.sina.com.cn/signup/signup.php">通行证注册</a> | <a href="http://help.sina.com.cn/">产品答疑</a></li>
		<li>Copyright © 1996-2013 SINA Corporation, All Rights Reserved</li>
	    <li>新浪公司　<a target="_blank" href="http://www.sina.com.cn/intro/copyright.shtml">版权所有</a></li>
	</ul>
	<span class="mianze">新浪财经免费提供股票、基金、债券、外汇等行情数据以及其他资料均来自相关合作方，仅作为用户获取信息之目的，并不构成投资建议。<br>新浪财经以及其合作机构不为本页面提供信息的错误、残缺、延迟或因依靠此信息所采取的任何行动负责。市场有风险，投资需谨慎。</span>
</div>


<div class="loginBG" id="loginBG"></div>
<div class="loginLayer" id="loginLayer">
    <a href="javascript:void(0)" title="关闭" class="login_close" id="loginClose"></a>
    <div class="login_title"></div>
    <div class="login_cont">
        <table border="0" cellpadding="5" cellspacing="0">
            <colgroup>
                <col width="130">
                <col width="305">
            </colgroup>
            <tbody><tr>
                <th>用户名：</th>
                <td><input type="text" class="txt" id="loginName"></td>
            </tr>
            <tr>
                <th>密&nbsp;&nbsp;码：</th>
                <td><input type="password" class="txt" id="loginPSW"></td>
            </tr>
            <tr>
                <th></th>
                <td><label><input type="checkbox" id="loginRemember" checked="checked"> 记录登录状态一个月</label></td>
            </tr>
            <tr>
                <th></th>
                <td>
                    <p><span id="loginError"></span><a href="javascript:void(0)" id="loginBtn" class="login_btn_m">登录</a></p>
                    <div class="login_loginBtn_bg"></div>
                    <div class="login_link0">
                        <a href="http://login.sina.com.cn/getpass.html" target="_blank">找回密码</a>
                        <a href="http://login.sina.com.cn/help.html" target="_blank">登录帮助</a>
                    </div>
                    <div class="login_link1">
                        <p>还不是新浪会员？</p>
                        <div><a href="http://login.sina.com.cn/signup/signup.php?entry=finance&amp;r=" target="_blank" class="reg_btn">新用户注册</a></div>
                    </div>
                </td>
            </tr>
        </tbody></table>
    </div>
</div>
<script type="text/javascript" charset="utf-8" src="http://www.sinaimg.cn/unipro/pub/suda_s_v851c.js"></script><!-- start添加SUDA代码 -->
<script type="text/javascript" src="http://n.sinaimg.cn/finance/hq_SUDA20161010/hqdetail_suda20161010.js"></script>
<!-- end添加SUDA代码 -->

</body></html>

'''
print(type(html))
page = etree.HTML(html.lower().decode('utf-8'))
print(type(page))
print(len(page))
print(page)
trList = page.xpath('//*[@id="con02-7"]/table/tbody/tr[2]/td/div[1]/ul/a/text()')
#trList = page.xpath('/html/body/div[4]/div/div[2]/ul/li[1]/a/text()')
#trList = page.xpath('//div[6]/div[2]/div[2]/div/a/text()')
#trList = page.xpath('/html')
print(trList)
print len(trList)
#for trList_ in trList:
    #print(trList_)
