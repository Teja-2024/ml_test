#purchase history
@login_required
def purchasing_history(request):
    purchasing_history = user_payment.objects.select_related('user').all()
    return render(request, 'purchasing_history.html', {'purchasing_history': purchasing_history})

@login_required
def purchasing_histor(request):
    return render(request,'purchasing_history.html')

@login_required
def product_purchase_details(request):
    
    return render(request,'product_buy_details.html')

@login_required
def product_cart_details(request, cart_id):


    # Retrieve product details and related cart items for the specific cart_id
    cart_items = Cart_items.objects.select_related('product').filter(cart_id=cart_id)

    # Pass the cart_items to the template context
    context = {
        'cart_items': cart_items,
    }

    

    return render(request, 'product_buy_details.html', context)


    def recommend_based_on_purchasing_history(self, site_id, user_id):
        purchasing_history = self.getPurchasingHistory(site_id, user_id)["purchasing_history"]
        topn = self.calc_weighted_top_list_method1(site_id, "PLO", purchasing_history)
        return topn

    def getSimilaritiesForViewedUltimatelyBuy(self, site_id, item_id):
        viewed_ultimately_buys = getSiteDBCollection(self.connection, site_id, "viewed_ultimately_buys")
        result = viewed_ultimately_buys.find_one({"item_id": item_id}, read_preference=ReadPreference.SECONDARY_PREFERRED)
        if result is not None:
            vubs = result["viewedUltimatelyBuys"]
        else:
            vubs = []
        topn = [(vubs_item["item_id"], vubs_item["percentage"]) for vubs_item in vubs]
        topn = self.apply_black_list2topn(site_id, item_id, topn)
        return topn

class PurchaseHistory(db.Model):
    __tablename__ = 'Purchase_history'
    Purchase_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, nullable=False)
    OrderID = db.Column(db.Integer, nullable=False)
    Order_Date = db.Column(db.Date, nullable=False)
    Status_Order = db.Column(db.Enum('D', 'ND'), nullable=False)
    Delivery_Date = db.Column(db.Date, nullable=False)

class Inventory(db.Model):
    __tablename__ = 'Inventory'
    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Quantity = db.Column(db.Integer, nullable=False)

