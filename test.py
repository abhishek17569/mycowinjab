# from datetime import date

# # def today_date():
# #     today = date.today()
# #     today_date = today.strftime("%d-%m-%Y")
# #     # print(today_date)

# #     return today_date

# # print(today_date())

response= requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=173205&date=09-05-2021')
response = response.text
dic= json.loads(response)
#dic = dict({"centers":[{"center_id":579408,"name":"ESI HOSPT OKHLA SITE 2","address":"Okla Phase-1","state_name":"Delhi","district_name":"South East Delhi","block_name":"Not Applicable","pincode":110020,"lat":28,"long":77,"from":"09:00:00","to":"17:00:00","fee_type":"Free",""'sessions'"":[{"session_id":"3797808b-48a2-4173-8610-09163628f2af","date":"07-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"3ec4141c-872f-49d3-98f8-1f3fd19b537c","date":"08-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-06:00PM"]},{"session_id":"98e411fd-ae79-429f-a1ab-084d8dca980a","date":"10-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-06:00PM"]},{"session_id":"77fb20d1-922e-4906-90f7-2b9d1020712d","date":"11-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-06:00PM"]},{"session_id":"12408e47-5fb5-480a-b035-978f17957fef","date":"12-05-2021","available_capacity":49,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-06:00PM"]},{"session_id":"1ce71363-8f7c-46b2-b0a3-2016a0480674","date":"13-05-2021","available_capacity":92,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-06:00PM"]}]},{"center_id":8148,"name":"MCW Nehru Nagar PHC","address":"H.No. 1, Block-10, Near-Jhule Lal Mandir, Nehru Nagar, New Delhi-110065","state_name":"Delhi","district_name":"South East Delhi","block_name":"Not Applicable","pincode":110020,"lat":28,"long":77,"from":"09:00:00","to":"17:00:00","fee_type":"Free",""'sessions'"":[{"session_id":"612fbfe6-63c9-43a9-8fcd-04fd7bdb3d0f","date":"08-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"fe69525b-42a9-49b4-9dc5-1d755096304f","date":"10-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"eaeb3e51-47dd-4ed8-aba4-0e0162e0af24","date":"11-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"07893545-b653-48e6-8d69-b8db2d674e5c","date":"13-05-2021","available_capacity":19,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]}]},{"center_id":605453,"name":"SPUHC Jasola","address":"Jasola Village","state_name":"Delhi","district_name":"South East Delhi","block_name":"Not Applicable","pincode":110020,"lat":28,"long":77,"from":"09:00:00","to":"17:00:00","fee_type":"Free",""'sessions'"":[{"session_id":"6720f634-c37d-4bc4-b9b1-b95d56cefc6e","date":"08-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVISHIELD","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"121cb102-09c8-4721-9f98-f06550d61247","date":"10-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVISHIELD","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"ee5184e7-3522-436c-b0bf-2743b930dbb9","date":"11-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVISHIELD","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"6200bc77-200c-418c-bffa-118115c5c8ce","date":"13-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVISHIELD","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]}]},{"center_id":627894,"name":"ESI Modi Mill","address":"Okhla Industrial Area, Modi Mills, Okhla NEW DELHI","state_name":"Delhi","district_name":"South East Delhi","block_name":"Not Applicable","pincode":110020,"lat":0,"long":0,"from":"09:00:00","to":"17:00:00","fee_type":"Free",""'sessions'"":[{"session_id":"092a661e-f565-4ef9-a623-cb7587c51564","date":"08-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"80a6539b-6a7e-45a9-bf57-ba9371be92f3","date":"10-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"ca166c7c-f2ab-48a3-a9f8-c19ec8381789","date":"11-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"3d2e56ee-61fb-4749-ac41-b5638b611431","date":"13-05-2021","available_capacity":13,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]}]},{"center_id":8830,"name":"MCW Okhla Phase I PHC","address":"Near JJ Slum Primary School MCD,DDA Flats KalkajiNew Delhi 110019","state_name":"Delhi","district_name":"South East Delhi","block_name":"Not Applicable","pincode":110020,"lat":28,"long":77,"from":"09:00:00","to":"17:00:00","fee_type":"Free",""'sessions'"":[{"session_id":"98c110c9-a2a0-45f1-bb4d-e723072857b5","date":"08-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"4ac6350c-21d2-4d33-ac5d-9173d1630f70","date":"10-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"14d3d0fe-a0c9-4e5e-88cc-677237c7e839","date":"11-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"a42bdc7c-3855-459c-824d-c16869ab1662","date":"13-05-2021","available_capacity":61,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]}]},{"center_id":8163,"name":"ESI Hospital Okhla Phase 1 DH","address":"Okla Phase-1","state_name":"Delhi","district_name":"South East Delhi","block_name":"Not Applicable","pincode":110020,"lat":28,"long":77,"from":"09:00:00","to":"17:00:00","fee_type":"Free",""'sessions'"":[{"session_id":"a2714ada-d995-4c3e-8987-7f606450fcbc","date":"08-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"5568e609-9058-4010-b660-8f27915bfb8f","date":"10-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"0b42a6b5-3107-43d9-aa4f-addfa5d51584","date":"11-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"26ed260e-1e58-4b8f-81a2-1cd317838672","date":"12-05-2021","available_capacity":0,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]},{"session_id":"4545c697-29b9-4c3c-86bb-b3a37c7e01f7","date":"13-05-2021","available_capacity":49,"min_age_limit":45,"vaccine":"COVAXIN","slots":["09:00AM-11:00AM","11:00AM-01:00PM","01:00PM-03:00PM","03:00PM-05:00PM"]}]}]})
vaccine = 0
centre = dic["centers"]
# print(type(centre))
for li in centre:
    # print(type(li))
    print("Centre Name:", li['name'], "\nCentre Address:", li['address'], li['block_name'], li['district_name'], li['pincode'],"\nFee Type:",li['fee_type']) #, li["'sessions'"][0]['date'], li["'sessions'"][0]['date'], li["'sessions'"][0]['available_capacity'], li["'sessions'"][0]['min_age_limit'])
    # print(li[""'sessions'""])
    for session in li["sessions"]:
        print(session['date'], session['available_capacity'], session['min_age_limit'], session['vaccine'])
        vaccine=vaccine+session['available_capacity']
print(session['min_age_limit'])
print(vaccine)