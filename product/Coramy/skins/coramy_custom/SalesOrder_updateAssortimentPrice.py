## Script (Python) "SalesOrder_updateAssortimentPrice"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
assort_dict ={}
assort_dict['009H401_12P_H']=51.00
assort_dict['009H402_12P_H']=47.40
assort_dict['009H403_12P_H']=57.00
assort_dict['108E5386_12P_H']=150.00
assort_dict['108H401_12P_H']=145.80
assort_dict['11414442_12P_H']=182.40
assort_dict['11495210_12P_H']=171.60
assort_dict['114H401_12P_H']=264.00
assort_dict['114H402_12P_H']=240.00
assort_dict['114H403_12P_H']=214.80
assort_dict['11684401_12P_H']=136.80
assort_dict['116H401_12P_H']=147.00
assort_dict['116H402_12P_H']=144.00
assort_dict['118H401_12P_H']=151.20
assort_dict['118H402_12P_H']=117.60
assort_dict['124H401_12P_H']=135.60
assort_dict['134A0104_12P_H']=115.20
assort_dict['136H401_12P_H']=149.40
assort_dict['136H402_12P_H']=192.00
assort_dict['136H403_12P_H']=192.00
assort_dict['137H401_18P_H']=234.00
assort_dict['140H401_12P_H']=107.16
assort_dict['140H402_12P_H']=109.59
assort_dict['141H401_12P_H']=131.64
assort_dict['14693101_12P_H']=199.20
assort_dict['153E5245_12P_H']=166.80
assort_dict['153F5340_12P_H']=166.80
assort_dict['153H402_12P_H']=186.00
assort_dict['153H403_12P_H']=183.00
assort_dict['15554770_12P_H']=144.00
assort_dict['15873440_12P_H']=172.80
assort_dict['158H401_12P_H']=138.00
assort_dict['16863440_12P_H']=171.60
assort_dict['168H401_12P_H']=150.00
assort_dict['168H402_12P_H']=168.00
assort_dict['168H403_12P_H']=138.00
assort_dict['169H401_12P_H']=107.16
assort_dict['169H402_12P_H']=152.40
assort_dict['169H403_12P_H']=163.20
assort_dict['19015387_18P_H']=216.00
assort_dict['19015896_12P_H']=144.00
assort_dict['213H401_12P_H']=148.20
assort_dict['223H401_12P_H']=139.20
assort_dict['223H402_12P_H']=139.20
assort_dict['230H401_12P_H']=159.60
assort_dict['232H401_12P_H']=142.80
assort_dict['232H402_12P_H']=140.40
assort_dict['232H403_12P_H']=156.00
assort_dict['233H402_12P_H']=126.00
assort_dict['233H403_12P_H']=216.00
assort_dict['236H401_12P_H']=174.00
assort_dict['237H401_12P_H']=150.00
assort_dict['237H402_12P_H']=138.00
assort_dict['237H403_12P_H']=118.80
assort_dict['237H404_12P_H']=171.00
assort_dict['237H405_12P_H']=135.00
assort_dict['237H406_12P_H']=115.20
assort_dict['237H407_12P_H']=174.00
assort_dict['237H412_12P_H']=150.00
assort_dict['240H401_12P_H']=146.40
assort_dict['240H402_12P_H']=151.20
assort_dict['240H403_12P_H']=139.20
assort_dict['245H401_12P_H']=216.00
assort_dict['246H401_12P_H']=187.20
assort_dict['247H401_12P_H']=234.00
assort_dict['247H402_12P_H']=216.00
assort_dict['24800156_12P_H']=82.80
assort_dict['24805576_12P_H']=83.40
assort_dict['24850104_12P_H']=94.80
assort_dict['24850134_12P_H']=90.00
assort_dict['24860157_12P_H']=87.60
assort_dict['248B5000_12P_H']=91.20
assort_dict['248H402_12P_H']=216.00
assort_dict['248H403_12P_H']=231.60
assort_dict['248H404_12_H']=201.60
assort_dict['248H405_12P_H']=216.00
assort_dict['248H406_12P_H']=211.20
assort_dict['248H407_12P_H']=188.40
assort_dict['248H408_12P_H']=190.80
assort_dict['248H409_12P_H']=183.00
assort_dict['248H410_12P_H']=196.80
assort_dict['25040169_12P_H']=81.00
assort_dict['25042733_12P_H']=88.80
assort_dict['25065455_12P_H']=114.00
assort_dict['251H401_12P_H']=180.00
assort_dict['251H402_12P_H']=189.60
assort_dict['251H403_12P_H']=148.80
assort_dict['251H405_12P_H']=213.60
assort_dict['25365673_12P_H']=98.40
assort_dict['25415284_12P_H']=102.00
assort_dict['25415674_12P_H']=99.60
assort_dict['26220104_12P_H']=126.00
assort_dict['27165093_12P_H']=160.80
assort_dict['27284967_12P_H']=159.00
assort_dict['274E5600_12P_H']=152.40
assort_dict['335H401_12P_H']=174.00
assort_dict['335H402_12P_H']=174.00
assort_dict['352H401_12P_H']=60.60
assort_dict['354H401_12P_H']=97.32
assort_dict['372H401_12P_H']=123.60
assort_dict['401H401_12P_H']=74.40
assort_dict['401H402_12P_H']=127.20
assort_dict['405H401_12P_H']=116.40
assort_dict['406H402_18P_H']=115.20
assort_dict['406H403_12P_H']=88.80
assort_dict['40700157_12P_H']=72.00
assort_dict['40750109_12P_H']=67.20
assort_dict['408H401_12P_H']=102.00
assort_dict['41335586_12P_H']=68.40
assort_dict['415H401_18P_H']=104.40
assort_dict['415H402_12P_H']=90.00
assort_dict['415H404_12P_H']=99.60
assort_dict['416H401_12P_H']=87.60
assort_dict['416H402_12P_H']=91.20
assort_dict['416H403_12P_H']=80.40
assort_dict['416H404_12P_H']=114.00
assort_dict['420H401_12P_H']=96.00
assort_dict['42225455_12P_H']=84.00
assort_dict['42232733_12P_H']=70.80
assort_dict['423H401_12P_H']=94.80
assort_dict['423H402_18P_H']=147.60
assort_dict['423H403_18P_H']=178.20
assort_dict['423H404_12P_H']=93.60
assort_dict['42420163_12P_H']=59.40
assort_dict['42435683_12P_H']=64.80
assort_dict['500H401_12P_H']=79.20
assort_dict['511H401_12P_H']=100.20
assort_dict['511H402_12P_H']=99.00
assort_dict['518E0157_12P_H']=67.20
assort_dict['518H401_12P_H']=76.80
assort_dict['519H401_12P_H']=90.00
assort_dict['52020109_12P_H']=75.60
assort_dict['52185530_12P_H']=71.40
assort_dict['527H401_12P_H']=103.20
assort_dict['527H402_12P_H']=68.40
assort_dict['52830164_12P_H']=54.00
assort_dict['52835683_12P_H']=68.40
assort_dict['528H401_12P_H']=90.00
assort_dict['53580108_12P_H']=51.60
assort_dict['536H401_12P_H']=74.76
assort_dict['536H402_12P_H']=85.68
assort_dict['536H403_12P_H']=67.32
assort_dict['537H401_12P_H']=74.76
assort_dict['537K0107_12P_H']=44.40
assort_dict['537K4747_12P_H']=58.80
assort_dict['538H401_12P_H']=83.40
assort_dict['538H402_12P_H']=114.00
assort_dict['543H401_12P_H']=82.80
assort_dict['590A5151_12P_H']=42.00
assort_dict['593K4747_12P_H(2-8)']=36.00
assort_dict['593K4747_12P_H(6-24m)']=33.60
assort_dict['593M5000_12P_H']=38.40
assort_dict['636H401_12P_H']=70.80
assort_dict['656H401_12P_H']=52.08
assort_dict['658H401_12P_H']=72.84
assort_dict['701H401_12P_H']=47.40
assort_dict['701H402_12P_H']=43.20
assort_dict['701H403_12P_H']=59.40
assort_dict['70255000_12P_H(10-16)']=43.80
assort_dict['70255000_16P_H(2-8)']=52.80
assort_dict['702H401_12P_H']=45.00
assort_dict['709H401_12P_H']=54.00
assort_dict['712H401_12P_H']=51.60
assort_dict['712H402_12P_H']=49.80
assort_dict['712H403_12P_H']=57.00
assort_dict['712H404_18P_H']=85.50
assort_dict['712K0108_12P_H']=39.00
assort_dict['712K0150_12P_H']=42.00
assort_dict['713H401_12P_H']=56.40
assort_dict['71414760_12P_H']=44.40
assort_dict['71415665_16P_H']=44.00
assort_dict['714B5306_12P_H']=43.80
assort_dict['714H401_12P_H']=42.00
assort_dict['714H402_12P_H']=51.48
assort_dict['714H403_12P_H']=42.24
assort_dict['714H404_12P_H']=51.60
assort_dict['715H401_12P_H']=57.60
assort_dict['715H402_12P_H']=51.60
assort_dict['720A5265_12P_H']=40.20
assort_dict['720H401_12P_H']=52.20
assort_dict['720H402_12P_H']=64.80
assort_dict['72374749_12P_H']=52.80
assort_dict['72375665_16P_H']=56.00
assort_dict['723H401_18P_H']=83.70
assort_dict['723H402_12P_H']=70.80
assort_dict['724H401_12P_H']=79.56        
assort_dict['724h402_18P_H']=90.00        
assort_dict['725H401_12P_H']=70.80        
assort_dict['725J0108_12P_H']=43.20
assort_dict['725J0150_12P_H']=43.80       
assort_dict['727H401_12P_H']=60.00
assort_dict['72845000_12P_H(10-16)']=54.00
assort_dict['72845000_16P_H(2-8)']=63.20
assort_dict['75105143_12P_H']=61.20       
assort_dict['751H401_12P_H']=75.60        
assort_dict['751H402_12P_H']=63.00
assort_dict['755H401_16P_H']=76.00        
assort_dict['769H401_12P_H']=70.44
assort_dict['769H402_16P_H']=91.20        
assort_dict['77045143_12P_H']=47.40       
assort_dict['770H401_12P_H']=67.32
assort_dict['770H402_12P_H']=64.92        
assort_dict['770H403_12P_H']=79.20        
assort_dict['770H404_16P_H']=116.00
assort_dict['770H405_12P_H']=63.00        
assort_dict['77115217_12P_H']=62.40       
assort_dict['77115401_12P_H']=70.80
assort_dict['771H401_12P_H']=66.72        
assort_dict['771H402_12P_H']=97.80
assort_dict['771H403_16P_H']=84.00
assort_dict['771H404_12P_H']=66.00
assort_dict['772H401_12P_H']=68.40
assort_dict['774H402_16P_H']=108.00       
assort_dict['774H403_16P_H']=130.40       
assort_dict['775H401_12P_H']=88.80
assort_dict['775H402_16P_H']=159.20
assort_dict['776H401_16P_H']=110.40       
assort_dict['778H401_16P_H']=120.00
assort_dict['778H402_12P_H']=85.80        
assort_dict['855H401_12P_H']=39.00
assort_dict['869H401_12P_H']=53.40
assort_dict['910H401_12P_H']=149.40

order = context
assort_keys = assort_dict.keys()
movement_list = order.getMovementList()
for movement in movement_list :
  resource = movement.getResourceValue()
  if resource is not None :
    if resource.getPortalType() == "Assortiment" :
      assort_id = resource.getId()
      if assort_id in assort_keys :
        movement.setProperty(key='price',value=assort_dict[assort_id])
        #print "prix actuel : "+str(movement.getPrice())+"  prix assortiment : "+str(assort_dict[assort_id])

#return printed
