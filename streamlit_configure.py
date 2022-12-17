# %%





import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
import json
import os
import ssl







def fn(datetime="2011-11-27T00:00:00.000Z",
          Global_reactive_power= 0.0,
          Voltage= 0.0,
          Global_intensity= 0.0,
          Sub_metering_1= 0.0,
          Sub_metering_2= 0.0,
          Sub_metering_3= 0.0,
          sub_metering_4= 0.0):
  def allowSelfSignedHttps(allowed):
      # bypass the server certificate verification on client side
      if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
          ssl._create_default_https_context = ssl._create_unverified_context

  allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

  # Request data goes here
  # The example below assumes JSON formatting which may be updated
  # depending on the format your endpoint expects.
  # More information can be found here:
  # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
  data =  {
    "Inputs": {
      "data": [
        {
          "datetime": datetime,
          "Global_reactive_power": Global_reactive_power,
          "Voltage": Voltage,
          "Global_intensity": Global_intensity,
          "Sub_metering_1": Sub_metering_1,
          "Sub_metering_2": Sub_metering_2,
          "Sub_metering_3": Sub_metering_3,
          "sub_metering_4": sub_metering_4
        }
      ]
    },
    "GlobalParameters": {
      "quantiles": [
        0.025,
        0.975
      ]
    }
  }

  body = str.encode(json.dumps(data))

  url = 'http://113adb81-0355-487d-8a64-5e93e08a45b6.eastus2.azurecontainer.io/score'
  # Replace this with the primary/secondary key or AMLToken for the endpoint
  api_key = 'DrD9hDfcunc70aEkbbdIo7lyS9pax0dB'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")


  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)

      result = response.read()
      print(result)
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))

      # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())
      print(error.read().decode("utf8", 'ignore'))
  return result





# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
st.header("Fish Weight Prediction App")
st.text_input("Enter your Name: ", key="name")
data = pd.read_csv("https://github.com/jjaggi/SmartGrid-2/raw/main/household_power_consumption_days.csv")
#load label encoder
# encoder = LabelEncoder()
# encoder.classes_ = np.load('classes.npy',allow_pickle=True)

# load model
# best_xgboost_model = xgb.XGBRegressor()
# best_xgboost_model.load_model("best_model.json")

if st.checkbox('Show Training Dataframe'):
    data

# st.subheader("Please select relevant features of your fish!")
# left_column = st.columns(1)
# with left_column:
#     inp_species = st.radio(
#         'Name of the fish:')

input_Length1 = st.slider('Voltage',min(data["Voltage"]), max(data["Voltage"]))
input_Length2 = st.slider('Intensity',min(data['Global_intensity']), max(data["Global_intensity"]), 1.0)
input_Length3 = st.slider('Sub_metering_1',min(data['Sub_metering_1']), max(data["Sub_metering_1"]), 1.0)
input_Height = st.slider('Sub_metering_2',min(data['Sub_metering_2']), max(data["Sub_metering_2"]), 1.0)
input_Width = st.slider('Sub_metering_3',min(data['Sub_metering_3']), max(data["Sub_metering_3"]), 1.0)

if st.button('Make Prediction'):
    # input_species = encoder.transform(np.expand_dims(inp_species, -1))
    # inputs = np.expand_dims(
        # [int(input_species), input_Length1, input_Length2, input_Length3, input_Height, input_Width], 0)
    # prediction = best_xgboost_model.predict(inputs)
    prediction=fn(datetime="2011-11-27T00:00:00.000Z",Voltage=input_Length1,Global_intensity=input_Length2,Sub_metering_1=input_Length3,Sub_metering_2=input_Height,Sub_metering_3=input_Width,sub_metering_4=150)
    prediction=json.loads(prediction)['Results']['forecast']
    print(input_Length1)
    print("final pred", (prediction))
    st.write(f"Global power usage is: {np.squeeze(prediction, -1):.2f}KW")

    st.write(f"Thank you {st.session_state.name}! I hope you liked it.")
    st.balloons()
    



