var scn_data={
		alarm:{alarm:10,fault:10},
		dtu:{ on:150,off:150},
		plc:{on:10,off:10},
		industy:{v1:10,v2:11,v3:12,v3:14,v4:15,v5:17,v6:18},
		online:{v1:10,v2:11,v3:12,v3:14,v4:15,v5:17,v6:18},
		almMsg:[{msg:"2017年5月4日市A区12#机器气压过高报警"},
				{msg:"上海市A区12#机器气压过高报警"},
				{msg:"江苏省12#机器气压过高报警"},
				{msg:"河南省郑州市B区12#机器气压过高报警"},
				{msg:"河南省郑州市B区12#机器气压过高报警"},
				{msg:"河南省郑州市B区12#机器气压过高报警"},
				{msg:"河南省郑州市B区12#机器气压过高报警"}
				],
		msgCnt:[{msg:100,alm:20},
			{msg:200,alm:40},
			{msg:300,alm:50},
			{msg:400,alm:35},
			{msg:400,alm:40},
			{msg:400,alm:11},
			{msg:400,alm:66},
			{msg:100,alm:77},
			{msg:200,alm:88},
			{msg:300,alm:22},
			{msg:400,alm:99},
			{msg:400,alm:100},
			{msg:400,alm:111},
			{msg:400,alm:222},
			{msg:100,alm:333},
			{msg:200,alm:11},
			{msg:300,alm:33},
			{msg:400,alm:55},
			{msg:400,alm:77},
			{msg:400,alm:90}
			],
		map:[{area:"山东",cnt:20},
			{area:"浙江",cnt:40},
			{area:"江苏",cnt:5000},
			{area:"辽宁",cnt:50}
		],
		factoryHeader:[
	        {"categories":"工程名"},
	        {"categories":"位置"},
	        {"categories":"使用单位"},
	        {"categories":"安装时间"},
	        {"categories":"设备号"},
	        {"categories":"操作"}
    	],
		factory:[
			{"company":"黄浦大桥","dtuCnt": "上海黄浦", "plcCnt": "黄浦大桥工程队","dataCnt":"2018.10.08","alarm": 100},
	        {"company":"南浦大桥","dtuCnt": "上海南浦", "plcCnt": "南浦大桥工程队","dataCnt":"2018.10.08","alarm": 150},
	        {"company":"杨浦大桥","dtuCnt": "上海杨浦", "plcCnt": "杨浦大桥工程队","dataCnt":"2018.10.08","alarm": 101},
	        {"company":"东海大桥","dtuCnt": "上海东海", "plcCnt": "东海大桥工程队","dataCnt":"2018.10.08","alarm": 108},
	        {"company":"上海长江大桥","dtuCnt": "上海长江", "plcCnt": "长江大桥工程队","dataCnt":"2018.10.08","alarm": 190},
	        {"company":"金山铁路大桥","dtuCnt": "上海金山", "plcCnt": "金山铁路大桥工程队","dataCnt":"2018.10.08","alarm": 178},
	        {"company":"中国宇宙大桥","dtuCnt": "宇宙中心", "plcCnt": "中心大桥工程队","dataCnt":"2018.10.08","alarm": 250},
	        {"company":"中国宇宙大桥","dtuCnt": 1000,"plcCnt": 800,"dataCnt": 200,"alarm": "无"},
	        {"company":"中国宇宙大桥","dtuCnt": 1000,"plcCnt": 800,"dataCnt": 200,"alarm": "无"},
			{"company":"中国宇宙大桥","dtuCnt": 1000,"plcCnt": 800,"dataCnt": 200,"alarm": "无"}		],
		usermanagerHeader:[
			{"categories":"用户名"},
			{"categories":"密码"},
			{"categories":"负责工程"},
			{"categories":"权限"},
			{"categories":"操作"},
		],
		usermanager:[
			{"username":"mayun","password":"mababa","engineering":"alibaba","usrpermission":"supermanager"},
			{"username":"mahuateng","password":"mababa","engineering":"tencent","usrpermission":"supermanager"},
			{"username":"xiaoxiami","password":"xiaoxiami","engineering":"aha","usrpermission":"ordinary"},
		]
	};
var vm = new Vue({
	el: '#content',
	data: scn_data,
	methods: {
		details: function() {
			
		}
	}
})