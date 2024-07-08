$client = new Client('https://s1.ripple.com:51234');

$response = $client->send('account_info', [
    'account' => 'rG1QQv2nh2gr7RCZ1P8YYcBUKCCN633jCn'
]);

if ($response->isSuccess()) {
    // getResult() returns the associative array defined as the result in the API documentation.
    $data = $response->getResult();
}


public function account_info()
   {
   $request = "/v1/account_infos";
   $data = array(
      "request" => $request
   );
   return $this->hash_request($data);
   }
device_name = sys.argv[1]  # Choose device from cmd line. Options: gpu or cpu
shape = (int(sys.argv[2]), int(sys.argv[2]))
if device_name == "gpu":
    device_name = "/gpu:0"
Set your desired network name (ssid) and password (wpa_passphrase).
```
sudo mv /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.bak
sudo vim /etc/hostapd/hostapd.conf
```
```
# Basic configuration
interface=wlan0
ssid=raspwifi
channel=1
#bridge=br0

# WPA and WPA2 configuration
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=3
wpa_passphrase=abcdefg123
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP

# Hardware configuration
driver=rtl871xdrv
ieee80211n=1
hw_mode=g
device_name=RTL8192CU
manufacturer=Realtek
```
