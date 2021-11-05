# // sample-applications-for-"DICTIONARY"//
monthConversions = {
  "Jan": "January", # --> /keys-should-be-unique/
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sep": "September",
  "Nov": "November",
  "Dec": "December"
# //changing-keys-into-numbers-is-acceptable//
}



print(monthConversions["Nov"])
print(monthConversions["Aug"])
print(monthConversions["Feb"])
print(monthConversions["Jan"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Sep"))
print(monthConversions.get("Love")) # //not included in the key//
print(monthConversions.get("Love", "Invalid key")) # //default value// 
print(monthConversions.get("Love", "Not a valid key")) # //default value// 




