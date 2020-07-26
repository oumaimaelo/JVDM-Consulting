odoo.define('website_terms_conditions.terms', function (require) {
"use strict";

    var ajax = require('web.ajax');

    $('.oe_website_sale').each(function () {
        var oe_website_sale = this;
        $('.terms_link').on('click' , function(){
            var term =$('#data_terms_conditions').attr('terms');
            $('.terms').html(term);
            $('.wk_content').html(term);
            $(".wk_content").slideToggle(1000);
        });
        $('#checkbox_terms').on('click', function() {
            if ($(this).prop('checked')) {
                ajax.jsonRpc('/set/check/status', 'call', {
                    'state': true
                })
            } else {
                ajax.jsonRpc('/set/check/status', 'call', {
                    'state': false
                })
            }
        })

        $("#o_payment_form_pay").on('click', function(event){
            var self = $(this);
            var show_terms = $('#data_terms_conditions').attr('show_terms');
            var show_checkbox = $('#data_terms_conditions').attr('show_checkbox');
            if($('#checkbox_terms').prop('checked') != true && show_terms == 'True'  && show_checkbox == 'True')
            {
                event.preventDefault();
                $(this).prop("disabled", "disabled");
                self.popover({
                    content:"<div class='text-center'><span style='color:red'>Accept the Terms and Conditions</span></div>",
                    title:"<div class='text-center bg-primary'><span style='color:red'>WARNING!!</span></div>",
                    html:true,
                    placement:"left",
                    trigger:'focus',
                });
                self.popover('show');
            }
            setTimeout(function() {
                self.popover('dispose');
            },3000);
        });

        $('#checkbox_terms').on('click', function(){
            $("#o_payment_form_pay").prop("disabled", false);
            $("#o_payment_form_pay").popover('dispose');
        });
    });

});
