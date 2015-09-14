import requests
import json
import datospayu

class PayU(object):
    """Datos iniciales PayU"""
    def __init__(self, api_login='', account_id=''):
        self.api_login = API_LOGIN
        self.api_key = API_KEY
        self.account_id = ACCOUNT_ID
        self.reports_url = REPORTS
        self.payments_url = PAYMENTS
        self.test = TEST

        self.payload = {
            'language': 'es',
            'command': 'PING',
            'merchant':{
                'apiLogin' : self.api_login,
                'apiKey': self.api_key,
            },
            'test': self.test,
        }

        self.order = {
            'language': 'es',
            'accountId': self.account_id,
        }

        self.transaction_data = {
            'type': 'AUTHORIZATION_AND_CAPTURE',
            'paymentCountry': 'CO',
        }

        def s_req(self, payload, api_type=PAYMENTS):
            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json',
            }
            pay_url = self.payments_url
            if api_type == REPORTS:
                pay_url == self.reports ##Cambiar URL Reports en C:PayU()

            response = requests.post(
                pay_url,
                data = json.dumps(payload),
                headers = headers,
                verify = False
            )
            #print ('REQUEST: %s' % payload)
            print ('RESPONSE: %s' % json.dumps(response.text, indent=2))
            return response

            ##Tarjeta de credito
        def submit_tr(self,
                    full_name,
                    email,
                    phone,
                    dni,
                    str1,
                    str2,
                    city,
                    state,
                    zipcode,
                    referenceCode,
                    description,
                    notifyUrl,
                    value,
                    card_number,
                    expdate):

            payload = self.payload.copy()

            payload.update({
                'command': 'SUBMIT_TRANSACTION'
                'buyer':{
                    'fullname' : full_name,
                    'emailAddress' : email,
                    'contactPhone' : phone,
                    'dniNumber': dni,
                    'shippingAddress':{
                        'street1': str1,
                        'street2': str2,
                        'city': city,
                        'state': state,
                        'country': 'CO',
                        'postalCode': zipcode,
                        'phone': phone,
                    }
                },
                'shippingAddress':{
                    'street1': str1,
                    'street2': str2,
                    'city': city,
                    'state': state,
                    'country': 'CO',
                    'postalCode': zipcode,
                    'phone': phone,
                }

            })

            order = self.order.copy()

            order.update({
                'referenceCode': referenceCode,
                'description': description,
                'signature':            ,
                'notifyUrl': notify_url,
                'additionalValues':{
                    'TX_VALUE':{
                        'value': value,
                        'currency': 'COP',
                    }
                }
            })

            transaction = self.transaction_data.copy()
            transaction.update({
                'order': order,
                'paymentMethod': pmethod,
                'deviceSessionId': dvcsession,
                'ipAddress': ipclient,
                'cookie': cookie,
                'userAgent': usagent,

            })

            response = self.s_req(payload, order, transaction)
            return json.loads(response.text)


        #Efectivo (Baloto, Efecty)
        def sub_cash(email,
                    pmethod,
                    cashexpdate,
                    ipclient,
                    referenceCode,
                    description,
                    notifyUrl,
                    value,
                    ): #Buscar si value arg son taxes

            payload = self.payload.copy()
            payload.update({
                'command': 'SUBMIT_TRANSACTION',
                'buyer':{
                    'emailAddress': email,
                }
            })

            transaction = self.transaction_data.copy()
            transaction.update({
                'order': order,
                'paymentMethod': pmethod,
                'expirationDate': cashexpdate,
                'ipAddress' ipclient,

            })

            order = self.order.copy()

            order.update({
                'referenceCode': referenceCode,
                'description': description,
                'signature':            ,
                'notifyUrl': notify_url,
                'additionalValues':{
                    'TX_VALUE':{
                        'value': value,
                        'currency': 'COP',
                    }
                }
            })

            response = self.s_req(payload, order, transaction)
            return json.loads(response.text)

            """
            def banktransfer(arg):
                payload = self.payload.copy()
                payload.update({
                    'command': 'GET_BANK_LISTS',
                    'bankListInformation':{
                        'paymentMethod': 'PSE',
                        'paymentCountry': 'CO',

                    }
                })
            """
