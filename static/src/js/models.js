odoo.define('same_motion_module.models', function(require) {
	'use strict';
	var models = require('point_of_sale.models');
	var _super_order = models.Order.prototype;
	models.Order = models.Order.extend({
		add_product: function(product, options){
			_super_order.add_product.apply(this, arguments);
			if(product.list_price==0){
				alert('Operacion Invalida, El producto que usted esta ingresando');
			}
		}
	});
});
