from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import random
import sys

def login2(driver, firstTime):
	play_friend = "/html/body/div[7]/div/div/md-content/div/div/div/div/div[1]/div/div[2]/div[2]/button[2]"
	find_opponent_button = "/html/body/div[7]/div/div/md-content/div/div/div/div/div[1]/div/div[2]/div[2]/button[1]"
	name_input = "/html/body/div[11]/md-dialog/div/div[1]/div[1]/input"
	next_button = "/html/body/div[12]/md-dialog/div/div[1]/div[3]/button"
	paper_man_button = "/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/div[4]/div/ng-include/div/div[2]/button"
	print("1")
	time.sleep(3)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, find_opponent_button))).click()
	print("2")
	driver.find_element_by_xpath("/html/body/div[11]/md-dialog/div/div[1]/div[1]/input").send_keys("test")
	driver.find_element_by_xpath("/html/body/div[11]/md-dialog/div/div[1]/div[3]/button/span").click()
	#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, name_input))).send_keys("Bax")
	#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
	time.sleep(3)
	starting_url = driver.current_url
	try:
		find_element_by_xpath("/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/points-booster/div/div[3]/p/a").click()
	except:
		print("no block")
	print("start: " + starting_url)
	t1 = time.time()
	while (time.time() - t1 < 30):
		if driver.current_url != starting_url:
			print("Game found")
			time.sleep(5)
			return 1
def login(driver, firstTime):
	"""driver.get("https://papergames.io")
	email = "fetak37470@hype68.com"
	password = "botpassword"
	login_button = "/html/body/div[7]/div/md-sidenav/div/div[1]/md-list/md-list-item[7]/button"
	hamburger = "/html/body/div[7]/div/div/md-toolbar/div[1]/button"
	email_field = '//*[@id="mainBody"]/form/div[1]/div/div[3]/div[1]/input'
	login_form = "/html/body/div/div/div/div[1]/div/div/div/form"
	find_opponent_button = "/html/body/div[7]/div/div/md-content/div/div/div/div/div[1]/div/div[2]/div[2]/button[1]"
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, hamburger))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, login_button))).click()
	time.sleep(20)
	driver.get("https://papergames.io/en/connect4")
	time.sleep(30)
	
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, find_opponent_button))).click()
	time.sleep(1.5)
	starting_url = driver.current_url
	print(starting_url)
	t1 = time.time()
	while (time.time() - t1 < 30):
		if driver.current_url != starting_url:
			print("Game found")
			read(driver)
			return 1
	"""
	play_friend = "/html/body/div[7]/div/div/md-content/div/div/div/div/div[1]/div/div[2]/div[2]/button[2]"
	find_opponent_button = "/html/body/div[7]/div/div/md-content/div/div/div/div/div[1]/div/div[2]/div[2]/button[1]"
	name_input = "/html/body/div[12]/md-dialog/div/div[1]/div[1]/input"
	next_button = "/html/body/div[12]/md-dialog/div/div[1]/div[3]/button"
	paper_man_button = "/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/div[4]/div/ng-include/div/div[2]/button"
	try:
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, find_opponent_button))).click()
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, name_input))).send_keys("Bax")
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
		#time.sleep(3)
		if firstTime:
			print("I'm trying")
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, name_input))).send_keys("Bax")
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
		time.sleep(3)
		starting_url = driver.current_url
		try:
			find_element_by_xpath("/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/points-booster/div/div[3]/p/a").click()
		except:
			print("no block")
		print("start: " + starting_url)
		t1 = time.time()
		while (time.time() - t1 < 30):
			if driver.current_url != starting_url:
				print("Game found")
				time.sleep(5)
				return 1
	except:
		time.sleep(3)
		login(driver, firstTime)
	#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, name_input))).send_keys("Bax")
	#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
	#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, paper_man_button))).click()

	return 0
def read(driver):
	board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
	for i in range(1,8):
		for j in range(1,7):
			cell_source = driver.find_element_by_xpath("/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/div[2]/game-connect4/div/div/table/tbody/tr[" + str(j) + "]/td[" + str(i) + "]/span/img").get_attribute('src')
			if cell_source == "https://papergames.io/images/symbols/circle-placeholder-bright.svg":
				board[j-1][i-1] = 0
			elif cell_source == "https://papergames.io/images/symbols/circle-dark.svg":
				board[j-1][i-1] = 1
			elif cell_source == "https://papergames.io/images/symbols/circle-light.svg":
				board[j-1][i-1] = 2
	#for row in board:
	#	print(row)
	return board
def computeCell(board):
	open_spots = []
	for i in range(0, 7):
		if board[0][i] == 0:
			open_spots.append(i)				
	#print(open_spots)
	return int(random.choice(open_spots)) + 1
def chooseCell(column, driver):
	driver.find_element_by_xpath("/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/div[2]/game-connect4/div/div/table/tbody/tr[1]/td[" + str(column) + "]/span/img").click()
	time.sleep(0.2)
	starting_time = driver.find_element_by_xpath("/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/div[3]/div/ng-include/div/div[1]/user/div[2]/timer").text
	while driver.find_element_by_xpath("/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/div[3]/div/ng-include/div/div[1]/user/div[2]/timer") == starting_time:
		time.sleep(0.1)
	return 1
def findStarting(driver):
	right_name = driver.find_element_by_xpath("/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/div[3]/div/ng-include/div/div[2]/user/div[2]/div[1]/a").text
	if right_name[0:3] == "Bax":
		return 1
	else:
		return 2
def waitForTurn(driver):
	initial = read(driver)
	print("Waiting at this:")
	for row in initial:
		print row
	while (read(driver) == initial):
		time.sleep(0.1)
	return 1
def mockThem(driver):
	return None
def finishGame(driver):
	return None
def run(firstTime):
	driver.get("https://papergames.io/en/connect4")
	time.sleep(3)
	if firstTime:
		print("starting...")
		driver.switch_to.window(driver.window_handles[0])
	login2(driver, firstTime)
	time.sleep(10)
	starting_role = findStarting(driver)
	if starting_role == 2:
		print("I'm starting")
	else:
		print("I'm second")
	for i in range(50):
		try:
			find_element_by_xpath("/html/body/div[7]/div/div/md-content/div/div/div/div/div/div/div[2]/div[3]/div/div/div[3]/button").click()
		except:
			try:
				chooseCell(computeCell(read(driver)), driver)
				print("chose cell, waiting for them to go")
				waitForTurn(driver)
				print("It's my turn now")
			except:
				print("game over")
				run(False)
path_to_extension = "/Users/baxterbarlow/Library/Application Support/Google/Chrome/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/4.32.1_0"
chrome_options = Options()
print("here")
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome("/Users/baxterbarlow/Desktop/chromedriver", chrome_options=chrome_options)
driver.create_options()
run(True)
#driver = webdriver.Chrome("/Users/baxterbarlow/Desktop/chromedriver")
#if login(driver) == 0:
#	print("Couldn't get into a game")
#time.sleep(20)

#read(driver)


#fetak37470@hype68.com
#botpassword