import pandas as pd
tls=pd.read_excel("TIRUPUR LOGISTIC SERVICES -VEHICLE DETAILS (2).xlsx")
print(tls)
tls_details=pd.DataFrame(tls)

tls_vehicle_details=tls_details.to_csv("tls_vehicle_details.csv",index=False)
print(tls_vehicle_details)