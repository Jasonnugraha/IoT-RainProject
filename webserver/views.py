# CONTROLLING VIEWS AND ROUTE
from flask import Blueprint, render_template
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db
import json

key = {
  "type": "service_account",
  "project_id": "iot-final-project-mqtt",
  "private_key_id": "e0c8c3e1905b1d1e8d2fcc0fa73149c4232d4c1d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDNBRc3u0LWqlMC\nDH1TzonJglE8bFCJV7QHsBGvDT8KnDgNcO6rpj3JlHjGqV1rDYXchPTfba8TWTkQ\nWBkRPo4njTh8mCznmJ2pBZWo69xmMDbA4z6XUYhmVUz7jo/AGiwHMOUAXBwmNnGk\nzAbnD1uNxSnk2Dn4Zh147Rlt8IIQTy4nyUun4+Ly2vxuikhwUtnMc2TTdUaGbfOY\n5eyEb3cfpWUQl9gkqieDqmFVNzZhIJBS7PV41zwa+6oGtt0CHG/yMXlmBYnKfxxg\nsPowWjYXLiF049+B/jEywL8k3Xsf6tUz5A4my3Lyt8Y3GMfrw/2pF4lNwgioHeFF\nvbnfAk5fAgMBAAECggEAOmfO23OfcOQIzbadJXjbS+qyFdKNhvLTOLVx9DqD0RP7\n6+hWNdQgGgMP/RhWop6xmcbOs6/dhleOqBdQ3NbDTIUwqF35vOh/UZ1jq0G2Ae6O\nSpjyRc1WXEDEs41DamiKTmohct7KriAoc9gjx0Naw6J9ctIegaMllkOFUQqJIvfI\nlz6wikEa2qopWJAEM8sRP0hCeXwnoqlMgSV8I1fvHvbbLB32bA9HLCCsyw2oKuyF\nrMcadtyktvCVtt42PLunv6ItrRFc/rddLsN0LucmrwdXnLGC3MUoqOHsidbQ9wlv\nZM+rrhcgzE7HYD7q2WqMdio4yEH4oO7i2wbutTF8EQKBgQD6JokLrvV3U4UPETL6\nhp0wrE4tO4+SSxOXRlX4znj3XYWXgOYLjCjpfvxB1b7c6D/OM5jDCgSJVIn6i9jE\nA5E0whGPQ82GMwUeIfHFHZgMCNdJoo4V0CfGjrLk6fsnlp6Ovfbw9Zzjlu61bA2a\nUl9T1xivLMmj9Z4EBT8GK2O/mwKBgQDR0GRQog7Y77NVBCP78jiRJwkVdFH1E+Cj\nbQ3BE0jfl3sRLLv+UIWV8lz9vjyan3Qf+c15kgUU2RMJkwBcsL6PzL4Fg0jL5KRP\nK63AvLZLpcW8ULAgprsOOPTnpLiMjVnmHi7skr6FqIXMtqnyOOzL0NydROKNTKCO\nYfRocwiyjQKBgG5YA0n5EmRhnicoUhF6weoPh6iiRlGk9m5bY18OTQPo6B4NiOx9\nFirxjfrIe5nchRDDZ9ZZG+ksNnUjrSnB3RKlrLNCmG1jIhXJqWlnBYQBfl4H658p\no/INTlJ1+AjdgvG6UCy4W011bbTvhgyV22ETV9sl6Yh+twZU/hkNmMGTAoGAdG8S\nDFEyrh6vRWGr2ng7/glMmDRZ+whR5D9zn47lJPe6WviZRvNGfsTl6AZ3OVN9rPUC\nmxF2cnBYiTqju8x1o/V6CjMl5ch3ilvx64COJYLULcIVS7lbGvRurFIT/CPBHNvp\nLG3u/ttbjRRdUUdX2W+JzljY5JL+kqU3bfNQg00CgYB+eQrUei1NECO6m0FCtQWN\n+j/o9Zf4AJi5m+OtYmt8GzRbfhEw5HF+GQInV0rpjlo2zs4RyUNQTBPNpjtCJiQw\nLXJsrd20odbnVtHBgxoE0ytiE1COstSLq2j8mGXtTnbZEVNH4ZZhKsB80mtZhwl0\nUpQZXi0+3aTA3wWt0+DYKw==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-y0p9w@iot-final-project-mqtt.iam.gserviceaccount.com",
  "client_id": "106339994358950931505",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-y0p9w%40iot-final-project-mqtt.iam.gserviceaccount.com"
}

SERVICE_ACCOUNT_PATH= key
FIREBASE_URL='https://iot-final-project-mqtt-default-rtdb.asia-southeast1.firebasedatabase.app/'

cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)

firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_URL
})
dbReference = db.reference('RainProject/sensor')

data = dbReference.get()




views = Blueprint('views', __name__)
@views.route('/')
def home():
    print()
    return render_template("home.html", dataToHTML = data)

# @views.route('/dashboard')