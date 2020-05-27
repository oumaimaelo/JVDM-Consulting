odoo.define('jvdm_consulting_cmdb.FormRenderer', function(require){
"Use strict";

var core = require('web.core');
var FormController = require('web.FormController');
var ListController = require('web.ListController');
var Dialog = require('web.Dialog');
var Sidebar = require('web.Sidebar');
var QWeb = core.qweb;
var rpc = require('web.rpc');


var FormController = FormController.include({

    _onButtonClicked: function (event) {
        var self = this;
/*        $el.click(function () {
            self.trigger_up('button_clicked', {
                attrs: node.attrs,
                record: self.state,
            });
        });*/
        this._super.apply(this, arguments);
        var record = event.data.record;
        if (record.model == 'systeme' && event.data.attrs.name == "run_system"){

            function UrlExists(url, cb){
                jQuery.ajax({
                    url:      url,
                    dataType: 'text',
                    type:     'GET',
                    complete:  function(xhr){
                        if(typeof cb === 'function')
                           cb.apply(this, [xhr.status]);
                    }
                });
            }

            message = "You can easily copy your access to this Website from here:"
            var $content = $(QWeb.render("jvdm_consulting_cmdb.AccessDataCopy", {
                message: message,
                data: record.data
            }));
//           $(website).on("load", function(){
//
//                website.document.getElementById('login').value = this.state.data.ip;
//                website.document.getElementById('password').value = this.state.data.password;
//
//           });
//            website.document.write("hello world");
            var buttons = [
                {
                    text: "Close",
                    classes: 'btn-primary',
                    close: true,
                },
            ];
            dialog = new Dialog(this,{
                size: 'medium',
                buttons: buttons,
                $content: $content,
                title: record.data.name + " Access Data",
            });

            var myInterval;
            var myTimeout;

            dialog.opened().then(function () {
                myInterval = setInterval(function(){
                //                  var count = document.getElementById("countdown").innerText -= 1
                    var progressbar = document.getElementById("progressbar");
                    var progressbar_value = document.getElementById("progressbar_value");
                    var count = Number(progressbar.style.width.slice(0, -1)) + 33.33;
                    if(count >= 99){
                        count = 100;
                        clearInterval(myInterval);
                    }
                    var value = String(count) + "%";
                    progressbar.style.width = value;
                    progressbar_value.innerText = value;
                }, 1000);

                var url = record.data.ip;
                url = ((url.includes('https') || url.includes('http'))? url: 'http://' + url);
                UrlExists(url + "/web/login", function(status){
                    if(status === 200) {
                        myTimeout = setTimeout(function(){window.open(url + "/web/login", "_blank")}, 3500);
                    }
                    else myTimeout = setTimeout(function(){window.open(url, "_blank")}, 3500);
                });


                $content.on('click', '.copy-login', function (ev) {
                    var ip = document.getElementById("system-login");
                    ip.select();
                    ip.setSelectionRange(0, 99999)
                    document.execCommand("copy");
                });

                $content.on('click', '.copy-password', function (ev) {
                    var password = document.getElementById("system-password");
                    password.select();
                    password.setSelectionRange(0, 99999)
                    document.execCommand("copy");
                });
            });
            dialog.on('closed', self, function () {
                clearTimeout(myTimeout);
                clearInterval(myInterval);
            });
            return dialog.open();
        }
    },


});


var ListController = ListController.include({

    _onButtonClicked: function (event) {
        var self = this;
        this._super.apply(this, arguments);
        var record = event.data.record;
        if (record.model == 'systeme' && event.data.attrs.name == "run_system"){

            function UrlExists(url, cb){
                jQuery.ajax({
                    url:      url,
                    dataType: 'text',
                    type:     'GET',
                    complete:  function(xhr){
                        if(typeof cb === 'function')
                           cb.apply(this, [xhr.status]);
                    }
                });
            }

            message = "You can easily copy your access to this Website from here:"
            var $content = $(QWeb.render("jvdm_consulting_cmdb.AccessDataCopy", {
                message: message,
                data: record.data
            }));

            var buttons = [
                {
                    text: "Close",
                    classes: 'btn-primary',
                    close: true,
                },
            ];
            dialog = new Dialog(this,{
                size: 'medium',
                buttons: buttons,
                $content: $content,
                title: record.data.name + " Access Data",
            });

            var myInterval;
            var myTimeout;

            dialog.opened().then(function () {
                myInterval = setInterval(function(){
                    var progressbar = document.getElementById("progressbar");
                    var progressbar_value = document.getElementById("progressbar_value");
                    var count = Number(progressbar.style.width.slice(0, -1)) + 33.33;
                    if(count >= 99){
                        count = 100;
                        clearInterval(myInterval);
                    }
                    var value = String(count) + "%";
                    progressbar.style.width = value;
                    progressbar_value.innerText = value;
                }, 1000);

                var url = record.data.ip;
                url = ((url.includes('https') || url.includes('http'))? url: 'http://' + url);
                UrlExists(url + "/web/login", function(status){
                    if(status === 200) {
                        myTimeout = setTimeout(function(){window.open(url + "/web/login", "_blank")}, 3500);
                    }
                    else myTimeout = setTimeout(function(){window.open(url, "_blank")}, 3500);
                });


                $content.on('click', '.copy-login', function (ev) {
                    var ip = document.getElementById("system-login");
                    ip.select();
                    ip.setSelectionRange(0, 99999)
                    document.execCommand("copy");
                });

                $content.on('click', '.copy-password', function (ev) {
                    var password = document.getElementById("system-password");
                    password.select();
                    password.setSelectionRange(0, 99999)
                    document.execCommand("copy");
                });
            });
            dialog.on('closed', self, function () {
                clearTimeout(myTimeout);
                clearInterval(myInterval);
            });
            return dialog.open();
        }

    },

});


var Sidebar = Sidebar.include({
    _onItemActionClicked: function (item) {
        var self = this;
        if (item.action.model_name == "systeme" && item.action.name == "Run This Systems"){
            this.trigger_up('sidebar_data_asked', {
                callback: function (env) {
                    rpc.query({
                        model: env.model,
                        method: 'read',
                        args: [env.activeIds, ['name','ip','user','password']],
                    }).done(function (datas) {
                        function OpenDialog(datas){
                            data = datas.pop();
                            if (data){
                                function UrlExists(url, cb){
                                    jQuery.ajax({
                                        url:      url,
                                        dataType: 'text',
                                        type:     'GET',
                                        complete:  function(xhr){
                                            if(typeof cb === 'function')
                                               cb.apply(this, [xhr.status]);
                                        }
                                    });
                                }

                                message = "You can easily copy your access to this Website from here:"
                                var $content = $(QWeb.render("jvdm_consulting_cmdb.AccessDataCopy", {
                                    message: message,
                                    data: data
                                }));
                                var buttons = [
                                    {
                                        text: "Close",
                                        classes: 'btn-primary',
                                        close: true,
                                    },
                                ];
                                dialog = new Dialog(this,{
                                    size: 'medium',
                                    buttons: buttons,
                                    $content: $content,
                                    title: data.name + " Access Data",
                                });

                                var myInterval;
                                var myTimeout;

                                dialog.opened().then(function () {
                                    myInterval = setInterval(function(){
                                        var progressbar = document.getElementById("progressbar");
                                        var progressbar_value = document.getElementById("progressbar_value");
                                        var count = Number(progressbar.style.width.slice(0, -1)) + 33.33;
                                        if(count >= 99){
                                            count = 100;
                                            clearInterval(myInterval);
                                        }
                                        var value = String(count) + "%";
                                        progressbar.style.width = value;
                                        progressbar_value.innerText = value;
                                    }, 1000);

                                    var url = data.ip;
                                    url = ((url.includes('https') || url.includes('http'))? url: 'http://' + url);
                                    UrlExists(url + "/web/login", function(status){
                                        if(status === 200) {
                                            myTimeout = setTimeout(function(){window.open(url + "/web/login", "_blank")}, 3500);
                                        }
                                        else myTimeout = setTimeout(function(){window.open(url, "_blank")}, 3500);
                                    });


                                    $content.on('click', '.copy-login', function (ev) {
                                        var ip = document.getElementById("system-login");
                                        ip.select();
                                        ip.setSelectionRange(0, 99999)
                                        document.execCommand("copy");
                                    });

                                    $content.on('click', '.copy-password', function (ev) {
                                        var password = document.getElementById("system-password");
                                        password.select();
                                        password.setSelectionRange(0, 99999)
                                        document.execCommand("copy");
                                    });
                                });
                                dialog.on('closed', self, function () {
                                    clearTimeout(myTimeout);
                                    clearInterval(myInterval);
                                    OpenDialog(datas);
                                });
                                return dialog.open();
                            }
                        };
                        OpenDialog(datas);
                    });
                }
            });
        }
        this._super.apply(this, arguments);
    },
});

});