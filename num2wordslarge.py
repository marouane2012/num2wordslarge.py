#This program converts numbers to words up to 'one decimillinillion'.
#Imports and settings.
import math
from mpmath import *
mp.dps = 5#mp.dps = 3003
number = mpf(2**100600) #Change this.
limit = 0 #Prevent infinite run.
global layer
if number > 0:
	layer = math.floor(log(mpf(number),mpf(1000)))
elif number < 0:
	layer = math.floor(log(mpf(number*-1),mpf(1000)))
class NumberConverter: #The actual num2word program.
	def __init__(inst, number,layer):
		global limit
		smallnumbers = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','twen','thir','fif'] #For 1-999
		prefixbase = ['','m','b','tr','quadr','quint','sext','sept','oct','non'] #For the first 9 illions
		prefixones = ['','un','duo','tre','quattor','quin','sex','septem','octo','novem'] #For the next 90 illions
		prefixones2 = ['','un','duo','tres','quattor','quin','sex','septem','octo','novem'] #Avoid 'trecentillion' and 'trescentillion'
		prefixtensbase = ['dec','vigint','trigint','quadragint','quinquagint','sexagint','septuagint','octogin','nonagin'] #For the tenth to 99th illions
		prefixtens = ['','deci','viginti','triginta','quadraginta','quinquaginta','sexaginta','septuaginta','octoginta','nonaginta'] #For the next 900 illions
		prefixhundreds = ['','cent','ducent','trecent','quadringent','quingent','sescent','septingent','octingent','nongent'] #For illions 100-999
		tiersec = ['milli'] #Tier two illions
		tiersecones = ['','du','tre','quadri','quinti','sexti','septi','octi','noni'] #Their prefixes
		tiersectens = ['','deci','viginti']
		if number == 0:
			print('zero')
		if number < 0:
			number *= -1
			print('negative', end = ' ')
		while number > 0 and limit < 1000:
			oldnum = number
			if layer > 0:
				layer2 = math.floor(log(mpf(layer),mpf(1000)))
			if number >= 900*(1000**layer) and number < 1000*(1000**layer): #If statements
				number -= 900*(1000**layer)
				print(smallnumbers[8] + ' hundred', end = ' ')
			if number >= 800*(1000**layer) and number < 900*(1000**layer):
				number -= 800*(1000**layer)
				print(smallnumbers[7] + ' hundred', end = ' ')
			if number >= 700*(1000**layer) and number < 800*(1000**layer):
				number -= 700*(1000**layer)
				print(smallnumbers[6] + ' hundred', end = ' ')
			if number >= 600*(1000**layer) and number < 700*(1000**layer):
				number -= 600*(1000**layer)
				print(smallnumbers[5] + ' hundred', end = ' ')
			if number >= 500*(1000**layer) and number < 600*(1000**layer):
				number -= 500*(1000**layer)
				print(smallnumbers[4] + ' hundred', end = ' ')
			if number >= 400*(1000**layer) and number < 500*(1000**layer):
				number -= 400*(1000**layer)
				print(smallnumbers[3] + ' hundred', end = ' ')
			if number >= 300*(1000**layer) and number < 400*(1000**layer):
				number -= 300*(1000**layer)
				print(smallnumbers[2] + ' hundred', end = ' ')
			if number >= 200*(1000**layer) and number < 300*(1000**layer):
				number -= 200*(1000**layer)
				print(smallnumbers[1] + ' hundred', end = ' ')
			if number >= 100*(1000**layer) and number < 200*(1000**layer):
				number -= 100*(1000**layer)
				print(smallnumbers[0] + ' hundred', end = ' ')
			if number >= 90*(1000**layer) and number < 100*(1000**layer):
				number -= 90*(1000**layer)
				print(smallnumbers[8] + 'ty', end = ' ')
			if number >= 80*(1000**layer) and number < 90*(1000**layer):
				number -= 80*(1000**layer)
				print(smallnumbers[7] + 'y', end = ' ')
			if number >= 70*(1000**layer) and number < 80*(1000**layer):
				number -= 70*(1000**layer)
				print(smallnumbers[6] + 'ty', end = ' ')
			if number >= 60*(1000**layer) and number < 70*(1000**layer):
				number -= 60*(1000**layer)
				print(smallnumbers[5] + 'ty', end = ' ')
			if number >= 50*(1000**layer) and number < 60*(1000**layer):
				number -= 50*(1000**layer)
				print(smallnumbers[14] + 'ty', end = ' ')
			if number >= 40*(1000**layer) and number < 50*(1000**layer):
				number -= 40*(1000**layer)
				print(smallnumbers[3] + 'ty', end = ' ')
			if number >= 30*(1000**layer) and number < 40*(1000**layer):
				number -= 30*(1000**layer)
				print(smallnumbers[13] + 'ty', end = ' ')
			if number >= 20*(1000**layer) and number < 30*(1000**layer):
				number -= 20*(1000**layer)
				print(smallnumbers[12] + 'ty', end = ' ')
			if number >= 19*(1000**layer) and number < 20*(1000**layer):
				number -= 19*(1000**layer)
				print(smallnumbers[8] + 'teen', end = ' ')
			if number >= 18*(1000**layer) and number < 19*(1000**layer):
				number -= 18*(1000**layer)
				print(smallnumbers[7] + 'een', end = ' ')
			if number >= 17*(1000**layer) and number < 18*(1000**layer):
				number -= 17*(1000**layer)
				print(smallnumbers[6] + 'teen', end = ' ')
			if number >= 16*(1000**layer) and number < 17*(1000**layer):
				number -= 16*(1000**layer)
				print(smallnumbers[5] + 'teen', end = ' ')
			if number >= 15*(1000**layer) and number < 16*(1000**layer):
				number -= 15*(1000**layer)
				print(smallnumbers[14] + 'teen', end = ' ')
			if number >= 14*(1000**layer) and number < 15*(1000**layer):
				number -= 14*(1000**layer)
				print(smallnumbers[3] + 'teen', end = ' ')
			if number >= 13*(1000**layer) and number < 14*(1000**layer):
				number -= 13*(1000**layer)
				print(smallnumbers[13] + 'teen', end = ' ')
			if number >= 12*(1000**layer) and number < 13*(1000**layer):
				print(smallnumbers[11], end = ' ')
				number -= 12*(1000**layer)
			if number >= 11*(1000**layer) and number < 12*(1000**layer):
				print(smallnumbers[10], end = ' ')
				number -= 11*(1000**layer)
			if number >= 10*(1000**layer) and number < 11*(1000**layer):
				number -= 10*(1000**layer)
				print(smallnumbers[9], end = ' ')
			if number >= 9*(1000**layer) and number < 10*(1000**layer):
				number -= 9*(1000**layer)
				print(smallnumbers[8], end = ' ')
			if number >= 8*(1000**layer) and number < 9*(1000**layer):
				number -= 8*(1000**layer)
				print(smallnumbers[7], end = ' ')
			if number >= 7*(1000**layer) and number < 8*(1000**layer):
				number -= 7*(1000**layer)
				print(smallnumbers[6], end = ' ')
			if number >= 6*(1000**layer) and number < 7*(1000**layer):
				number -= 6*(1000**layer)
				print(smallnumbers[5], end = ' ')
			if number >= 5*(1000**layer) and number < 6*(1000**layer):
				number -= 5*(1000**layer)
				print(smallnumbers[4], end = ' ')
			if number >= 4*(1000**layer) and number < 5*(1000**layer):
				number -= 4*(1000**layer)
				print(smallnumbers[3], end = ' ')
			if number >= 3*(1000**layer) and number < 4*(1000**layer):
				number -= 3*(1000**layer)
				print(smallnumbers[2],end = ' ')
			if number >= 2*(1000**layer) and number < 3*(1000**layer):
				number -= 2*(1000**layer)
				print(smallnumbers[1],end = ' ')
			if number >= 1*(1000**layer) and number < 2*(1000**layer):
				number -= 1*(1000**layer)
				print(smallnumbers[0], end = ' ')
			if (layer%1000) > 100 and (layer%1000) < 1001 and layer >1000 and (layer/(1000**layer2)) <= 10:
				print(tiersecones[int(math.floor((layer-1)/(1000**layer2))-1)] + tiersec[(layer2)-1] + '-' + prefixones[int(layer%10)-1] + prefixtens[int(math.floor(((layer%100)-1)/10))] + prefixhundreds[int(math.floor(((layer%1000)-1)/100))] + 'illion',end = ' ')
			if (layer%1000) > 10 and (layer%1000) < 101 and layer > 1000 and (layer/(1000**layer2)) <= 10:
				print(tiersecones[int(math.floor((layer-1)/(1000**layer2))-1)] + tiersec[(layer2)-1] + '-' + prefixones[int(layer%10)-1] + prefixtensbase[int(math.floor(((layer%100)-1)/10)-1)] + prefixhundreds[int(math.floor(((layer%1000)-1)/100))] + 'illion',end = ' ')
			if (layer%1000) < 11 and layer > 1000 and (layer/(1000**layer2)) <= 10:
				print(tiersecones[int(math.floor((layer-1)/(1000**layer2))-1)] + tiersec[(layer2)-1] + '-' + prefixbase[int(layer%10)-1] + prefixtens[int(math.floor(((layer%100)-1)/10))] + prefixhundreds[int(math.floor(((layer%1000)-1)/100))] + 'illion',end = ' ')
			if layer > 100 and layer < 1001:
				print(prefixones2[int(layer%10)-1] + prefixtens[int(math.floor(((layer%100)-1)/10))] + prefixhundreds[int(math.floor((layer-1)/100))] + 'illion',end = ' ')
			if layer > 10 and layer < 101 and oldnum-(int(oldnum)%(1000**(int(layer)))) != 0:
				print(prefixones[int(layer%10)-1] + prefixtensbase[int(math.floor((layer-1)/10)-1)] + 'illion',end = ' ')
			if layer > 1 and layer < 11 and oldnum-(int(oldnum)%(1000**(int(layer)))) != 0:
				print(prefixbase[int(layer-1)] + 'illion',end = ' ')
			if layer == 1 and (oldnum-(int(oldnum)%1000)) != 0:
				print('thousand', end = ' ')
			layer -= 1
			limit += 1

			
			
NumberConverter(mpf(number),mpf(layer))
		
