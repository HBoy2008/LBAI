var app_config = {
	version: '1.0.0',
	cssAr: [
		'../../css/mui.min.css',
		'../../css/icons-extra.css',
		'../../libs/font-awesome/css/font-awesome.min.css',
		'../../css/common.css',
		'../../css/iconfont.css',
		'../../css/app.css'
	],
	jsAr: [
		'../../js/mui.min.js',
		'../../libs/md5.min.js',
		'../../libs/artTemplate.js',,
		'../../js/app/constants.js',
		'../../js/app/sysUtils.js',
		'../../js/app/common.js',
		'../../js/app/utils.js'
	]
}

// 动态加载解决app重启时候缓存问题。
Array.prototype._distinct = function() {
	var arr = this,
		result = [],
		_result = [],
		len = arr.length;
	arr.forEach(function(v, i, arr) {
		var _v = v.split('/')[v.split('/').length - 1];
		if(_result.indexOf(_v) === -1) {
			result.push(v);
			_result.push(_v);
		} else {
			//替换默认引入文件
			result[_result.indexOf(_v)] = v;
			_result[_result.indexOf(_v)] = _v;
		}
	})
	return result;
};

function link(cssAr, type) {
	var cssAr = type ? cssAr._distinct() : app_config.cssAr.concat(cssAr || [])._distinct();
	for(var i = 0; i < cssAr.length; i++) {
		document.write('<link rel="stylesheet" href="' + cssAr[i] + '?version=' + app_config.version + '"/>');
	}
}

function script(jsAr, type) {
	var jsAr = type ? jsAr._distinct() : app_config.jsAr.concat(jsAr || [])._distinct();
	for(var i = 0; i < jsAr.length; i++) {
		document.write('<script src="' + jsAr[i] + '?version=' + app_config.version + ' type="text/javascript" charset="utf-8"><\/script>');
	}
}