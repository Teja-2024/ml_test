order_hist = data.groupby(['user'])['order_id'].unique().apply(list).reset_index()
order_history = pd.read_csv('order_history.csv')
order_history['Item Total'] = pd.to_numeric(order_history['Item Total'].str.replace('$', ''))

# Calculate the total amount spent on Amazon
total_spent = order_history['Item Total'].sum()

# Determine the most frequently used card
most_used_card = order_history['Payment Instrument Type'].value_counts().index[0]

# Determine the month and year of each order
order_history['Order Date'] = pd.to_datetime(order_history['Order Date'])
order_history['Month'] = order_history['Order Date'].dt.month
order_history['Year'] = order_history['Order Date'].dt.year

# Map month numbers to month names
month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
order_history['Month Name'] = order_history['Month'].apply(lambda x: month_names[x-1])
purchase_history = pd.read_csv(data_dir.joinpath('purchase_history.csv'))
purchase_history = pd.read_csv('purchase_history.csv')
product_purchase_history = last_orders.pivot_table(index = ['user_id', 'product_id'],\
                                                   columns='rank', values = 'reordered').reset_index()

purchase_history = relationship('CartItem', backref='soda')
history = get_purchase_history(user, safe=False)
purchase_history_links = in_demand_item_finder(items)
purchase_history = serializers.StringRelatedField()
purchase_history_data_grid=SQLFORM.grid(db.purchase_history_data, 
        # fields=[
        #     db.categories.category_name,
        #     db.categories.category_description,
        #     db.categories.s3_url,
        # ],
        maxtextlength=100,
        )
purchase_history_data = {'date': datetime.datetime.now().astimezone(None), 'memberID': memID, 'totalPrice': float("{:.2f}".format(self.total)), 'items': items_data, 'paymentMode': self.pymnt_mode.currentText()}
            purchaseHistory.create_autoID(purchase_history_data)
purchase_history_data_id=db.purchase_history_data.bulk_insert([purchase_history_dict])[0]
    session.session_purchase_history_data_id=purchase_history_data_id
            purchase_history_data_id=purchase_history_data_id,
        purchase_history_data_row=db(db.purchase_history_data.id==purchase_history_data_id).select().first(),
…ase_history_products_rows=db(db.purchase_history_products.purchase_history_data_id==purchase_history_data_id).select(),
    redirect(URL('confirmation', args=(purchase_history_data_id)))
#     # {{purchase_history=db(db.purchase_history_data.muses_id==auth.user_id).select()}}
…    #     {{purchase_history_products=db(db.purchase_history_products.purchase_history_data_id==purchase.id).select()}}
