# // sample-applications-for-"DICTIONARY"//
monthConversions = {
  0  : "January", # --> /keys-should-be-unique/
  1  : "February",
  2  : "March",
  3  : "April",
  4  : "May",
  5  : "June",
  6  : "July",
  7  : "August",
  "Sep"  : "September",
  9  : "October",
  10 : "November",
  "Dec" : "December"
# /changing-keys-into-numbers-is-acceptable/-->/as-long-as-unique/
}
print(monthConversions[10])
print(monthConversions["Aug"]) # <-----/invalid---using-brackets=strict/
print(monthConversions[1])
print(monthConversions[0])
print(monthConversions.get("Dec"))
print(monthConversions.get("Sep"))
print(monthConversions.get("Love")) # /not-included-in-the-key/
print(monthConversions.get("Love", "Invalid key")) # /default-value/
print(monthConversions.get("Love", "Not a valid key")) # /default-value/ 