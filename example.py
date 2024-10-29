import requests


HOST = "https://uauirt-admin.bars.group/api"

login_payload = {
    "Login": "admin",
    "Password": "root"
}

#1 Залогинились
response = requests.post(
    url=f"{HOST}/Security/Login",
    headers={"Authorization": "Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjMiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYWRtaW4iLCJJc0FkbWluIjoiVHJ1ZSIsImV4cCI6MTczMDIzMDM2MSwiaXNzIjoibG9jYWxob3N0IiwiYXVkIjoibG9jYWxob3N0In0.2VUVaE2Ce-NyEE29flfWSUO0hUoh-DgHBekeB3oHe4E"},
    json=login_payload
)

print(response.status_code)

#2 Получаем список физ лиц
response = requests.post(
    url=f"{HOST}/PhysicalPerson/List",
    headers={"Authorization": "Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjMiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYWRtaW4iLCJJc0FkbWluIjoiVHJ1ZSIsImV4cCI6MTczMDIzMDM2MSwiaXNzIjoibG9jYWxob3N0IiwiYXVkIjoibG9jYWxob3N0In0.2VUVaE2Ce-NyEE29flfWSUO0hUoh-DgHBekeB3oHe4E"},
)

print(response.json())
