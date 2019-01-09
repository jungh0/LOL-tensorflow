import requests

fin = ""
fin2 = "" 
for i in range(0,10000):
	try:
		if i % 50 == 0:
			file = open('output.txt', 'a', encoding='utf8')
			file.write(fin)
			file.close()
			fin = ""
			print("save" + str(i))
			file = open('result.txt', 'a', encoding='utf8')
			file.write(fin2)
			file.close()
			fin2 = ""
		get = requests.get("http://op.gg/summoner/matches/ajax/detail/teamAnalysis/gameId=" + str(3412790236 - i) +"&moreLoad=1").content
		result_win = str(get).split('<div class="Value Result-WIN">')
		result_lose = str(get).split('<div class="Value Result-LOSE">')
		
		line = ""
		line2 = ""

		tmp1 = int(result_win[1].split('</div>')[0].replace(",",""))
		tmp2 = int(result_lose[1].split('</div>')[0].replace(",",""))
		win = ((tmp1 - tmp2) + 40) / 80
		lose = ((tmp2 - tmp1) + 40) / 80
		if (win > 1):
			win = 1
		if (win < 0):
			win = 0
		if (lose > 1):
			lose = 1
		if (lose < 0):
			lose = 0
		line = line + str(win) + ","
		line2 = line2 + str(lose) + ","

		tmp1 = int(result_win[2].split('</div>')[0].replace(",",""))
		tmp2 = int(result_lose[2].split('</div>')[0].replace(",",""))
		win = ((tmp1 - tmp2) + 40000) / 80000
		lose = ((tmp2 - tmp1) + 40000) / 80000
		if (win > 1):
			win = 1
		if (win < 0):
			win = 0
		if (lose > 1):
			lose = 1
		if (lose < 0):
			lose = 0
		line = line + str(win) + ","
		line2 = line2 + str(lose) + ","

		tmp1 = int(result_win[3].split('</div>')[0].replace(",",""))
		tmp2 = int(result_lose[3].split('</div>')[0].replace(",",""))
		win = ((tmp1 - tmp2) + 40000) / 80000
		lose = ((tmp2 - tmp1) + 40000) / 80000
		if (win > 1):
			win = 1
		if (win < 0):
			win = 0
		if (lose > 1):
			lose = 1
		if (lose < 0):
			lose = 0
		line = line + str(win) + ","
		line2 = line2 + str(lose) + ","

		tmp1 = int(result_win[4].split('</div>')[0].replace(",",""))
		tmp2 = int(result_lose[4].split('</div>')[0].replace(",",""))
		win = ((tmp1 - tmp2) + 40) / 80
		lose = ((tmp2 - tmp1) + 40) / 80
		if (win > 1):
			win = 1
		if (win < 0):
			win = 0
		if (lose > 1):
			lose = 1
		if (lose < 0):
			lose = 0
		line = line + str(win) + ","
		line2 = line2 + str(lose) + ","

		tmp1 = int(result_win[5].split('</div>')[0].replace(",",""))
		tmp2 = int(result_lose[5].split('</div>')[0].replace(",",""))
		win = ((tmp1 - tmp2) + 40000) / 80000
		lose = ((tmp2 - tmp1) + 40000) / 80000
		if (win > 1):
			win = 1
		if (win < 0):
			win = 0
		if (lose > 1):
			lose = 1
		if (lose < 0):
			lose = 0
		line = line + str(win) + ","
		line2 = line2 + str(lose) + ","

		tmp1 = int(result_win[6].split('</div>')[0].replace(",",""))
		tmp2 = int(result_lose[6].split('</div>')[0].replace(",",""))
		win = ((tmp1 - tmp2) + 400) / 800
		lose = ((tmp2 - tmp1) + 400) / 800
		if (win > 1):
			win = 1
		if (win < 0):
			win = 0
		if (lose > 1):
			lose = 1
		if (lose < 0):
			lose = 0
		line = line + str(win) + "\n"
		line2 = line2 + str(lose) + "\n"

		#print(line)
		#print(line2)
		fin = fin + line + line2
		fin2 = fin2 + "0,1\n" + "1,0\n"
	except:
		aa = ""
file = open('output.txt', 'a', encoding='utf8')
file.write(fin)
file.close()
fin = ""
print("save" + str(i))
file = open('result.txt', 'a', encoding='utf8')
file.write(fin2)
file.close()
fin2 = ""