from pymongo import MongoClient, DESCENDING

class DataBase_Table:

    def __init__(self, dbase):
        cluster = MongoClient(dbase, connectTimeoutMS=120000)
        db = cluster["admin"]
        self.collection = db["Collection_Notes"]


    def Count_Data(self):
        count_users = self.collection.count_documents({})
        # who_have_WebName = self.collection.count_documents({"User.Web.WebName": {"$exists": True, "$ne": None}})
        # Data = [count_users, who_have_Valentine]
        return count_users


    def AddUser(self, UserId, Referal_id, Username):
        try:
            UserId = str(UserId)
            Referal_id = str(Referal_id)
            Username = str(Username)

            highest_id_doc = self.collection.find_one(sort=[("_id", DESCENDING)])
            
            if highest_id_doc:
                highest_id = highest_id_doc['_id']
            else:
                highest_id = 0

            new_user = {
                '_id': highest_id + 1,
                "User": {
                    "ID": UserId,
                    "Username": Username,
                    "Referal": Referal_id,
                    "Time_Zone": False,
                    "QUESTS_FOR_TODAY": [],
                    "HISTORY_FINISH_TASKS": [],
                    "GOALS": None,
                    "STOP": False
                }
            }

            self.collection.insert_one(new_user)
        except Exception as error:
            print("Error AddUser", error)



    def Add_Time_Zone(self, UserId, Time_Zone):
        try:
            UserId = str(UserId)
            Time_Zone = str(Time_Zone)

            result = self.collection.find_one({'User.ID': UserId})
            self.collection.update_one(result, {"$set": {f"User.Time_Zone": Time_Zone}})
        except Exception as error:
            print("Error Add_Time_Zone", error)



    def Get_Time_Zone(self, UserId):
        try:
            UserId = str(UserId)
            result = self.collection.find_one({'User.ID': UserId})
            return result["User"]["Time_Zone"]
        except Exception as error:
            print("Error Get_Time_Zone", error)




    def Change_Time_Zone(self, UserId, new_region):
        try:
            UserId = str(UserId)
            new_region = str(new_region)

            result = self.collection.find_one({'User.ID': UserId})
            self.collection.update_one(result, {"$set": {f"User.Time_Zone": new_region}})
        except Exception as error:
            print("Error Del__fear_and_greed", error)



    def ACTIONS_STOP(self, UserId, action="get"):
            try:
                UserId = str(UserId)

                if action == "True":
                    self.collection.update_one(
                        {'User.ID': UserId},
                        {"$set": {f"User.STOP": True}}
                    )

                elif action == "False":
                    self.collection.update_one(
                        {'User.ID': UserId},
                        {"$set": {f"User.STOP": False}}
                    )

                elif action == "get":
                    result = self.collection.find_one({'User.ID': UserId})
                    return result["User"]["STOP"]
                    
                else:
                    print("Invalid action or missing index for update.")

            except Exception as error:
                print("Error in STOP:", error)




    def ACTIONS_QUESTS_FOR_TODAY(self, UserId, text=None, action="add", index=None):
        try:
            UserId = str(UserId)

            if action == "add":
                self.collection.update_one(
                    {'User.ID': UserId},
                    {"$push": {"User.QUESTS_FOR_TODAY": text}}
                )

            elif action == "remove_by_text":
                self.collection.update_one(
                    {'User.ID': UserId},
                    {"$pull": {"User.QUESTS_FOR_TODAY": text}}
                )

            elif action == "remove_by_index":
                document = self.collection.find_one({'User.ID': UserId})
                if document:
                    quests = document.get('User', {}).get('QUESTS_FOR_TODAY', [])
                    if 0 <= index < len(quests):
                        quests.pop(index)
                        self.collection.update_one(
                            {'User.ID': UserId},
                            {"$set": {"User.QUESTS_FOR_TODAY": quests}}
                        )


            elif action == "get_by_index":
                document = self.collection.find_one({'User.ID': UserId})
                if document:
                    quests = document.get('User', {}).get('QUESTS_FOR_TODAY', [])
                    if 0 <= index < len(quests):
                        return quests[index]


            elif action == "update" and index is not None:
                self.collection.update_one(
                    {'User.ID': UserId},
                    {"$set": {f"User.QUESTS_FOR_TODAY.{index}": text}}
                )


            elif action == "get":
                result = self.collection.find_one({'User.ID': UserId})
                if result and "User" in result and "QUESTS_FOR_TODAY" in result["User"]:
                    return result["User"]["QUESTS_FOR_TODAY"]
                else:
                    return None


            elif action == "get_morning_tasks":
                result = self.collection.find_one({'User.ID': UserId})
                if result and "User" in result and "QUESTS_FOR_TODAY" in result["User"]:

                    data = result["User"]["QUESTS_FOR_TODAY"]
                    last_morning_index = None
                    for i in range(len(data) - 1, -1, -1):
                        if data[i] == '———— 🔆 MORNING ————':
                            last_morning_index = i
                            break

                    if last_morning_index is not None:
                        result = data[last_morning_index:]
                    else:
                        result = []

                    return result, int(len(data) - len(result))

                else:
                    return None
                
            else:
                print("Invalid action or missing index for update.")

        except Exception as error:
            print("Error in Add_QUESTS_FOR_TODAY:", error)




