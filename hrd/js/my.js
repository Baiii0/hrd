var jsonData;
var pos;
var rank1;
var rank2;
var flag; //计时器开始标志
var isHelp;

$("#start").click(function() {
if (document.getElementById("start").innerHTML == "重新开始") {
	clearTimeout(timer);
}
flag = 1;
document.getElementById("sec").innerHTML = 0;
$("img").attr("onClick", "turn(this);");
document.getElementById("start").innerHTML = "重新开始";
$.ajax({
	url: "http://127.0.0.1:5000/getData",
	data: {},
	dataType: "json",
	async: false,
	success: function(data) {
		arr = data["pos"];
		pos = data["white"];
		t = arr.indexOf(pos);
		// 展示图片
		for (i = 0; i < 9; i++) {
			$("#" + i).attr("value", arr[i]);
			if(i==t) $("#" + t).attr("src", "data:image/jpg;base64," + data["wImg"]);
			else $("#" + i).attr("src", "data:image/jpg;base64," + data[arr[i]]);
		}
		pos = t;
		jsonData = data;
		$("#target").text("查看原图");
		$("#succ").attr("class", "");
		$("#succ").attr("role", "");
		$("#succ").text("");
		$("#duizhao").attr("src","data:image/jpg;base64," + jsonData["newImg"]);

		document.getElementById("cnt").innerHTML = 0;
		isHelp = false;
	},
	error: function(XMLHttpRequest, textStatus, errorThrown) {
		alert("error");
	}
});

if (flag == 1) {
	flag = 0;
	var count = 0;
	timer = setInterval(function() {
		count++;
		document.getElementById("sec").innerHTML = showNum(count);
	}, 1000)
}

});

function turn(btn) {
	white_btn = document.getElementById(pos);
	btn_id = btn.id;
	if (pos == btn_id) return;
	if ((btn_id == pos - 3) || (btn_id == parseInt(pos) + parseInt(3)) || (btn_id == pos - 1 && pos != 3 && pos != 6) ||
		(btn_id == parseInt(pos) + parseInt(1) && pos != 2 && pos != 5)) {

		src = white_btn.src;
		white_btn.src = btn.src;
		btn.src = src;

		var tmp = $("#" + pos).attr("value");
		$("#" + pos).attr("value", $("#" + btn_id).attr("value"));
		$("#" + btn_id).attr("value", tmp);

		pos = btn_id;
		k = document.getElementById("cnt").innerHTML;
		document.getElementById("cnt").innerHTML = parseInt(k) + 1;

		// 判断成功
		var flag = 1;
		for (i = 0; i < 9; i++) {
			if ($("#" + i).attr("value") != i) {
				flag = 0;
				break;
			}
		}
		if (flag) {
			$("#succ").attr("class", "alert alert-success");
			$("#succ").attr("role", "alert");
			$("#succ").text("成功解出!");
			//time stop
			clearTimeout(timer);
			//can't move
			$("img").attr("onClick", "");
			document.getElementById("start").innerHTML = "再来一局";
			// 有帮助 不记录
			if(!isHelp) record();
		}
	}
}

function help() {
	// 如果已经还原了
	var arr = new Array(9);
	flag = 1;
	for (i = 0; i < 9; i++){
		arr[i] = $("#" + i).attr("value");
		if(arr[i]!=i) flag=0;
	}
	if(flag) document.getElementById("succ").innerHTML = '您已经成功啦';
	else {
	isHelp = true;
	var jsonString = JSON.stringify(arr);
	$.ajax({
		type: "POST",
		url: "http://127.0.0.1:5000/getPath",
		data: {
			"pos": jsonString,
			"white": arr[pos]
		},
		dataType: "json",
		contentType: "application/x-www-form-urlencoded;charset=UTF-8",
		async: false,
		success: function(data) {
			arr = data;
			var j = 0;
			function fn(){ turn(document.getElementById(arr[j])); j++; }
			for(var i = 0; i < arr.length; i++ ){
		    	setTimeout(fn,i*200)//倍速?
		    }
		},
		error: function(XMLHttpRequest, textStatus, errorThrown) {
			alert("请先开始游戏");
		}
	});
	}
}

function rank(){
	//当前时间 步数 时间
	$.ajax({
			url: "http://127.0.0.1:5000/getRank",
			data: {},
			dataType: "json",
			async: false,
			success: function(data) {
				//空
				rank1=data["step"]
				rank2=data["time"]
				document.getElementById("content").innerHTML=rank1;
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
				alert("error");
			}
		});
}

function record(){
	var date = new Date();
	//id cnt sec
	var step=document.getElementById("cnt").innerHTML;
	var time=document.getElementById("sec").innerHTML;
	$.ajax({
		type: "POST",
		url: "http://127.0.0.1:5000/addRank",
		data: {
			"date": date,
			"step": step,
			"time": time
		},
		dataType: "json",
		contentType: "application/x-www-form-urlencoded;charset=UTF-8",
		async: false,
		success: function(data) {
		},
		error: function(XMLHttpRequest, textStatus, errorThrown) {

		}
	});
}

function stepRank(){
	document.getElementById("content").innerHTML=rank1;
}

function timeRank(){
	document.getElementById("content").innerHTML=rank2;
}

//封装一个处理单位数字的函数
function showNum(num) {
	if (num < 10) {
   		return '0' + num
   	}
   	return num
}


function cancel(){
	if(document.getElementById("yt").innerHTML=="取消原图"){
		document.getElementById("yt").innerHTML="显示原图"
		document.getElementById('duizhao').style.display="none";
	}else{
		document.getElementById("yt").innerHTML="取消原图"
		document.getElementById('duizhao').style.display="";
	}
}