class OrderUser(db.Model):
    __tablename__ = 'Order_User'
    OrderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Value_Order = db.Column(db.Float, nullable=False)
    UserID = db.Column(db.Integer, nullable=False)
    Placement = db.Column(db.String(100), nullable=False)
    Delivery_Date = db.Column(db.Date, nullable=False)
    Delivery_Personnel = db.Column(db.String(100), nullable=False)
    ProductID = db.Column(db.Integer, nullable=False)
    Product_Name = db.Column(db.String(100), nullable=False)
    Product_Size = db.Column(db.Enum('XS', 'S', 'M', 'L', 'XL', 'XXL'), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Status_Order = db.Column(db.Enum('D', 'ND'), nullable=False)
    AgentID = db.Column(db.Integer, nullable=False)
    

@app.route('/')
def home():
    # try:
    #     a = UserDetail.query.all()
    #     print(a)
    # except Exception as e:
    #     print(e)
    return render_template('home.html')



@app.route('/profile', methods=['POST', 'GET'])
def success():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    return render_template('success.html', user=current_user)

[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
order_hist = data.groupby(['user'])['order_id'].unique().apply(list).reset_index()
product_hist = data.groupby(['user'])['product_id'].apply(list).reset_index()
order_dow_hist = data.groupby(['user'])['order_dow'].apply(list).reset_index() # unique().적용해보기
order_hour_of_day_hist = data.groupby(['user'])['order_hour_of_day'].apply(list).reset_index()

import GPUtil
DEVICE_ID = str(GPUtil.getFirstAvailable(order='memory')[0])
os.environ["CUDA_VISIBLE_DEVICES"] = DEVICE_ID
print('GPU selected:', DEVICE_ID)


import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
browserInfo = '1ddcS8t1orBzkaklajVhFUY5nl)2AVnT66wlRr2CPHZZBE5swQzERQwqVS2GIZO15ltGWEg)wnMlzSwrC8NjgdbvkVEsrCtLahilGQQyWiYGxK4JKmBYFJcyrcO2L13JaElKnxTTRv834ZRvMp(xJ7X(z7Qg8uXWewqfPHi2Kyr43lgwj(Ic7KRTQdPIMdJrv6XxlS3ZAAMu9xFq65vodK(DILkztN(9mjcVlXSI1Zi)uv0a0HHwuV)OqmvBs3j7iBSia7ROkpBF5r)pL)XIBd0Dqby2X7XDltZyyl37xm7uXzsBP)y7Jax47IIsGgWivMpdBTR6LDmZH7DLfybwrS1zSqMXEIaYNuCnDMvnufikZJoEEhi42PMim9Wl2RoQeMX0XpkqUwl0wj0cLHXcg5V7CEMU)cKhtNYquIba(UpHp6dHCGXvEVVhcwdpEzKxJeNRhZHaNUNMmPqxquZ3nur)YegWtiPrwEStuQ4BHDxEfxg0iCRahbK)TyQwU9WrPxTR)kONAmeqxM0hwhtUz2)x)60O5ZZHq6ucCmH8(SC(ENU7a1FyzGss41k6fKqPqFJJ4M0wybv6R4HhfiDoKZhpd2i1lNhwtDdAN6nQeJp8hai5KS3KPttMHiCt80EcjF5ZjVTuvrJaxSU3HMNOtGY0xAkcwB8xpzT)bAOmDaUiG3RxdOUM6iV3t(C0ZH7nuhTg70hr5zzRJcZvVb2Dm76iUA9i7HvCz89vi70e1HAaW39a7AspzwUz1x0ilSaBoJji0(tnPkrZ(vTHkYkGdcaSDbdwZI9FepXaN4XujjGWFlNj9PXpnwo(oD9bU8sC0LxZHclfZP2Dv1M7ILSlehJ2ibe8uaSzCNwxKhKL(tzXqBp30TlupMaH4j3)xy2n8O0Z7DA0vsT0yxYh9lMI9Yh6H1Efy4Vg4tlClNaw97qwrIhCOgR3a1s62RrduXiXhgyPL0jHNexyPxKJOK((1au883(34mGnYuRVc0IqhAltQhbBW(Ual4zPzgMfH5Lllr7qs1owx2aCvTnSXrNFZQHOeJFzuwgo7vzYguowNBJCKKkzVCXHgLVcYrqJKrG2tfyCxqDv8JqgYKfQpkqQDdSeAYiudtIy2SVkEV8xcL)DVafJxuI1JlCYgTyw1HWaDTBCAbmoXoCGQnlcqixZ0gNumjvZ2yfeeZD92lc6J9wHbwqTNKT(mEz)Qs9ui9jlYzj)o1xBqt2o1ZrokQqgt7eFX)B7eKy2hv86q59IZzEu1nAYf7VXcKvFWfEukBg1IZv(f12wTWzS9WWu8(7WO7jxpUSZPotShB9bskzExJhKyZPUgpudfsbL7VSXF5wNE6Z)2NLRouep7tESjaIxbOLQuaXC2yf8GJBNqVRjMNFYUmWJva861vJqiRjeuDiR(6YH6i8UsY10A1(SgxiJNi5GX7YxNAwKjWWlZeCV9riFfdI5xXgVRnu4vKa1GNEgRuqCTKDk(lX56H1oq1oFKsOj8qyJ)qnHsb1f8LYAL8BF4IdsTH5HPczAMhY77ItgqKT7moH5TTQo(eVm3mELd)ez4QZDmAVqzfCLIXVdwm5mU(sATkNHHHgEaJCsJdSfoCYs9I8fMRMIQbiSBl4HL928(FftiUJ4ATsIR6vRyKnwJUCk2)3AEeCK1AAlGhu453QzFSR6BtUsBE5XNCW)Uv0fYMA1vOSmjBFe65eBAPy)U1gEavx6hJN(CMXHzjth91jhMhsQL3)UHQlb3cf84Kt)dfmuxyjNQGAgB(e9zpThy23CggKhFwxll2kmNUbY4YbUEQgavwqxSwL14mTJctGZRkgRQ4kNeaGK2TF4lbU5CRi)OF8hwXE2GSNnC5odPzzFxuBkFdyE9XpiEaeoG2gMBgLMrfHYUevSJ1301k2le(EjgMM(Sk7O8ElBoT)cAxJK0BQMEsAumcBd)oLlMFDJOSzezH9yeTjgl3DSY0SJ0gkLaPurwN)XYpiHd(dp)gBRmtnl66EIqTgZFBX41llBy2FhDZKevAfrMMAeaXOXwcQ(It0y1P8UqB3gzmRdE6zBV(A8X6h4HNWJL1iNby3Nh68IklacEzJcMO6P2EKvBuAz(YrrxO9oh7WBHpLd928HGs6t3)lvSIDSheR8)YpG4w(w5yKbqsolzgf592NWDf6y6tBfbim5hAnpkfpvemX)ULm2kG1UyyDPNVn4eXIzeMWNve8ECAxGm4BK6akgJHSq40GwMUtJifKDLgw4x4o8QueGCSu82WcVpnRACNIlU0tP3YUlaW1zssJwxhFIx3ZlfxHUu4dzS8xfqgZqkZ37FwsH51VqlHI4w1lEwqrF)9FfWExVM(q(2GN9rU1cNc(kFGH7vjC7BNrykXUrNqGYmHyZjHp37DhH(VGwp1XxA9YGR3WmbxwxNlJyKuTpOgSeN4q4oGcC(cwqZpkhrJSEuR5AY5gTJHYlxTV)8c72DPeAY2FwDCVFGyAXtOJIe6BqGpJ1gog4TkqQpezlhfIETxhNIziB0wiWgtBY04Z2Un2SG8JNne7j)tpk6SuNUxH7hlXKDObfS4vANvfx(EHmeXJU9tLNsoCNwe39fV4)xaTkaXI4F2jKBGy6mh7g5aR862CuCla9H337)vIkJ)oCG30tTcNVGaDJDhWgpMJ6RIns64cKuSm9zfGCr0GNghugshgIdduNbyBJSPc68hu1psMLS4DCy1fjgIVbVJjEN)l0JbQDXjgbzlBDlv8H0AhnzigqM9AJgIMqt(DZUSky4yG5D01)dz2DXoDG5t9f)QEJp71y9pMuZNOtnQ7SRf0GCUhbyNUAMAp5mP5R6CkuGOJE1lKcg4ih80x)yEUoGy(3ArN4ah(0AluoR8gK5MhyW1dSG7yP5Rkeg6nbqgoYuuH)BrDub1be54kzD4TrXQZp(oMrigZSz0WcBKmhf3Dgq(YRHeqaRglxkHvjqZF415AhHCovJlbwjI6Ikgl7l2uaYk3SAcCkTdgn(Wmi9DnGp1r3VS4kfEKjzHifM73TQxx88yO0Y0ChZGtFSOoLCxbq9UwnivUt(KZMd9vdXDwA8KQnGqSJS)qgbtUcusI9Nz0RZDw2(T3WaD6703t(2XfRfRrpS6gq24ywUCv96VXkhnYxTXtVyYKyucGcj0bWP8ISK60iERzwmhD5m7aSEZuWR6kujOQGWar0Hax)TMQCMF894EaE15ejZaOcx4m8aWTcwTD(PneZA3L7jmxBk9m5rIryM51JX(tvNeumvC7eKSc7Ye)O2YP6wosnNkztpYCd4hh(dlHTLdqQpbtfI9w(bkuMROQKKXuS979OVfAY0Vrvjwfikbo30AnaIWW)hW56KotLOWsAuW(vpk6AaTa4PNGx8va0KSb(K4NeHC)JZJtcP9DEAc22XQw4GtkN(qfTo4RCAcldhi)GwMrGAc)gq0pUc5jP(F4aOyRzGRUE8M0Vit2s2VF8wp4otLeQcgmayodZRaf4dDpwVh96yaw46i2kcybJpoNuSh6igYfcfSWe0XoXCjpDh7TlWvu0feHbMjf)tEwTDi)DKoKmYA3t8OwxHnSL2jGoxk4(FepLGNYIsPxRBw(jTcYxa705db245d537a24b51c0f85a6163ec20d15aa5a5fa455ba78b7139897c8fd877c268bf968c2425c1d4a41842ce4e25f6817bf8427c628af5fac117241aaa59409e21e19df187fabfccfa68f36e8f8159a678ff7be77794f0f3e1c070b4a856c089bb9a18f3d243e5bde4a63cf353da792ebb9d19e9ece46cc2a88652ecc17ad'
browserInfo = loads(infos[2])

browserInfo = 'my browser information'
# swagger_types = {
#         "browser_info": "BrowserInfo",
#         "device": "Device",
#         "email": "str",
#         "home_phone": "str",
#         "id": "str",
#         "identity": "str",
#         "ip": "str",
#         "ip_country": "str",
#         "locale": "str",
#         "phone": "str",
#         "user_agent": "str",
#         "work_phone": "str",
#     }

account_Info = "abscde"
