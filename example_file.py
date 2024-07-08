paymentDetails = { "amount":132,
                "card":{"cardNum":"XXXX111111000000",
                			  "cardExpiryMonth":"10",
                        "cardExpiryYear":"2024",
                        "cvv":"102"},
                "billingAddress":{"country":"US",
                                    "zip":"38138",
                                    "state":"TN",
                                    "street":"123 ABC Lane",
                                    "city":"Memphis"}
               }
billingAddress = json2Address(json_dic["BillingAddress"])
account.get("billingAddressLine1", "UnknownAddress")
account["billingAddressPostcode"].replace(" ", "").upper()

customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, blank=True, null=True, related_name='billing_addresses')
address = models.CharField(max_length=225, null=True, blank=True)
city = models.CharField(max_length=225, null=True, blank=True)
state = models.CharField(max_length=225, null=True, blank=True)
zipcode = models.CharField(max_length=225, null=True, blank=True)
date_added = models.DateTimeField(default=timezone.now)
is_no_billing_address = models.BooleanField(default=False)

public static IAmount merchantAccount(String account) {
    IBuilder billingAddress(Address address);
    IBuilder shopperDateOfBirth(Date dateOfBirth);
    IBuilder shopperEmail(String email);
    IBuilder shopper(Name name, String email, String ip, String reference, ShopperInteraction interaction);

public class CustomerAccount {
private String customerName;
return customerName;
public void setCustomerName(String customerName) {
this.customerName = customerName;
    private String accountNumber;
    private String accountId;
        return accountId;
    public void setAccountId (String accountId)
        this.accountId = accountId;
