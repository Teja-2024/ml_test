address = 0x02000000
for peripheral in settings["peripherals"]:
    peripheral.enumerate(address)
    address += 0x01000000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 18157)
sock.connect(server_address)
address = ('localhost', 6000) 

address = os.environ.get('NVIM_LISTEN_ADDRESS')
nvim = pynvim.attach('socket', path=address)

address = server_list[checked_node_id]['add']

ip_address = input('enter ip address>')
address = input("Enter Address of Employee: ")

billingaddress = models.TextField()
BillingAddress = get_model('order', 'BillingAddress')
billingAddress = StringField('Billing Address', [validators.Length(min=1, max=100)])
'BillingAddressForm': 'shop.forms.checkout.BillingAddressForm',

billingAddress_URL = [
    path('billing/address/',BillingAddressView.as_view()),
    path('shipping/address/',ShippingAddressView.as_view()),
    path('billng/address/delete/<int:pk>/', BillingAddressDeleteView.as_view())]

billing_address = AddressModel.retrieve_user_shipping_address_by_id(user_id)
billingAddress1 = models.CharField(max_length = 250, blank = True)
billingName = models.CharField(max_length=250, blank=True)
billingAddress1 = models.CharField(max_length=250, blank=True)
billingCity = models.CharField(max_length=250, blank=True)
billingPostcode = models.CharField(max_length=10, blank=True)
billingCountry = models.CharField(max_length=200, blank=True)


