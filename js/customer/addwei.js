// function checkboxs(){
// 	document.getElementById('boxs').onclick=function(){
// 		this.style.background = "url('../../images/wxz.png') no-repeat";
// 	}
// }
// checkboxs()
//全选框实现逻辑
// function ollCheck(){
// 	document.getElementById('all').onclic=function(){
// 		
// 	}
// }
//全选
// function setAll(){
// 	var chek = document.getElementsByName("checkbox1");
// 	for (var i = 0; i < chek.length; i++) {
// 	         chek[i].checked = true;
// 	     }
// }
// //全不选
// function setNo(){
// 	var chek = document.getElementsByName("checkbox1");
// 	for (var i = 0; i < chek.length; i++) {
// 	         chek[i].checked = false;
// 	     }
// }
// //反选
// function setOthers(){
// 	var chek = document.getElementsByName("checkbox1");
// 	for(var i = 0; i < chek.length; i++){
// 		if(chek[i].checked == false){
// 			chek[i].checked = true;
// 		}else {
// 			chek[i].checked = false
// 		}
// 	}
// }
//全选/全不选操作

    var box = document.getElementById("boxid");
    var chek = document.getElementsByName("checkbox1");
        if(box.checked == false){
            for (var i = 0; i < chek.length; i++) {
                chek[i].checked = false;
            }
        }else{
            for (var i = 0; i < chek.length; i++) {
                chek[i].checked = true;
            }
        }

// setAllNo()