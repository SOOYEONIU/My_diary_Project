from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
from .models import Daily_diary1
from datetime import datetime
import json

#JSON 설계
class MakeJSON :
	def __init__(self):
		pass

	@staticmethod
	def printJSON():
		diaryJSON = {"diaryInfo": []}
		diary_list = Daily_diary1.objects.order_by('id')
		for diaryData in diary_list:
			json_output = {}
			
			json_output["id"] = diaryData.id
			json_output["created_date"] = diaryData.diary_created_date
			json_output["updated_date"] = diaryData.diary_updated_date
			json_output["diary_title"] = diaryData.diary_title
			json_output["diary_contents"] = diaryData.diary_contents
			diaryJSON["diaryInfo"].append(json_output)
			#print(diaryJSON)

			
		with open('diaryData.json', 'w')as f:
			json.dump(diaryJSON, f, default=str, ensure_ascii=False, indent=4)

def diary_index(request):
	MakeJSON.printJSON()
	
	url = f'http://kkms4001.iptime.org/~c18st04/portfolio/project_diary/project_frontEnd/diary_mainPage.html'
	return redirect(url)


#데이터 CREATE
@csrf_exempt
def diary_create(request):
	if( request.POST["created_date"] != '' and request.POST["diary_title"] != '' and request.POST["diary_contents"] != ''):
		newDaily_diary = Daily_diary1(diary_created_date = request.POST["created_date"], diary_title = request.POST["diary_title"], diary_contents = request.POST["diary_contents"])
		newDaily_diary.save()
	
	MakeJSON.printJSON()

	url = f'http://kkms4001.iptime.org/~c18st04/portfolio/project_diary/project_frontEnd/diary_mainPage.html?date={request.POST["created_date"]}'
	return redirect(url)

#데이터 DELETE
@csrf_exempt
def diary_delete(request, id):
	remove_diary = Daily_diary1.objects.get(id = id)
	remove_diary.delete()

	MakeJSON.printJSON()

	url = 'http://kkms4001.iptime.org/~c18st04/portfolio/project_diary/project_frontEnd/diary_mainPage.html'
	return redirect(url)

#데이터 UPDATE
@csrf_exempt
def diary_update(request, id):
	update_diary = Daily_diary1.objects.get(id = id)
	update_diary.diary_title = request.POST["dailyTitle"]
	update_diary.diary_contents = request.POST["dailyContext"]
	update_diary.save()

	MakeJSON.printJSON()

	url = f'http://kkms4001.iptime.org/~c18st04/portfolio/project_diary/project_frontEnd/diary_readPage.html?id={id}'
	return redirect(url)