#############################################################################################################################################


    def ACTIONS_HISTORY_FINISH_TASKS(self, UserId, text=None, action="add", index=None, date=None):
        try:
            UserId = str(UserId)
            date_key = str(date)

            # # Шаг 1: Обновляем структуру, если HISTORY_FINISH_TASKS всё ещё массив
            # self.collection.update_one(
            #     {'User.ID': UserId, 'User.HISTORY_FINISH_TASKS': {"$type": "array"}},
            #     {"$set": {'User.HISTORY_FINISH_TASKS': {}}}
            # )

            if action == "add":
                self.collection.update_one(
                    {'User.ID': UserId},
                    {"$push": {f"User.HISTORY_FINISH_TASKS.{date_key}": f"✅ {text}"}}
                )

            elif action == "add_foul":
                self.collection.update_one(
                    {'User.ID': UserId},
                    {"$push": {f"User.HISTORY_FINISH_TASKS.{date_key}": f"❌ {text}"}}
                )

            # elif action == "remove_by_text":
            #     self.collection.update_one(
            #         {'User.ID': UserId},
            #         {"$pull": {"User.HISTORY_FINISH_TASKS": text}}
            #     )

            # elif action == "remove_by_index":
            #     document = self.collection.find_one({'User.ID': UserId})
            #     if document:
            #         quests = document.get('User', {}).get('HISTORY_FINISH_TASKS', [])
            #         if 0 <= index < len(quests):
            #             quests.pop(index)
            #             self.collection.update_one(
            #                 {'User.ID': UserId},
            #                 {"$set": {"User.HISTORY_FINISH_TASKS": quests}}
            #             )


            # elif action == "update" and index is not None:
            #     self.collection.update_one(
            #         {'User.ID': UserId},
            #         {"$set": {f"User.HISTORY_FINISH_TASKS.{index}": text}}
            #     )

            elif action == "get":
                result = self.collection.find_one({'User.ID': UserId})
                if result and "User" in result and "HISTORY_FINISH_TASKS" in result["User"]:
                    return result["User"]["HISTORY_FINISH_TASKS"]
                else:
                    return None

            else:
                print("Invalid action or missing index for update.")

        except Exception as error:
            print("Error in Add_HISTORY_FINISH_TASKS:", error)




    def ACTIONS_FOR_QUEUE(self, action="add", queue=None, UnicKey_input=None):

        if action == "add":
            try:
                self.collection.update_one(
                    {"name": "example"},
                    {"$push": {"FreeQueueData": queue}}
                )

            except Exception as error:
                print("Error AddQueue", error)


        elif action == "get":
            try:
                result = self.collection.find_one({"name": "example"})
                return result["FreeQueueData"]
            except Exception as error:
                print("Error GetQueue", error)


        elif action == "delete":
            try:
                num = 0
                data_list = self.ACTIONS_FOR_QUEUE(action="get")
                for i in data_list:
                    UnicKey = i["UnicKey"]
                    if UnicKey == UnicKey_input:

                        data_list.pop(num)
                        self.collection.update_one(
                            {"name": "example"},
                            {"$set": {"FreeQueueData": data_list}}
                        )

                        break
                    num+=1
            except Exception as error:
                print("Error DeleteQueue", error)



    def CheckRegistr(self, UserId):
        try:
            UserId = str(UserId)

            result = self.collection.find_one({'User.ID': UserId})
            return bool(result)
        except Exception as error:
            print("Error CheckRegistr", error)



    # def CheckUnicKey(self, UserId_getnode):
    #     try:
    #         result = self.collection.find_one({'User.ID': UserId_getnode})
    #         # print(bool(result["User"]["UnicKey"]))
    #         return bool(result["User"]["UnicKey"])
    #     except Exception as error:
    #         print("Error CheckUnicKey", error)


    # def SavePaths(self, UserId_getnode, list_with_paths):
    #     try:         
    #         result = self.collection.find_one({'User.ID': UserId_getnode})
    #         for path in list_with_paths:
    #             true_path = path.replace("\\", "/")
    #             self.collection.update_one(result, {"$set": {f"User.PATHs_to_Telegram": true_path}})
    #     except Exception as error:
    #         print("Error SavePaths", error)

    
    # def GetSavePaths(self, UserId_getnode):
    #     try:
    #         result = self.collection.find_one({'User.ID': UserId_getnode})
    #         print(result["User"]["PATHs_to_Telegram"])
    #         return result["User"]["PATHs_to_Telegram"]
    #     except Exception as error:
    #         print("Error CheckSavePaths", error)


    # def GetUsersAll(self):
    #     try:
    #         user_ids = []
    #         users = self.collection.find({}, {"User.ID": 1})
    #         for user in users:
    #             user_ids.append(user["User"]["ID"])
    #         return user_ids
    #     except Exception as error:
    #         print("Error GetUsersAll", error)


