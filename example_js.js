customer() {
		var me = this;
		erpnext.utils.get_party_details(this.frm, null, null, function() {
			me.apply_price_list();
		});
	}

	customer_address() {
		erpnext.utils.get_address_display(this.frm, "customer_address");
		erpnext.utils.set_taxes_from_address(this.frm, "customer_address", "customer_address", "shipping_address_name");
	}

	shipping_address_name() {
		erpnext.utils.get_address_display(this.frm, "shipping_address_name", "shipping_address");
		erpnext.utils.set_taxes_from_address(this.frm, "shipping_address_name", "customer_address", "shipping_address_name");
	}

	dispatch_address_name() {
		erpnext.utils.get_address_display(this.frm, "dispatch_address_name", "dispatch_address");
	}

	sales_partner() {
		this.apply_pricing_rule();
	}

const { Sequelize, DataTypes } = require('sequelize');
const db = require('../utils/database');
const Customer = require('./customerModel');

// Sequelize model for Customer_Address table
const CustomerAddress = db.define(
	'customer_add_tbl',
	{
		id: {
			type: DataTypes.BIGINT,
			autoIncrement: true,
			primaryKey: true
		},
		locality: {
			type: DataTypes.STRING(200),
		},
		city: {
			type: DataTypes.STRING(45),
		},
		state: {
			type: DataTypes.STRING(45),
		},
		pincode: {
			type: DataTypes.BIGINT,
		},
		lat: {
			type: DataTypes.DECIMAL(10, 0),
		},
		long: {
			type: DataTypes.DECIMAL(10, 0),
		},
		isHomeAddress: {
			type: DataTypes.TINYINT(1),
		}
	},
	{
		timestamps: true,
		createdAt: 'created_at',
		updatedAt: 'modified_at',
		freezeTableName: true
	}
);
var DeviceFingerprint = function(type, device, fingerprint) {
  lan.utils.merge(this, fingerprint);
  lan.utils.merge(this, device);

  /*
   * Starts the Fingerprint request
   * @param [String] base the https:// or http:// base URL
   * @param [Function(statusBoolean)] callback
   */
  this.check = function(opts, callback) {
    var Probe = this.constructor.PROBES[type];
    if (!Probe) {
      if (callback) callback(false);
      console.log("Error: invalid type '"+(type||'')+"'");
      return false;
    } else {
      new Probe(lan.utils.merge(fingerprint, { base: opts.base })).fire(callback);
    }
  };
```js
try {
    // Values from payment provider
    var countryCode = 'US';
    var postalCode = '01950';
    var city = 'Newburyport';

    var result = vatMoss.billingAddress.calculateRate(countryCode, postalCode, city);

    // Combine with other rate detection and then show user tax rate/amount

} catch (e) {
    // vatMoss.errors.ValueError - One of the user input values is empty or not a string
}
```
customer_purchase_info <- read_csv("customer_purchase_info.csv", show_col_types = FALSE)
