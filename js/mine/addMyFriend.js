var friendid;
mui.init();
mui.plusReady(function() {
	storage.init();
	storageUser.log();
	friendid = appPage.getParam("id");
	document.getElementById("inpt_val").value = "我是" + storageUser.RealName;
	document.getElementById("btn_ok").addEventListener("tap", function() {

		request("/Player/addPlayerFriend", {
				playerid: storageUser.UId,
				friendid: friendid,
				remark: document.getElementById("inpt_val").value.trim()
			},
			function(json) {
				if(json[SysConstants.ERROR_CODE_KEY] == SysConstants.ERROR_CODE_OBJECT.ERROR_CODE_SUCCESS) {
					mui.toast(json[SysConstants.ERROR_MESSAGE_KEY]);
					mui.back();
				} else {
					mui.toast(json[SysConstants.ERROR_MESSAGE_KEY]);
				}
			});

	})
})