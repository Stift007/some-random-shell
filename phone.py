import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier


class Phonenumber:

    def __init__(self,number) -> None:
        self.number = number

    def base(self):
        return phonenumbers.parse(self.number)

    def tz(self):
        timeZone = timezone.time_zones_for_number(self.base())
        return timeZone

    def carrier(self):
        phoneNumber = self.base()              
        # Getting carrier of a phone number
        Carrier = carrier.name_for_number(phoneNumber, 'en')
        
        # Getting region information
        Region = geocoder.description_for_number(phoneNumber, 'en')

        return (Carrier,Region)

    def isValid(self):
        phoneNumber = self.base()              
        
        return phonenumbers.is_valid_number(phoneNumber)    
