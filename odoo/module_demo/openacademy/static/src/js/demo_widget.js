odoo.define('openacademy.Widget',function(require){
    "use strict";


    var FieldChar = require('web.basic_fields').FieldChar;

    var CustomFieldChar = FieldChar.extend({
        _renderReadonly: function(){
            this._super();
            var old_html_render = this.$el.html();
            var new_html_render = '<b style="color:red;">' + old_html_render + ' VND</b>'
            this.$el.html(new_html_render);
        },
    });

    var fieldRegistry = require('web.field_registry');
    fieldRegistry.add('red_color',CustomFieldChar)

});