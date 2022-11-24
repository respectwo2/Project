import joblib

rf_model = joblib.load('extractor/rf_model.pkl')

def convertString(arr):
    str_result = ""
    for s in arr:
        str_result += str(s)

    return str_result

def extract_crop(sun, temp, humid, carbon, land_moist):
    prediction = rf_model.predict([[sun, temp, humid, carbon, land_moist]])
    crop_result = convertString(prediction)
    return crop_result


