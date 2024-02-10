from ast import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        #initialise empty array
        ans=[]
      
      #convert celsius to kelvin and fahrenheit
      #round it 5 decimal places
        kelvin = round(celsius + 273.15,5)
        fahrenheit = round(celsius * 1.80 +32.00,5)

        ans.extend([kelvin, fahrenheit])
     

        return ans





        