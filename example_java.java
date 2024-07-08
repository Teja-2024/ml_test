public static class Device_info {
        public String Dev_ID = "NONE";

        public String Wired_IP = "NONE";
        public String Wired_ID = "NONE";
        public char Wired_conn;
        public String Wired_MAC = "NONE";
        public String Wired_loc = "NONE";

        public String Wifi_IP = "NONE";
        public String Wifi_ID = "NONE";
        public char Wifi_conn;
        public String Wifi_loc = "NONE";
        public String Wifi_MAC = "NONE";
        public String LTE_IP = "NONE";
	
        public String LTE_ID = "NONE";
        public char LTE_conn;
        public String LTE_loc = "NONE";
        public String LTE_MAC = "NONE";
    }

public class Refresh_device_info
{

	public static String baseurl = "https://suremdm.42gears.com/api";  // BaseURL of SureMDM
	private static String Username = "Username";
	private static String Password = "Password";
	private static String ApiKey = "Your ApiKey";

	public static void main(String[] args) throws Exception
	{

		String DeviceID = GetDeviceID("Device_Name");
		if (DeviceID != null)
		{
			String status = RefreshDeviceInfo(DeviceID);
			System.out.print(status);
		}
		else
		{
			System.out.print("Device not found!");
		}
	}

	private static String RefreshDeviceInfo(String deviceID) throws Exception
	{
		// /* Api to apply dynamic jobs
		// Endpoint: /dynamicjob
		//   Method: POST
		//   Request Body:
		//      {
		//          "JobType":string,
		//          "DeviceID":string
		//      }
		//   Authentication:
		//       Basic authentication
		//   Headers:
		//       ApiKey: �Your Api-Key�
		// */

		// // ... API URL
		String URL = baseurl + "/dynamicjob";
		// ... PayLoad data
		JSONObject PayLoad = new JSONObject();
		PayLoad.put("DeviceID", deviceID);
		PayLoad.put("JobType", "Refresh_Device");
		// ... request body
		MediaType mediaType = MediaType.parse("application/json");
		RequestBody body = RequestBody.create(mediaType, PayLoad.toString());
		// ... Create request
		OkHttpClient client = new OkHttpClient();
		Request request = new Request.Builder().url(URL)
				// ... Send payload
				.post(body)
				// ... Basic authentication header
				.addHeader("Authorization", Credentials.basic(Username, Password))
				// ... ApiKey Header
				.addHeader("ApiKey", ApiKey)
				// ... Set content type
				.addHeader("Content-Type", "application/json").build();
		// ... Execute request
		Response response = client.newCall(request).execute();

		return response.body().string();
	}

	private static String GetDeviceID(String deviceName) throws Exception
	{
		/*  Retreiving information of device
		Endpoint: /device
		Method: POST
		Request Body:
		    {  
		       "ID": string,
		       "SearchValue":string,
		       "Limit":integer,
		       "SortColumn":string,
		       "SortOrder":string,
		       "IsSearch":boolean,
		       "SearchColumns":string[]
		   }
		Authentication:
		    Basic authentication
		Headers:
		    ApiKey: �Your Api-Key� 
		*/

		// request body
		JSONObject PayLoad = new JSONObject();
		PayLoad.put("ID", "AllDevices");
		PayLoad.put("IsSearch", true);
		PayLoad.put("Limit", 20);
		PayLoad.put("SearchColumns", new JSONArray("[\"DeviceName\"]"));
		PayLoad.put("SearchValue", deviceName);
		PayLoad.put("SortColumn", "LastTimeStamp");
		PayLoad.put("SortOrder", "asc");
		MediaType mediaType = MediaType.parse("application/json");
		RequestBody body = RequestBody.create(mediaType, PayLoad.toString());

		// API URL
		String URL = baseurl + "/device";
		// Create request
		OkHttpClient client = new OkHttpClient();
		Request request = new Request.Builder().url(URL)
				// Send payload
				.post(body)
				// Basic authentication header
				.addHeader("Authorization", Credentials.basic(Username, Password))
				// ApiKey Header
				.addHeader("ApiKey", ApiKey)
				// Set content type
				.addHeader("Content-Type", "application/json").build();
		// Execute request
		Response response = client.newCall(request).execute();
		// Extracting DeviceID
		String data = response.body().string();
		if (response.isSuccessful())
		{
			JSONObject jsonObj = new JSONObject(data);
			JSONArray devices = jsonObj.getJSONArray("rows");
			for (int index = 0; index < devices.length(); index++)
			{
				JSONObject device = devices.getJSONObject(index);
				if (device.get("DeviceName").equals(deviceName))
				{
					return device.get("DeviceID").toString();
				}
			}
		}
		return null;
	}
host_name, device_type = value 
public static native int device_type(long j);
public int device_type;
protected List getFieldOrder() { return Arrays.asList(new String[]
      { "device_type", "device_id" }); }
  }

