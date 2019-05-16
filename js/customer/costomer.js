// mui.plusReady(function(){
// 	document.getElementById('phone').onclick=function(){
// 		openNew("addressbook.html")
// 		console.log(123)
// 		// location.href="./addressbook.html"; 
// 	}
// })
//点击跳转到通讯录导入页面
function hrefPhone(){
	document.getElementById('phone').onclick=function(){
		 location.href="./addressbook.html"; 
	}
}
hrefPhone()
//点击跳转到微信导入页面
function hrefwei(){
	document.getElementById('wei').onclick=function(){
		location.href="./addwei.html"; 
	}
}
hrefwei()