db = DataBase_Table("mongodb://expin1226707:.aRTTIG12267@91.107.123.97:37757/admin")
# a = {"UserId":"23527457", "now_date":"0579864", "time_before":"23456245627", "data_type":"remember", "msg_text":"jsrjzrjryhj", "UnicKey":"ADaktnhx"}

# new_user = {
#     '_id': 0,
#     "name": "example",
#     "FreeQueueData": []
# }

# db.collection.insert_one(new_user)
# db.ACTIONS_FOR_QUEUE(action="delete", UnicKey_input="5VLp634bPD9dXflvFiVJJiNde0a6CsaETaBwlHDe")
# a = db.GetQueue()
# for i in a:
#     print(i["UserId"])
# print(a)
# db.DeleteQueue('hrshbsrth')

# print(db.ACTIONS_QUESTS_FOR_TODAY(324430515, action="get_morning_tasks"))
# db.Add_Time_Zone()
# db.SavePaths()
# # Подключение к MongoDB
# client = MongoClient("mongodb://expin1226707:.aRTTIG12267@91.107.123.97:37757/admin")

# # Выполнение запроса serverStatus для получения информации о сервере
# server_status = client.admin.command("serverStatus")

# # Вывод информации о подключениях
# print("Максимальное количество подключений:", server_status)

# # Закрытие соединения с MongoDB
# client.close()

# db.collection.insert_one(new_user)

# db.AddFreeKey("bhertbjtej")
# a = db.GetFreeKey()
# print(a)
# for i in a:
#     print(i)

# data = db.ACTIONS_HISTORY_FINISH_TASKS(UserId="324430515", action="get")
# for date, entries in data.items():
#     print(date)
#     for entry in entries:
#         print(f'    {entry}')


# a = db.ACTIONS_QUESTS_FOR_TODAY(f"324430515", index=int(0), action="get_by_index")
# print(a)
